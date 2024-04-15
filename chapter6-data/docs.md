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