# 아래 단계를 따라하면 파이썬애니웨어 사용이 안 됨. 사용할 수 있는 방법 알아내서 수정할 것

웹앱을 파이썬애니웨어에 배포하는 과정을 다룰 것이다. 파이썬애니웨어는 flask를 지원하며 비용을 지불하지 않고 시작할 수 있다. 

## 0단계 : 준비 

아래 그림처럼 webapp이라는 폴더에 웹앱 코드를 저장했다. 파일과 폴더는 아래 그림과 같이 있고 모든 파일들을 webapp.zip으로 압축한다. 

![image](https://github.com/sjHong645/head-first-python/assets/64796257/89a5f0ef-069d-47a6-b102-fd687746b7dd)

뿐만 아니라 4장에서 배운 `vsearch 모듈`도 업로드하고 설치해야 한다. 
- 위치 : chapter4-functionAndModule/mymodules/dist/vsearch-1.0.tar.gz

지금 당장 두 파일로 아무 작업도 할 필요가 없다. 나중에 파이썬애니웨어로 두 파일을 업로드하기만 할 거다. 

## 1단계 : 파이썬애니웨어 가입 

## 2단계 : 파일을 클라우드에 업로드 

1. Recent Files 탭 클릭
2. Upload a file 버튼 이용해서 vsearch 모듈 압축파일, webapp 압축파일 업로드

## 3단계 : 업로드한 파일의 코드 추출 및 설치 

1. Open Bash console here 클릭 > 그러면 터미널 창이 열린다. 
2. vsearch 모듈을 설치한다.  
   a. `python3 -m pip install vsearch-1.0.tar.gz --user`
   b. --user 옵션을 이용해서 vsearch 모듈을 우리만 사용할 수 있도록 설치함
3. 웹앱 코드를 mysite 폴더에 설치한다. (폴더가 없으면 만들면 됨)  
   a. `unzip webapp.zip`
   b. `mv webapp/* mysite`

## 4단계 : 스타터 웹앱 만들기 

1. 우측 상단 구석 > 설정 > Web 클릭 : 여기서 새로운 스타터 웹앱을 만든다.
2. Add a new web app 클릭 > (username).pythonanywhere.com을 도메인으로 지정한다는 화면이 나옴 > Next  
   a. 만약 도메인 이름을 원하는 대로 변경하고 싶으면 요금제를 구독해야 함
3. Flask를 선택한 다음 배포하려는 파이썬 버전과 플라스크 버전을 선택한다. (최신버전을 선택하도록 하자)
   a. 파이썬애니웨어는 2개 이상의 파이썬 웹 프레임워크를 지원한다. 목록 중에서 원하는 시스템을 선택해주면 된다.
4. Quickstart new Flask project 창 > Next 클릭

4단계를 완료하면 Web 대시보드가 나타난다. 아직 파이썬애니웨이에 내 코드를 설정하지 않았으므로 `Reload 버튼`을 누르면 안 된다. 왜냐하면, 지금은 아무것도 실행할 수 없기 때문이다. 

## 5단계 : 웹앱 설정 

1. Web 대시보드 > `Code : ` 영역 > WSGI configuration file의 링크 클릭
2. 해당 링크를 클릭하면 새로 만든 flaks 웹앱의 설정 파일이 파이썬애니웨어의 웹 기반 텍스트 편집기로 열린다.  
   a. 5장 끝부분에서 파이썬애니웨어는 `app.run()`을 실행하기 전에 우리 웹앱의 코드를 import한다고 했다.
   b. 이 동작을 지원하는 파일이 바로 이 설정파일이다.
   c. `from vsearch4web import app as application` 으로 수정하고 Save 클릭 

## 6단계 : 클라우드 기반 웹앱 실행 

1. Web 탭 > `Reload ~~` 버튼 클릭 
