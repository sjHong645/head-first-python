## 집합 컴프리헨션 (setcomp)

집합 컴프리헨션을 만들고 사용할 수는 있지만 그런 예시를 실제로 보긴 어렵다. 

리스트 컴프리헨션과 비슷한 문법으로 이뤄진 한 행의 코드로 새로운 집합을 만들 수 있다. 

- 예시
```
>>> vowels = {'a', 'e', 'i', 'o', 'u'}
>>> message = "Don't forget to pack your towel." 
>>> found = set()
>>> for v in vowels : 
...     if v in message : 
...             found.add(v)
...
>>> found
{'u', 'o', 'a', 'e'}

# 집합 컴프리헨션 적용 
found2 = {v for v in vowels if v in message}
```

- 리스트 컴프리헨션과의 차이점 : 대괄호(`[]`) 대신에 중괄호(`{}`)를 사용했다. 
- 딕셔너리 컴프리헨션과의 차이점 : `key:value` 형태로 값을 저장하지 않는다. 

## 튜플 컴프리헨션? 그런 건 없다. 

`리스트 컴프리헨션`은 대괄호(`[]`)로 감싸고 `딕셔너리 컴프리헨션`은 중괄호(`{}`)로 감싼다. 

그런데 소괄호(`()`) 사이에서 코드를 사용하는 경우도 종종 있다. 이를 `튜플 컴프리헨션`이라고 생각할 수 있지만 제목에서 말했듯 `그런 건 없다`. 그럼 정체가 뭘까? 

### 튜플 컴프리헨션이 존재할 수 없는 이유 

`튜플`이란 바꿀 수 없는 자료구조다. 
때문에 아래 예시처럼 기존 튜플에 데이터를 추가하는 동작을 실행할 수 없다. 그러니 당연히 `튜플 컴프리헨션`이라는 건 존재할 수가 없다. 

- 예시 
```
>>> names = () 
>>> for n in ('John', 'Paul') : 
...     names.append(n)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'tuple' object has no attribute 'append'
```

### 그럼 이건 뭐지

```
# 중괄호로 감쌌음
# 리스트 컴프리헨션이 적용되었군 
>>> for i in [x*3 for x in [1, 2, 3, 4, 5]] : 
...     print(i)
...
3
6
9
12
15

# 소괄호로 감쌌음 
# 튜플 컴프리헨션은 없는데 이건 뭐지? 
>>> for i in (x*3 for x in [1, 2, 3, 4, 5]) :  
...     print(i)
...
3
6
9
12
15
```

### 생성기(generator)라고 한다. 

`리스트 컴프리헨션을 사용`할 수 있다면 어디든 `생성기를 사용`할 수 있다. 

앞서 본 예시는 출력결과는 같지만 동작방식이 많이 다르다. 

어떻게 다른지 예시를 보면서 살펴보겠다. 

- 리스트 컴프리헨션을 사용한 경우
```
>>> import requests
>>> urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')
>>>  
>>> for reap in [requests.get(url) for url in urls] : 
...     print(len(reap.content), '->', reap.status_code, '->', reap.url)
... 

# 이 결과가 나올 때 까지 시간이 약간 걸렸다. 
# 그리고 데이터가 한 번에 나타난 걸 확인할 수 있는데 
# 이는 for루프 시작 전에 리스트 컴프가 urls 튜플의 각 URL을 모두 처리했기 때문이다. 

# 그래서 결과가 출력될 때까지 기다려야 한다. 
82063 -> 200 -> https://www.oreilly.com/
82063 -> 200 -> https://www.oreilly.com/
2344 -> 400 -> https://twitter.com/
```

- 생성기를 사용한 경우 

```
>>> for reap in (requests.get(url) for url in urls) :  
...     print(len(reap.content), '->', reap.status_code, '->', reap.url)
...

# 결과가 하나씩 하나씩 출력된 걸 확인할 수 있다. 
# 리스트컴프와 달리 데이터가 준비된대로 데이터를 제공한 걸 확인할 수 있다. 

# 생성기를 사용함으로써 for 루프의 반응성이 좋아졌다. 
82063 -> 200 -> https://www.oreilly.com/
82063 -> 200 -> https://www.oreilly.com/
2344 -> 400 -> https://twitter.com/
```

### 생성기를 함수로 캡슐화하는 방법 

앞서 생성기를 사용한 부분을 함수로 정의하자. 

```
def gen_from_urls(urls: tuple) -> tuple: 
    for reap in (requests.get(url) for url in urls) :  
        return len(reap.content), reap.status_code, reap.url
```

그런데 `return`을 사용하면 for문을 통해 처리한 값을 하나 출력하는 순간 함수가 종료된다. 
`gen_from_urls` 함수는 for문의 일부로 사용되고 호출할 때 마다 다른 튜플 결과를 제공해서 위와 같이 함수를 종료하면 안 된다. 

- `yield`를 사용하자. 
    
`yield`란 
1. 생성자 함수를 만들 수 있또록 Python에 추가된 키워드
2. yield를 사용하면 함수는 반복자가 호출할 수 있는 생성기 함수로 변환된다. 

```
def gen_from_urls(urls: tuple) -> tuple: 
    for reap in (requests.get(url) for url in urls) :  
        yield len(reap.content), reap.status_code, reap.url
```

