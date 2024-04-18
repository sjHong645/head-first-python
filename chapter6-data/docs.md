## 텍스트 파일에 저장하는 방법 

텍스트 파일에 저장하는 내용은 크게 3가지로 나눌 수 있다.

- 파일을 연다.
- 데이터를 처리한다(읽기, 쓰기, 추가하기 등등)
- 파일을 닫는다

### 파일 열기 / 데이터 처리 / 파일 닫기 예제 

```
# todos.txt라는 파일을 연다. 
# 모드는 추가(append) 모드 
>>> todos = open('todos.txt', 'a') 
                                   
# 출력한 내용을 
# 'file' 매개변수를 이용해서 파일 스트림을 지정한다. 
>>> print('Put out the trash.', file = todos)
>>> print('Feed the cat.', file = todos) 

# 파일을 닫는다. 
# close() 를 호출하지 않는다면 데이터가 유실될 수 있다. 
>>> todos.close()
```

### 기존 파일에서 데이터 읽기 

```
>>> tasks = open('todos.txt') # todos.txt 파일을 연다.
                              # 기본 모드는 읽기('r')이다. 

>>> tasks
<_io.TextIOWrapper name='todos.txt' mode='r' encoding='cp949'>

# 아래 결과를 보면
# txt 파일에 있는 각각의 행을 읽어온 걸 확인할 수 있다. 

# 각 줄마다 빈 줄이 하나씩 더 늘어난 이유는
# 파일 자체에 있는 객행문자(\n) + print() 메소드가 마지막에 제공하는 \n이 합쳐져서
# 두 줄 띄어쓰기가 되었기 때문이다. 
>>> for chore in tasks : 
...     print(chore)
... 
Put out the trash.

Feed the cat.

# 파일을 열었다면 반드시 닫아줘야 한다. 
>>> tasks.close()
```

#### 파일 모드 

- 'r' : 읽기 모드 (기본값)
    - 파일이 이미 존재할 때 해당 파일을 읽어온다. 

- 'w' : 쓰기 모드 
    - 파일이 이미 존재한다면 기존 내용을 삭제하고 새로 쓴다.

- 'a' : 추가 모드 
    - 기존 파일의 내용은 유지하면서 파일의 끝 부분에 새로운 데이터를 추가한다. 
    - 기존 파일이 없다면 새로운 파일을 만들어낸다. 

- 'x' : 새로운 파일 쓰기 모드
    - 새로운 파일을 쓴다.
    - 기존에 파일이 이미 존재한다면 파일 열기가 실패한다. 

### with문

- 기존 코드
```
>>> tasks = open('todos.txt') 
>>> for chore in tasks : 
...     print(chore)
>>> tasks.close()
```

- with문 적용
```
with open('todos.txt') as tasks: 
    for chore in tasks : 
        print(chore)
```

`close 호출`을 사용하지 않아도 with문 suite가 끝나면 알아서 close가 호출된다. 

### 웹앱을 통해 로그 파일 출력하기 

[해당 커밋](https://github.com/sjHong645/head-first-python/commit/4d6694419fbf64a5c72307681206223b2ce7d608)에서 코드 작성을 끝내고 프로그램을 실행하면 다음과 같이 화면이 출력된다. 

![image](https://github.com/sjHong645/head-first-python/assets/64796257/dfcba45c-583c-4978-9ad6-956dae546f00)

분명히 
`<Request 'http://localhost:5000/search4' [POST]> {'i', 'o', 'e'}` 가 출력되어야 하는데 `{'i', 'o', 'e'}` 들만 출력된 걸 확인할 수 있다. 

더 정확한 내용은 `페이지 소스 보기`를 통해 문제 상황을 더 확실하게 인지할 수 있다. 

화면에 출력된 결과는 `웹 브라우저가 가공해 렌더링한 결과`라는 점을 잊지 말자. 
즉, `가공된 결과`가 화면에 출력되고 `가공되지 않은 결과`를 페이지 소스를 통해 확인할 수 있다. 

데이터를 감싸는 꺽쇠괄호(`<>`)를 살펴보자. 
브라우저는 기본적으로 꺽쇠괄호(`<>`)를 HTML 태그로 처리한다. 그러나 `<Request>`는 유효한 HTML 태그가 아니므로 이 태그를 무시하고 아무것도 출력하지 않은 것이다. 

그렇다면, 어떻게 해야 우리가 원하는 데이터를 브라우저의 화면을 통해 볼 수 있을까? 

### 데이터 이스케이프

- escaping : 특수한 HTML 문자가 HTML로 해석되지 않고 화면으로 출력될 수 있도록 HTML 특수 문자를 인코딩하는 기법 
    ex. `<` : `&lt;` / `>` : `&gt;`

flaks에서는 Jinja2에서 상속받은 `escape 함수`를 갖고 있다. 
가공되지 않은 데이터를 출력할 때 escape 함수를 사용하면 HTML 특수 문자를 escape한 문자열을 제공한다. 

```
>>> from markupsafe import escape

>>> escape('This is a Request')
Markup('This is a Request')

>>> escape('This is a <Request>') 
Markup('This is a &lt;Request&gt;') # 특수문자을 표현한 문자열에 escape를 사용함 
```

### 로깅되는 내용을 좀 더 유용하게 바꾸기

- 현재까지 상황에서 로깅되는 내용 
```
<Request 'http://localhost:5000/search4' [POST]> {'o', 'i', 'e'}
<Request 'http://localhost:5000/search4' [POST]> {'o', 'i', 'e'}
<Request 'http://localhost:5000/search4' [POST]> {'i', 'o', 'e'}
```

로깅된 결과는 다르지만 로깅된 웹 요청은 모두 동일하다. 

웹 요청을 객체 수준에서 로깅하고 있어서 중요한 내용은 요청 객체 안에 들어있다. 
`dir() 메소드`를 사용해서 메서드와 속성 목록을 로깅하도록 해보자.

`dir() 메소드`를 사용해서 로그 파일을 출력하니 이런 결과가 나온다. 
```
['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cached_json', '_get_file_stream', '_get_stream_for_parsing', '_load_form_data', '_parse_content_type', '_parsed_content_type', 'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes', 'access_control_request_headers', 'access_control_request_method', 'access_route', 'application', 'args', 'authorization', 'base_url', 'blueprint', 'blueprints', 'cache_control', 'close', 'content_encoding', 'content_length', 'content_md5', 'content_type', 'cookies', 'data', 'date', 'dict_storage_class', 'endpoint', 'environ', 'files', 'form', 'form_data_parser_class', 'from_values', 'full_path', 'get_data', 'get_json', 'headers', 'host', 'host_url', 'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since', 'input_stream', 'is_json', 'is_multiprocess', 'is_multithread', 'is_run_once', 'is_secure', 'json', 'json_module', 'list_storage_class', 'make_form_data_parser', 'max_content_length', 'max_form_memory_size', 'max_form_parts', 'max_forwards', 'method', 'mimetype', 'mimetype_params', 'on_json_loading_failed', 'origin', 'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer', 'remote_addr', 'remote_user', 'root_path', 'root_url', 'routing_exception', 'scheme', 'script_root', 'server', 'shallow', 'stream', 'trusted_hosts', 'url', 'url_root', 'url_rule', 'user_agent', 'user_agent_class', 'values', 'view_args', 'want_form_data_parsed'] {'i', 'o', 'e'}
```

이 중에서 수행한 검사 결과는 맨 마지막에 있는 `{'i', 'o', 'e'}`이다. 

로그 결과를 보니 단순히 검사 결과뿐만 아니라 던더, 원더, 메서드와 관련된 모든 속성을 포함한다는 걸 알 수 있다. 

모든 속성들을 다 로깅할 필요는 없고 중요한 3가지 속성만 살펴보자.

- req.form : 웹 앱의 HTML 폼에서 보낸 정보
- req.remote_addr : 웹 브라우저가 실행 중인 IP주소
- req.user_agent : 데이터를 전송한 브라우저 정보 

위 3가지 정보만 출력해서 결과를 보자. 

```
ImmutableMultiDict([('phrase', 'lookinggoodperson'), ('letters', 'aeiou')])
127.0.0.1
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
{'o', 'e', 'i'}
```

### 가공되지 않은 데이터를 읽기 쉬운 형태로 출력하기 

브라우저 창에 출력된 데이터는 가공되지 않은 형태이다. HTML 이스케이핑을 수행했을 뿐 다른 작업은 하지 않았다. 

로깅된 데이터를 보여주는 것도 좋지만 읽기 어렵다면 소용이 없으니 가독성있게 텍스트를 조정하는 작업이 필요하다. 


