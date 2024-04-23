## URL 접근 제한 - Decorator(장식자)를 이용하자

이제 `/page1`, `/page2`, `/page3` URL에 접속을 제한하는 방법을 알아보자. 

서로 다른 URL을 처리하는데 똑같은 함수를 호출하는 건 별로 좋지 않다. 
그래서 `Decorator(장식자)`를 만들어서 사용하는 방법을 생각할 수 있다. 

### 최악의 방법 : 각 URL에 status 함수의 내용 복사/붙여넣기 

서로 다른 URL을 처리할 때 코드 자체를 복사/붙여넣기를 하면서 코드를 관리하는 건 유지보수 측면에서 굉장히 안 좋은 방법이다. 

열심히 복사/붙여넣기를 했는데 인증방식을 변경해야 한다면? 복사/붙여넣기 했던 모든 코드를 하나씩 살펴보면서 코드를 변경해야 하는 지옥이 시작된다. 

### 차선의 방법 : 여러 곳에서 사용할 코드를 함수로 만들어서 호출하기 

함수를 이용하면 유지보수 문제는 발생하지 않는다. 

- check_logged_in : 사용자가 로그인하면 True / 그렇지 않으면 False 반환
```
def check_logged_in() -> bool : 
    if 'logged_in' in session : 
        return True 
    
    return False 
```

- page1 URL에 접근했을 때 실행할 함수
```
@app.route('/page1')
def page1() -> str:

    if not check_logged_in() : 
        return 'Your are NOT logged in'

    return 'This is page 1.'
```

확실히 복사/붙여넣기 방법보다는 더 좋은 방법이다. 
하지만, `/page2`, `/page3` URL에 접근할 때 실행할 함수와 앞으로 추가할 함수에 똑같은 함수 호출 코드와 관련 처리 코드를 추가해야 한다는 문제가 있다. 

종류만 다를 뿐 결국 똑같이 복사/붙여넣기를 한다. 

### 최선의 방법 : Decorator(장식자) 사용하기

1. 사용자의 브라우저가 기존 함수의 코드를 변경하지 않고 
2. 함수의 고유 작업을 방해하지 않으면서 

동작을 바꾸기 위해서 사용할 수 있는 기능이 바로 `Decorator(장식자)`이다. 

전혀 생소한 개념이 아니다. `@app.route('/')` 역시 장식자를 이용한 것이다. 

그러면 장식자를 어떻게 구현할 수 있을까? 다음 4가지 사실을 알아야 한다. 

1. 함수를 구현하는 방법 - 이미 알고 있음 
2. 함수를 함수의 인자로 전달하는 방법 
    - 말 그대로 구현한 함수를 그냥 인자로 전달하면 됨
    - 함수 역시 `객체`이기 때문이다. 
3. 함수에서 함수를 반환하는 방법
    - python은 `중첩 함수(nested function)`를 지원한다.
    - 즉, 함수 안에서 함수를 정의할 수 있다. 
    - 이때, 내부에서 정의한 함수를 반환할 수 있다. 
4. 다양한 개수와 유형의 함수 인자를 처리하는 방법 

3번 예시 코드
```
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper 
```

4번 내용 
- `*`를 이용해서 0개 이상의 인자를 받을 수 있다. 

ex) 
```
# 엄밀히 따지면 *args는 튜플이지만 인자 리스트라고 생각하면 편하다 
# 0개 이상의 인자들을 args 라는 이름의 튜플에 저장해서 전달한다. 
def myfunc(*args) : 
    for a in args : 
        print(a, end = ' ')

    if args : 
        print()

>>> myfunc()
>>> myfunc(10) 
10
>>> myfunc(10, 20, 30, 40, 50)
10 20 30 40 50
>>> myfunc(10, 'two', 30, 'four', 50)
10 two 30 four 50
```

- 함수 호출할 때 `*`를 사용하는 방법 

```
>>> values = [1, 2, 3, 5, 7, 11] 

# 리스트를 인자로 제공했다. 
# 리스트 자체에 몇 개의 값이 있는지 상관없이 1개의 항목으로 처리한다. 
>>> myfunc(values)
[1, 2, 3, 5, 7, 11] 

# 리스트의 항목을 각각의 인자처럼 취급하도록 하려면 리스트를 확장해야 한다.
# 이를 위해서 *를 사용하면 된다. 
# 즉, 1, 2, 3, 5, 7, 11이 각각의 인자로 취급되었기 때문에 아래와 같이 출력된 것이다. 
>>> myfunc(*values) 
1 2 3 5 7 11
```

- `**`를 사용해서 임의의 키워드 인자 처리하기 

`**`에서는 `키워드 인자`를 의미하는 `kwargs`를 사용한다. 명칭은 관습적인 것이라 다른 이름을 써도 상관은 없지만 대부분은 이 이름을 사용한다. 

`**`는 `key와 value의 딕셔너리를 확장한다는 의미`로 생각하면 된다.

```
def myfunc2(**kwargs) : 
    for k, v in kwargs.items() : 
        print(k, v, sep = '->', end = ' ')
    if kwargs : 
        print()

>>> myfunc2(a = 10, b = 20)
a->10 b->20 
>>> myfunc2(a = 10, b = 20, c = 30, d = 40) 
a->10 b->20 c->30 d->40 
```

- 함수 호출할 때 `**`을 사용하는 방법 

chapter9-context_manager/before_context_applied.py 파일에서 해당 내용을 확인할 수 있다. 

```
dbconfig = {
        'host' : 'localhost', 
        'user' : 'root', 
        'password' : 'asi', 
        'database' : 'vsearchlogDB', 
        'port' : 3308
    }
    
conn = mysql.connector.connect(**dbconfig)

똑같은 동작 

conn = mysql.connector.connect('host' = 'localhost', 
                               'user' = 'vsearch', 
                               'password' = 'asi', 
                               'database' = 'vsearchlogDB', 
                               'port' = 3308)
```

