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
