# youtube2gpt

## 초기 세팅
```bash
git clone https://github.com/taeho0888/youtube2gpt.git .
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## 환경변수 설정
1. `.env` 파일 생성 후 OPENAI KEY 입력
```
OPENAI_API_KEY = your openai api key
```

## 가상환경 실행
```bash
source .venv/bin/activate
```

## 실행
```bash
python3 main.py
```

###주의사항
1. 엑셀 `D열`은 유튜브 링크, `E열`은 유튜브 스크립트, `F열`은 GPT 요약, `G열`은 블로그 (TODO)
2. 엑셀을 저장하고 종료한 뒤 실행 커맨드 입력
