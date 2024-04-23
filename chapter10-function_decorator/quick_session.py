# session을 import함으로써 웹앱이 상태를 저장할 수 있는 기능을 추가함
# 브라우저의 고유 쿠키값을 key로 사용해서 웹앱의 각 사용자별로 고유의 값을 저장할 수 있다. 
from flask import Flask, session

app = Flask(__name__)

# 세션을 사용하기 위해 필요한 비밀키 
# 비밀키를 이용해서 쿠키를 암호화하고 외부 사용자로부터 정보를 보호한다.
app.secret_key = 'YouWillNeverGuess'

# Python의 dictionary를 사용하듯이 session을 코드에서 사용할 수 있다. 


@app.route('/setuser/<user>')
def setuser(user : str) -> str : 
    session['user'] = user # session에 상태 저장 
    return 'User values set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str : 
    
    # session에 있는 상태값에 접근 
    return 'User values is currently set to: ' + session['user']

if __name__ == '__main__' : 
    app.run(debug=True)