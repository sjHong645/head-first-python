## `comprehension`에 대해서 다룰 거다. 

### csv 파일을 읽어오는 여러 가지 방법

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

### 요구조건
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

- 가공하지 않은 데이터에서 공백을 제거한 다음 나누자. 

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

- 추가 요구사항
1. 비행시간을 24시간 형식 => AM / PM 형식으로 변경
2. 목적지 정보를 맨 앞글자만 대문자로 변경 
3. 기존에 가공되지 않은 데이터는 그대로 유지할 것. 
    - 데이터 변환은 복사본에 적용해야 한다. 

이는 같은 데이터를 `다르게 표현`하는 것이라는 걸 알 수 있다. 

그리고 현재는 하나의 행에 `하나의 비행시간 & 목적지 정보`를 포함하고 있다. 
이 구조를 `key는 목적지 정보`, `value는 비행시간 리스트`를 갖는 딕셔너리로 바꾸려고 한다. 

ex) 아래와 같이 변경하고 싶다 
```
{
    'Freeport' : ['09:35AM', '05:00PM'], 
    ...
}
```

