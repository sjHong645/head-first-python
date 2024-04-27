# `comprehension`에 대해서 다룰 거다. 

## csv 파일을 읽어오는 여러 가지 방법

- 파일 자체를 그냥 읽어오기 
```
>>> import os
>>> os.chdir('./chapter12_advanced_loop') 
>>> with open('buzzers.csv') as raw_data : 
...     print(raw_data.read())
... 
TIME,DESTINATION
09:35,FREEPORT
17:00,FREEPORT
09:55,WEST END
19:00,WEST END
10:45,TREASURE CAY
12:00,TREASURE CAY
11:45,ROCK SOUND
17:55,ROCK SOUND
```

- 파일을 리스트로 읽어오기 
```
>>> import csv
>>> with open('buzzers.csv') as data : 
...     for line in csv.reader(data) : 
...             print(line) 
... 
['TIME', 'DESTINATION']  
['09:35', 'FREEPORT']    
['17:00', 'FREEPORT']    
['09:55', 'WEST END']    
['19:00', 'WEST END']    
['10:45', 'TREASURE CAY']
['12:00', 'TREASURE CAY']
['11:45', 'ROCK SOUND']
['17:55', 'ROCK SOUND']
```

- 파일을 dictionary로 읽어오기 

```
>>> with open('buzzers.csv') as data : 
...     for line in csv.DictReader(data) :  
...             print(line) 
... 
{'TIME': '09:35', 'DESTINATION': 'FREEPORT'}
{'TIME': '17:00', 'DESTINATION': 'FREEPORT'}
{'TIME': '09:55', 'DESTINATION': 'WEST END'}
{'TIME': '19:00', 'DESTINATION': 'WEST END'}
{'TIME': '10:45', 'DESTINATION': 'TREASURE CAY'}
{'TIME': '12:00', 'DESTINATION': 'TREASURE CAY'}
{'TIME': '11:45', 'DESTINATION': 'ROCK SOUND'}
{'TIME': '17:55', 'DESTINATION': 'ROCK SOUND'}
```

# 요구조건
하지만, 받고 싶은 데이터의 형태는 따로 있다. 
csv에 있는 그대로 {'시간' : '장소', '시간' : '장소', '시간' : '장소', ...}
형태로 데이터를 변경해달라고 한다.

그러면 다음과 같이 코드를 작성할 수 있다.

```
>>> with open('buzzers.csv') as data : 
...     ignore = data.readline()
...     flights = {}
...     for line in data :
...             k, v = line.split(',')
...             flights[k] = v
...
>>> flights
{'09:35': 'FREEPORT\n', '17:00': 'FREEPORT\n', '09:55': 'WEST END\n', '19:00': 'WEST END\n', '10:45': 'TREASURE CAY\n', '12:00': 'TREASURE CAY\n', '11:45': 'ROCK SOUND\n', '17:55': 'ROCK SOUND\n'}
>>>
>>> import pprint
>>> pprint.pprint(flights)
{'09:35': 'FREEPORT\n',
 '09:55': 'WEST END\n',
 '10:45': 'TREASURE CAY\n',
 '11:45': 'ROCK SOUND\n',
 '12:00': 'TREASURE CAY\n',
 '17:00': 'FREEPORT\n',
 '17:55': 'ROCK SOUND\n',
 '19:00': 'WEST END\n'}
```

## 가공하지 않은 데이터에서 공백을 제거한 다음 나누자. 

```
>>> with open('buzzers.csv') as data : 
...     ignore = data.readline()
...     flights = {}
...     for line in data :
...             k, v = line.strip().split(',') # 이 부분을 변경
                                               # 공백을 제거한 후에 분리했음
...             flights[k] = v
>>> pprint.pprint(flights)
{'09:35': 'FREEPORT',
 '09:55': 'WEST END',
 '10:45': 'TREASURE CAY',
 '11:45': 'ROCK SOUND',
 '12:00': 'TREASURE CAY',
 '17:00': 'FREEPORT',
 '17:55': 'ROCK SOUND',
 '19:00': 'WEST END'}
```

## 추가 요구사항
1. 비행시간을 24시간 형식 => AM / PM 형식으로 변경
2. 목적지 정보를 맨 앞글자만 대문자로 변경 
3. 기존에 가공되지 않은 데이터는 그대로 유지할 것. 
    - 데이터 변환은 복사본에 적용해야 한다. 

요구 사항을 해결하기 위해서 코드를 작성했다. 이때, 동일한 패턴이 적용된 부분을 확인할 수 있다. 

1. for문을 시작하기 전에 새로운 빈 자료구조를 만들었다. 
2. for문의 각 suite는 `새로운 자료구조`에 `기존에 처리한 데이터를 추가`하는 코드를 담고 있다. 
```
with open('buzzers.csv') as data : 
        ignore = data.readline()

        # 이 부분
        flights = {}
        for line in data :
                k, v = line.strip().split(',')
                flights[k] = v
                
pprint.pprint(flights)
print()

for key in flights : 
    
    ampm = convert2ampm(key)
    
    # 이 부분 
    flights2 = {}
    for k, v in flights.items() : 
        flights2[convert2ampm(k)] = v.title()
        
pprint.pprint(flights2)
```

### 리스트 컴프리헨션 

딕셔너리 뿐만 아니라 `리스트`에서도 이러한 패턴이 있다는 사실을 알 수 있다. 

- flights 딕셔너리에서 `key(비행시간)`과 `value(목적지)`를 리스트로 추출한 다음 프로그래밍 패턴을 이용해 새로운 리스트로 변환하는 코드 
```
flight_times = []
for ft in flights.keys() : 
    flight_times.append(convert2ampm(ft))

print(flight_times)
['09:35AM', '05:00PM', '09:55AM', '07:00PM', '10:45AM', '12:00PM', '11:45AM', '05:55PM']       

destinations = []
for dest in flights.values() : 
    destinations.append(dest.title())

print(destinations)
['Freeport', 'Freeport', 'West End', 'West End', 'Treasure Cay', 'Treasure Cay', 'Rock Sound', 'Rock Sound']
```

Python에서는 이러한 일련의 작업을 `Comprehension`이라고 한다. `Comprehension`을 만드는 과정을 살펴보자. 

- Comprehension 적용

아래 코드를 컴프리헨션 기능을 이용해서 1줄로 줄일 수 있다. 
```
destinations = []
for dest in flights.values() : 
    destinations.append(dest.title())
```

1. 새로운 빈 리스트를 만든다.
```
more_dests = []
```

2. for문으로 flights의 기존 데이터를 어떻게 처리할지 지정한 다음 대괄호 안에 추가
```
more_dests = [for dest in flights.values()] # flights.values()의 각각의 값을
                                            # dest에 할당하면서 반복 
```

3. dest에 저장된 데이터를 원하는 형태로 변환. 
    - 여기서는 맨 앞에만 대문자 나머지는 소문자로 변경해서 리스트에 저장하고 싶음

```
more_dests = [dest.title() for dest in flights.values()]
```

(p.532 그림 추가)

- 아래 코드도 마찬가지
```
flight_times = []
for ft in flights.keys() : 
    flight_times.append(convert2ampm(ft))

# 컴프리헨션 적용
fts2 = [convert2ampm(ft) for ft in flights.keys()]
```

#### 리스트 컴프리헨션을 배워야 하는 2가지 이유

1. 코드양이 적고 python 인터프리터가 실행할 수 있또록 최적화되어 있어서 속도가 빠르다. 
    - 같은 동작을 하는 for문보다 속도가 빠르다. 

2. for문을 사용할 수 없는 곳에 컴프리헨션을 사용할 수 있다. 
    - 할당 연산자의 오른쪽에 컴프리헨션이 등장했는데 이는 for문으로 구현할 수 없는 부분이다. 

### 딕셔너리 컴프리헨션 (dictcomp)

- 아래 코드는 앞서 반복되었던 2가지 부분 중 하나였다.
```
flights2 = {}
for k, v in flights.items() : 
    flights2[convert2ampm(k)] = v.title()
```

1. 새로운 빈 딕셔너리 생성
```
more_flights = {}
```

2. for문으로 기존 데이터를 어떻게 반복할 지 지정
```
more_flights = {for k, v in flights.items()} # flights.items()의 각각의 값을
                                             # k, v에 할당하면서 반복 
```

3. k, v에 저장된 데이터를 원하는 형태로 변환 
```
more_flights = {convert2ampm(k) : v.title() for k, v in flights.items()}
```

- 조건문 적용 

v의 값이 'FREEPORT'인 데이터만 저장하고 싶음
```
more_flights = {convert2ampm(k) : v.title() for k, v in flights.items() if v == 'FREEPORT'}
```

## 추가 요구사항 

기존 value에 위치한 목적지 주소를 key값으로 변경하고 싶음

- 고유한 목적지 정보를 만들기 
```
dests = set(fts.values())
```

- West End 비행시간만 따로 추출하기
```
wests = []
for k, v in fts.items() : 
    if v == 'West End' : 
        wests.append(k)

# 리스트 컴프리헨션 적용
wests2 = [k for k, v in fts.items() if v == 'West End']
```

위 두 가지를 접목해서 모든 목적지의 비행시간을 추출하자 

```
for dest in set(fts.values()) : 
    print(dest, '->', [k for k, v in fts.items() if v == dest])

# 딕셔너리 컴프리헨션 적용
when = {} 
for dest in set(fts.values()) : 
    when[dest] = [k for k, v in fts.items() if v == dest]

# 하지만, 위 코드 역시 컴프리헨션을 적용할 수 있을 것 같다. 
# 딕셔너리의 value에 리스트 컴프리헨션을 적용했을 뿐 
# 크게 보면 결국 딕셔너리 컴프리헨션이기 때문이다. 

when2 = {dest : [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
```

물론 반드시 컴프리헨션을 사용해야 된다는 건 아니다. for문이 좋다면 for문을 쓰고 컴프리헨션이 좋다면 컴프리헨션을 써도 상관없다. 

## 질문 

1. 표준루프를 줄이면 컴프리헨션이 된다는 건지? 
A : 그렇다. 구체적으로 for문을 줄인거다. 표준 for문과 대응하는 컴프리헨션은 같은 작업을 수행한다. 하지만, 보통 컴프리헨션이 for문보다 빠르게 동작한다. 

2. 리스트 컴프리헨션을 사용해야 되는 건 어떻게 알 수 있는지 
A : 정해진 법칙은 없다. 보통 기존 리스트를 이용해 새 리스트를 만든다면 루프 코드를 자세히 살펴보고 컴프리헨션으로 바꿀 수 있는지 살펴보자. 새 리스트를 한 번 사용하고 버리는 상황이라면 내장된 리스트 컴프리헨션이 더 좋은 방법일 수 있다. 

3. 컴프리헨션을 꼭 사용해야 하는 건지? 
A : 사용하지 않을 수 있다. 하지만, 이미 많은 python 프로그래머들이 컴프리헨션을 사용하고 있다. 막상 익숙해지면 굉장히 편한 문법이기에 꼭 익숙해지길 바란다. 