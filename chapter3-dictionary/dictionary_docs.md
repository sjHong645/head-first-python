# 순서가 없는 key-value 쌍의 집합 

## 검색속도가 빠른 딕셔너리 

- `key값`과 매핑된 `value`를 추출하는 dictionary 

- 많은 데이터에서 인터프리터가 key와 매핑된 value를 `얼마나 빨리 반환할 수 있느냐`가 관건 
    - 최적화된 해싱 알고리즘 덕분에 해당 작업을 아주 빠르게 수행됨 
    - 파이썬의 딕셔너리는 크기를 조절할 수 있는 해시 테이블로 구성되어 있고 최적화되어 있음

## 딕셔너리를 이용해서 for문을 사용할 때 
```
for k in some_dict : 
    print(k) // k값은 딕셔너리의 키 값만 출력됨
    print(some_dict[k]) // 키 값에 대한 value를 알고 싶다면 직접 접근해야 함 
```

- key값이 정렬된 딕셔너리를 얻고 싶다면? `sorted() 메소드`를 써라
```
for k in sorted(some_dict) : 
    print(k) // k값은 딕셔너리의 키 값만 출력됨
    print(some_dict[k]) // 키 값에 대한 value를 알고 싶다면 직접 접근해야 함 
```

- key값과 value값을 모두 접근할 수 있는 방법
```
for k, v in some_dict.items() : 
    print(k) // k값은 딕셔너리의 key 값만 출력됨
    print(v) // v값은 딕셔너리의 value 값만 출력됨
```

## 딕셔너리의 key는 반드시 초기화 되어야 한다.
- 오류가 발생하는 상황 
```
vowels = ['a', 'e', 'i', 'o', 'u']
word = 'hitchhiker'

found = {}

for letter in word : 
    if letter in vowels : 
        found[letter] += 1 # 여기서 KeyError 오류 발생!
                           # 딕셔너리의 key값을 초기화하지 않았기 때문

```

즉, 아래와 같이 초기화 해줘야 오류가 발생하지 않는다.
```
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
```

하지만, 검색하고 싶은 문자가 많아진다면 위와 같이 일일이 초기화해주는 건 너무 비효율적이다. 그리고 일일이 설정하다보면 동일한 key값을 굳이 여러 번 초기화할 수도 있다. 

그러면 어떻게 초기화해주면 될까? 아래 코드에 추가된 if문을 보자. 
```
vowels = ['a', 'e', 'i', 'o', 'u']
word = 'hitchhiker'

found = {}

for letter in word : 
    if letter in vowels : 

        // letter라는 값이
        // found라는 딕셔너리의 key값에 이미 존재하는지 판단한다.
        // 없다면 초기화한다. 
        if letter not in found : 
            found[letter] = 0

        found[letter] += 1 

```

- setdefault 메서드 사용 

```
vowels = ['a', 'e', 'i', 'o', 'u']
word = 'hitchhiker'

found = {}

for letter in word : 
    if letter in vowels : 

        found.setdefault(letter, 0) // 방금 위에서 사용한 if문과 동일한 기능 수행
                                    // letter라는 key값이 이미 존재하면 아무 동작을 하지 않고 
                                    // letter라는 key값이 존재하지 않으면 초기화를 진행하는데 value는 0으로 초기화 

        found[letter] += 1 

```

