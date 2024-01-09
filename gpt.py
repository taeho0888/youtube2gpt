import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class GPTChatProcessor:
    def __init__(self):
        self.gpt = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def generate_summary(self, sheet, input_column, output_column):
        for row in sheet.iter_rows(min_row=3, min_col=input_column, max_col=input_column):
            if sheet.cell(row=row[0].row, column=output_column).value:
                continue

            script = row[0].value

            if script.startswith("[오류]"):
                continue

            response = self.gpt.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": """
                        You are a summarizer and I'm a client. 
                        I'll give you the script of a YouTube video, and you should summarize that. 
                        Please summarize the video script and divide it into several paragraphs.
                    """},
                    {"role": "user", "content": f"{script}"}
                ]
            )

            summary = response['choices'][0]['message']['content']
            print(summary)

            sheet.cell(row=row[0].row, column=output_column, value=summary)
