chapter11에서 아직 해결하지 못한 문제가 있다. 

어떤 작업을 실행하는데 굉장히 오래 걸리는 경우를 해결하지 못했다. 

어떤 작업을 하는데 시간이 오래 걸리면 어떤 일이 일어나는지에 대한 한 가지 해결책을 찾아보도록 하자.

웹앱의 작동과 관련해서는 `쓰기 작업을 대기`하는 것과 `읽기 작업을 대기`하는 건 다르다. 

`log_request`와 `view_the_log`에서 SQL 질의를 어떻게 이용하는지 살펴보자.

### 각 메소드에서 SQL 질의를 이용하는 방법 

- log_request 
```
def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""

        # 이 부분에서 웹앱이 DB에서의 작업을 완료하는 동안 '블록'(대기)한다. 
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))
```

- view_the_log
```
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    
    try : 
        with UseDatabase(app.config['dbconfig']) as cursor:
 
            _SQL = """select phrase, letters, ip, browser_string, results
                    from log"""

            # 이 부분에서 DB에서의 작업이 완료될 때까지 '블록(대기)'한다. 
            cursor.execute(_SQL)
            contents = cursor.fetchall()
            
```

두 함수 모두에서 `블록`이 되는 부분을 확인했다. 

- log_request : cursor.execute()를 마지막에 호출
- view_the_log : cursor.execute()를 나머지 함수 코드에서 호출 

이러한 함수의 특징이 어떤 차이점을 가져오는지 살펴보자. 

