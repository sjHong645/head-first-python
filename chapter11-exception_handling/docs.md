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

2. SQL 인젝션, XSS와 같은 공격에 취약함 
```
 _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
```

SQL 인젝션은 백엔드 DB를 노린 공격이고 XSS는 웹 사이트를 노린 공격이다. 
이러한 악의적인 공격이 발생할 수도 있는데 이에 대한 대비가 되어있지는 않다.

3. 오래 걸릴 수 있는 작업이 존재함
```
cursor.execute(~~) 부분 
```

백엔드 DB와 통신해서 실행해야 하는 부분인데 연결이 늦는다면 어떤 상황이 발생할까? 

실제로 코드가 파일, DB, 네트워크 등 외부 리소스와 상호작용하느라 시간이 걸릴 수 있다. 하지만, 이는 우리가 제어할 수 있는 영역은 아니다. 



4. 호출에 실패할 수 있음 
```
log_request(request, results)
```