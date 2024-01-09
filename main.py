import openpyxl
from youtube import YouTubeScriptExtractor
from gpt import GPTChatProcessor


if __name__ == "__main__":
    # 엑셀 파일 열기
    wb = openpyxl.load_workbook("youtube.xlsx")
    sheet = wb.worksheets[0]

    # 유튜브 클래스 호출 후 자막 추ㅜㄹ
    youtube_extractor = YouTubeScriptExtractor()
    youtube_extractor.process_scripts(sheet, input_column=4, output_column=5)

    # 지피티 클래스 호출 후 서머리 추출
    gpt_processor = GPTChatProcessor()
    gpt_processor.generate_summary(sheet, input_column=5, output_column=6)

    # Save changes
    wb.save("youtube.xlsx")
    wb.close()