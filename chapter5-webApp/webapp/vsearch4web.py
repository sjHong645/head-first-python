from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

# GET이 기본값으로 지정되어 있는데 
# 덧붙여진 데이터를 가진 요청을 처리하도록 POST 메소드만 허용했음

# GET, POST를 둘 다 허용하고 싶다면 
# methods=['GET', 'POST']라고 설정해주면 됨
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results) # 해당 메소드를 호출함으로써 
                                  # requests, results를 vsearch.log 파일에 작성함 

    # 요청으로 받은 데이터를 사용하도록 
    # 각각의 데이터를 매개변수를 통해 전달함.
    # 전달한 내용을 results.html 파일에 전달했음 

    # render_template 메소드를 사용함으로써
    # html 파일로 결과 화면을 출력할 수 있음 
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,) # 마지막 컴마를 사용하는 건 선택사항
                                                 # 문법적으로도 올바른 표현임 
# / url 또는 /entry url이 할당된 상태
# 요청이 올 때 url을 비교해서 일치하는 url을 발견했을 때 
# 해당 함수를 실행하도록 함  
@app.route('/') 
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')
    

def log_request(req : 'flask_request', res : str) -> None : 
    
    # 매개변수로 전달받은 req, res를 
    # vsearch.log 라는 파일에 작성하겠다는 의미 
    with open('vsearch.log', 'a') as vsearch_log : 
        
        print(req, res, file = vsearch_log)
        
        

if __name__ == '__main__':

    # 원래는 코드를 수정하고 나면 웹앱을 중지하고 재시작해야 하는데
    # 지금과 같이 코드를 계속해서 수정해야 하는 상황이라면
    # 디버깅 모드를 수행할 수 있도록 설정할 수 있음 

    # 변경된 코드가 저장되고 나면 자동으로 웹앱을 재시작함 

    # 던더 네임 던더 메인을 사용해서 
    # 해당 파이썬 코드를 로컬PC에서 직접 실행했을 때만
    # app.run() 메소드를 사용하도록 설정했음
    app.run(debug=True)

