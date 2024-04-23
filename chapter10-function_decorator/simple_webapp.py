from flask import Flask, session

from checker import check_logged_in

app = Flask(__name__)

# 모든 URL이 공개되어 있어서 누구나 브라우저로 접근할 수 있다. 
@app.route('/')
def hello():
    return 'Hello from the simple webapp.'


@app.route('/page1')
@check_logged_in # page1, page2, page3에 장식자를 적용함 
def page1():
    return 'This is page 1.'


@app.route('/page2')
@check_logged_in
def page2():
    return 'This is page 2.'


@app.route('/page3')
@check_logged_in
def page3():
    return 'This is page 3.'

# 여기에 `/page1`, `/page2`, `/page3` URL에 접근할 때 로그인한 사용자에게만 제공하려고 한다. 
# 이 기술을 flask의 session을 이용해서 구현할 것 이다. 
@app.route('/login')
def do_login() -> str : 
    session['logged_in'] = True
    return 'You are now logged in~!'

app.secret_key = 'YouWillNeverGuessMySecretKey'

# 로그아웃과 상태 확인 기능 구현 
@app.route('/logout')
def do_logout() -> str : 
    session.pop('logged_in')
    return 'You are no logged out~!'

@app.route('/status')
def check_status() -> str : 
    
    # logged_in 이라는 key값이 session에 있는지 확인했다.
    
    # 굳이 false라는 값을 저장해서 key값이 있는지 판별하지 않더라도 
    # 딕셔너리에 key값이 존재하는지 여부만으로 충분히 로그인 여부를 판단할 수 있기 때문에
    # false라는 값을 가지고 판단하지 않은 것이다. 
    
    # logged_in 키 값이 존재하면 로그인 상태인 거 확인
    # logged_in 키 값이 없다면 로그아웃 상태인 거 확인 
    if 'logged_in' in session :     
        return 'You are currently logged in~~'
    
    return 'You are NOT logged in!!'
    

if __name__ == '__main__':
    app.run(debug=True)
