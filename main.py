import openpyxl
import asyncio
import timeit
from youtube import YouTubeScriptExtractor
from gpt import GPTChatProcessor

async def main():
    # 엑셀 파일 열기
    wb = openpyxl.load_workbook("youtube.xlsx")
    sheet = wb.worksheets[0]

    # 유튜브 클래스 호출 후 자막 추출
    youtube_extractor = YouTubeScriptExtractor(sheet, input_column=4, output_column=5)
    await youtube_extractor.process_scripts()

    # 지피티 클래스 호출 후 서머리 추출
    gpt_processor = GPTChatProcessor(sheet, input_column=5, output_column=6)
    await gpt_processor.generate_summary()

    # Save changes
    wb.save("youtube.xlsx")
    wb.close()


def wrapper():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
    # elapsed_time = timeit.timeit(wrapper, number=1)
    # print(f"비동기: {elapsed_time * 1000:.2f}ms")