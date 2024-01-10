import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROMPT = """
            You are a summarizer and I'm a client. 
            I'll give you the script of a YouTube video, and you should summarize that. 
            Please summarize the video script and divide it into several paragraphs.
            Please give me a summary of the summary you just sent me by numbering it so that I can see it at a glance.
            Write it with Korean.
        """

class GPTChatProcessor:
    def __init__(self, sheet, input_column, output_column):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.sheet = sheet
        self.input_column = input_column
        self.output_column = output_column
        self.rows = [row for row in sheet.iter_rows(min_row=3, min_col=input_column, max_col=input_column)]

    def generate(self, row):
        if self.sheet.cell(row=row[0].row, column=self.output_column).value:
            return

        script = row[0].value
        if not script or script.startswith("[오류]"):
            return

        try:
            # 최대 토큰 4,096 = 4,800 character
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"{PROMPT}"},
                    {"role": "user", "content": f"{script}"}
                ],
                max_tokens=2000,
                temperature=1
            )
            print(response + "\n")
            summary = str(response.choices[0].message.content)
        except Exception as e:
            summary = f"[GPT 오류] : {e}"
            print(summary)


        self.sheet.cell(row=row[0].row, column=self.output_column, value=summary)

    def generate_summary(self):
        tasks = [self.generate(row) for row in self.rows]

        # await asyncio.gather(*tasks)