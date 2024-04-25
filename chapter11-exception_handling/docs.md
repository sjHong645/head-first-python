이번 장에서는 어떤 예외 상황이 발생할 수 있고 문제가 발생하기 전에 무엇을 해야 할 지 배운다. 

## vsearch4web.py 에서 문제 살펴보기

- 파일 위치 : chapter9-context_manager/vsearch4web.py

1. 아래와 같이 설정한 DB와의 연결을 실패하는 경우 
```
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }
```

DB를 사용할 수 있는지 여부는 항상 달라질 수 있다. 
위 코드는 DB의 실행이 멈춘 상태를 고려하지 않았기 때문에 그 상태가 도래한 경우 당연히 Error가 발생할 것 이다. 

이때 발생하는 에러는 `InterfaceError`이다. 

2. SQL 인젝션, XSS와 같은 공격에 취약함 
```
 _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
```

SQL 인젝션은 백엔드 DB를 노린 공격이고 XSS는 웹 사이트를 노린 공격이다. 

하지만, 모의로 SQL 인젝션, XSS 공격을 시도한 결과 별 문제가 없었다. 

3. 오래 걸릴 수 있는 작업이 존재함
```
cursor.execute(~~) 부분 
```

백엔드 DB와 통신해서 실행해야 하는 부분인데 연결이 늦는다면 어떤 상황이 발생할까? 

실제로 코드가 파일, DB, 네트워크 등 외부 리소스와 상호작용하느라 시간이 걸릴 수 있다. 하지만, 이는 우리가 제어할 수 있는 영역은 아니다. 이러한 상황이 발생할 수 있다는 것을 알고 있어야 한다. 

4. 호출에 실패할 수 있음 
```
log_request(request, results)
```

항상 함수가 성공적으로 호출된다는 보장은 없다. 특히 함수가 외부 코드와 상호 동작할 때는 더더욱 그렇다. 

## 확인된 문제 고찰 

지금까지 vsearch4web.py에서 4가지 문제를 발견했다. 각 문제를 확인하면서 다음 단계를 준비하자. 

### 1. DB와의 연결 실패
=> 이 경우 `InterfaceError`가 발생한다. 

Python의 내장 예외 처리 기법을 사용해 이런 종류의 문제를 처리할 수 있다. 

### 2. 웹앱이 공격대상이 될 수 있음 

애플리케이션의 공격 문제는 웹 개발자가 항상 신경써야 하는 문제다. 탄탄한 코드를 구현하는 습관은 항상 지녀야 한다. 

앞선 상황에서는 SQL 인젝션, XSS에 잘 대처한다는 사실을 확인했다. 이는 Jinja2 라이브러리 자체가 잠재적 문제가 있는 문자열을 escaping 하면서 XSS의 공격을 방어할 수 있도록 설계되었기 때문이다. 그래서 웹앱에서 JavaScript 공격을 시도하면 아무런 동작을 하지 않는다.

SQL 인젝션과 관련해서는 DB-API의 파라미터화된 SQL 문자열 덕분에 SQL 인젝션이라는 종류의 공격으로 부터 자유로워졌다. 

[SQL 인젝션 관련 내용](https://en.wikipedia.org/wiki/SQL_injection)
[XSS 관련 내용](https://en.wikipedia.org/wiki/Cross-site_scripting)

### 3. 코드를 실행할 때 오랜 시간이 걸릴 수 있음 

실행이 아예 안되는 건 아니지만 실행하는데 시간이 너무 오래 걸린다면  
사용자 입장에서는 문제가 생긴 것이라고 간주하게 된다. 

때문에 사용자가 기다려야 하는 상황이 발생할 때 어떤 조치를 취해줘야 한다. 

### 4. 함수 호출 실패 

내가 작성한 코드가 예외를 일으킬 수 있다. 이 문제는 1번과 같은 종류의 기법으로 해결할 수 있다. 

[모든 내장 예외 목록](https://docs.python.org/3/library/exceptions.html)

## 내장 예외 처리 방법 

아래 코드는 겉보기에는 아무런 문제가 없다. 
```
with open('myfile.txt') as fh : 
    file_data = fh.read()

print(file_data)
```

하지만, myfile.txt 파일에 접근할 수 없는 상황이라면 아래와 같은 에러가 발생한다.
(파일이 없거나 파일을 읽는데 필요한 권한이 없는 상황 등등)
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
```

`try`를 이용해서 `FileNotFoundError 예외를 처리`해보자. 

try suite 부분에서 `FileNotFoundError 에러`가 발생했을 때  
except suite 부분에서 원하는 작업을 수행할 수 있다. 

```
try : 
    with open('myfile.txt') as fh : 
        file_data = fh.read()
    print(file_data)

except FileNotFoundError : 
    print('The data file is missing')


실행 결과 
The data file is missing
```

하지만, `FileNotFoundError 예외` 말고 다른 에러가 발생할 수도 있다. 

파일을 읽을 권한이 없는 경우 `PermissionError 에러`가 발생할 수 있다. 그래서 아래와 같이 코드를 개선해야 한다. 

```
try : 
    with open('myfile.txt') as fh : 
        file_data = fh.read()
    print(file_data)

except FileNotFoundError : 
    print('The data file is missing')

except PermissionError : 
    print('This is not allowed')
```

하지만, 앞선 2가지 예외 말고도 예상하지 못한 에러가 또 발생할 수 있다. 