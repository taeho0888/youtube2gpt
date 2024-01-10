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

## 코드 업데이트
#### 1. 업데이트된 코드 되돌리기
<img width="309" alt="image" src="https://github.com/taeho0888/youtube2gpt/assets/105200642/ac30e559-aa05-4338-b491-862802a12e12">

- 이렇게 `파란색` + `M 표시`가 있는 파일들은 깃허브에서 다운 받은 후에 형 컴퓨터에서 변경되었다는 뜻!
- 그래서 얘네가 변경되기 전 상태로 되돌려져야지 새로운 코드로 업데이트 할 수 있다.
- `파란색` + `M 표시` 되어있는 애가 없으면 이 부분 건너뛰어도 됨

<img width="344" alt="image" src="https://github.com/taeho0888/youtube2gpt/assets/105200642/c9db208f-f5c9-4c37-b9db-686656a52834">

- 맨 왼쪽 바에서 `세번째 아이콘`을 클릭하고 `변경사항` -> `모든 변경 내용 취소`를 눌러준다

<img width="292" alt="image" src="https://github.com/taeho0888/youtube2gpt/assets/105200642/cb1ddf95-6154-4ad5-bbc0-52fdae8f4b8e">

- 얄짤없이 버려줌

#### 2. git pull

터미널에 아래 명령어 입력
```bash
git pull origin main
```
하면 끝입니당~ 다시 실행 가능


## 주의사항
1. 엑셀 `D열`은 유튜브 링크, `E열`은 유튜브 스크립트, `F열`은 GPT 요약, `G열`은 블로그 (TODO)
2. 엑셀을 저장하고 종료한 뒤 실행 커맨드 입력
