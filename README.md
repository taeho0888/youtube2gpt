# youtube2gpt

## 초기 세팅
#### 1. 코드 다운로드
```bash
git clone https://github.com/taeho0888/youtube2gpt.git .
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
#### 2. 환경변수 설정
`.env` 파일 생성 후 OPENAI KEY 입력
```
OPENAI_API_KEY = your openai api key
```

## 실행
#### 1. VS Code 열기
#### 2. 코드 있는 폴더 열기
#### 3. 가상환경 실행
```bash
source .venv/bin/activate
```
#### 4. 엑셀에 유튜브 링크 복붙
#### 5. 실행
```bash
python3 main.py
```
#### 6. 엑셀 껐다 키기

## 주의사항
1. 엑셀 `D열`은 유튜브 링크, `E열`은 유튜브 스크립트, `F열`은 GPT 요약, `G열`은 블로그 (TODO)
2. 엑셀을 저장하고 종료한 뒤 실행 커맨드 입력
