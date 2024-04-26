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

#### INSERT와 SELECT의 차이점 

- INSERT : 블록을 하는 코드가 필요 없음
- SELECT : DB에서 데이터를 반환할 때까지 블록해야 함 
    - 블록하지 않는다면 이후의 코드 실행에서 사용할 데이터가 없으니까 문제 발생 

때문에, `view_the_log`의 `cursor.execute()`는 데이터를 가져올 때 까지 블록해야 함. 

`log_request`는 반환값이나 데이터가 없다. 호출 코드는 이 작업이 언제 일어나는지에 크게 관심이 없다. 

사용자는 웹앱에 새로운 검색을 실행했을 때 사용자의 요청정보가 DB에 기록되어야 하는지에 대해서는 신경쓰지 않는다. 

그렇다면, `log_request`를 호출할 때는 굳이 사용자를 기다리지 않도록 해야 한다. 이를 위해서 웹앱의 메인 함수와 독립적이면서 순차적으로 로깅 작업을 할 수 있도록 다른 프로세스를 이용할 것 이다. 

### 한 번에 1가지 이상의 일 처리하기 

`log_request` 함수를 웹앱의 메인 함수와 독립적으로 실행할 계획이다. 
그러기 위해서는 `log_request`를 동시에 실행하도록 웹앱의 코드를 바꿔야 한다. 

웹앱과 사용자는 `log_request`가 즉시 처리되든, 시간이 얼마나 걸리든 상관하지 않는다. 코드가 순차적으로 실행되기만 하면 된다. 

#### 동시 실행 코드 

[Python의 표준 동시 실행 선택사항](https://docs.python.org/3/library/concurrency.html)

다양한 서드파티 모듈과 표준 라이브러리에서 동시 실행에 필요한 기능을 제공한다.

그 중에서 웹앱을 실행하는 OS 수준의 추상화된 스레딩 구현을 제공하는 threading 라이브러리가 대표적이다. 

```
from threading import Thread
```

- 예제

3개의 숫자 인자를 갖는 `execute_slowly`라는 함수가 있다고 하자. 
이 함수가 실행을 완료하는데 30초 정도 걸린다고 하면 호출 코드는 30초를 꼼짝없이 기다려야 한다. 

```
execute_slowly(glacial, plodding, leaden) # execute_slowly 함수를 사용하는 방법 

# Thread를 이용하는 방법 

from threading import Thread

# target : 호출할 함수
# args : 호출할 함수에 전달할 인자 
# 아직 Thread 객체를 t라는 변수에 할당했을 뿐 실행하지는 않았음 
t = Thread(target = execute_slowly, args = (glacial, plodding, leaden))

# 시작
# 아래 코드를 호출하고 나면 블록되지 않고 그 아래에 있는 코드를 계속 실행한다. 
# 시간이 30초가 걸려도 이후에 실행되는 코드에는 아무런 영향을 미치지 않는다. 
t.start() 
```

- do_search() 메소드에 적용하기

```
log_request(request, results) # 여기서 log_request를 sleep(15)를 이용해서 
                              # 일부러 15초 지연시켰다. 

대신에 

t = Thread(target = log_request, args = (request, results))
t.start()
```

하지만, 이렇게만 수정하면 오류가 발생한다. 왜 그런걸까? 

`do_search()`가 끝나면 인터프리터는 함수(및 컨텍스트)와 관련된 모든 데이터를 회수한다. 

즉, 함수 내에서 선언한 지역변수 phrase, letters, title, results가 만료된다. 
15초가 지난 후에는 이미 do_search 함수가 끝났기 때문에 request, results 변수를 사용하지 못하기 때문에 오류가 발생한다. 

- 원인을 찾았으니 해결하자 

정리하면 
1. log_request 함수를 스레드에서 실행할 때는 인자 데이터를 사용할 수 없게 되었다. 
2. do_search 함수가 끝나면서 인터프리터가 지역변수가 사용한 메모리를 회수했기 때문이다. 
3. request 객체 역시 만료되어서 log_request에서 사용할 수 없다. 

이 문제는 `flask의 장식자`를 이용해서 해결할 수 있다. 

`copy_current_request_context 장식자`를 이용하면 함수를 호출했을 때 활성 상태인 HTTP 요청을 나중에 thread에서 함수가 호출되는 순간까지 유지시켜 준다. 

단, 장식된 함수는 반드시 호출하는 함수의 내부 함수로 정의되어야 한다.

- 단계
1. log_request 함수를 do_search 함수 내부에 중첩
2. log_request 함수를 `@copy_current_request_context`로 장식
3. 재확인 

