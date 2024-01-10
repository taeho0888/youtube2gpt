import asyncio
from youtube_transcript_api import YouTubeTranscriptApi

MAX_SCRIPT_LENGTH = 2000

class YouTubeScriptExtractor:
    def __init__(self, sheet, input_column, output_column):
        self.sheet = sheet
        self.input_column = input_column
        self.output_column = output_column
        self.rows = [row for row in sheet.iter_rows(min_row=3, min_col=input_column, max_col=input_column)]

    def get_video_id(self, youtube_link):
        try:
            return youtube_link.split("?v=")[1]
        except Exception as e:
            return None

    async def extract_script(self, youtube_id):
        try:
            loop = asyncio.get_event_loop()
            scripts = await loop.run_in_executor(None, YouTubeTranscriptApi.get_transcript, youtube_id, ['ko'])
            script = " ".join(script["text"] for script in scripts)
            print(script[:MAX_SCRIPT_LENGTH])
            return script[:MAX_SCRIPT_LENGTH]
        except Exception as e:
            return "[오류] : 스크립트 추출 실패"

    async def process_row(self, row):
        if self.sheet.cell(row=row[0].row, column=self.output_column).value:
            return

        video_id = self.get_video_id(row[0].value)
        if video_id is None:
            return

        if video_id:
            content = await self.extract_script(video_id)
        else:
            content = f"[오류] : {row[0].value}는 올바른 URL이 아닙니다."
            print(content)

        self.sheet.cell(row=row[0].row, column=self.output_column, value=content)

    async def process_scripts(self):    
        tasks = [self.process_row(row)for row in self.rows]
        await asyncio.gather(*tasks)
