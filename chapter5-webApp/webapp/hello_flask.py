# 모듈이름 flask
# flask 모듈에서 사용할 Flask 클래스 
from flask import Flask
from vsearch import search4letters

# __name__ : 현재 활성 모듈의 이름
# 즉, Flask 클래스는 새로운 Flask 객체를 만들 때 현재 버전의 __name__을 인자로 받아야 함 
app = Flask(__name__)

# @라는 장식자(decorator) 등장
# 함수 decorator는 함수 코드를 바꾸지 않고 함수의 동작을 조절할 수 있다. 
# 주로 함수에 decorator를 붙이는 일이 많아서 `함수 decorator`라고 함 

# URL로 /가 왔을 때 hello() 함수가 동작하도록 함
@app.route('/')
def hello() -> str : 
    return 'Hello world from Flask!!'

@app.route('/search4')
def do_search() : 
    
    # 결과를 반환할 때 str 자료형이여야 함. 
    # set 그 자체는 반환이 안됨
    return str(search4letters('eiru,', 'life, the universe, and everything'))

# 웹앱 실행
# 여기서 포트번호 지정할 수 있는데 특별한 이유가 없다면 그대로 사용하는 게 편하지
app.run()