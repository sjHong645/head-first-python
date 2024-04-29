# 다루지 않은 인기항목 

## 객체 지향과 관련된 내용 

`Python`은 `객체`를 잘 활용한다. 이 말은 우리가 예상한대로 프로그램이 잘 동작한다는 것을 의미한다.  
하지만, 모든 것이 객체라는 말이 모든 것이 클래스에 속해야 함을 의미하지는 않는다. 

이 책에서는 처음부터 클래스를 설명하지 않았다.  
`컨텍스트 관리자`를 만들어야 할 때 컨텍스트 관리자를 만드는 데 필요한 클래스 관련 지식을 배웠을 뿐이다. 

필요한 여러 함수를 구현하기로 했으면 그렇게 하자. 함수형 방식이 더 잘 맞는다면 그 방식으로 접근하자.  
여전히 클래스에 코드를 포함하는 방식에서 헤어나오지 못했다면 Python에서 제공하는 완벽한 객체 지향 프로그래밍 문법을 즐기자. 

클래스를 만드느라 시간을 많이 소비하고 있다면 다음을 확인하자. 

- @staticmethod : 클래스 안에서 정적 함수를 만들 수 있도록 해주는 장식자. self를 첫 번째 인자로 받지 않음
- @classmethod : 클래스 메서드에서 첫 번째 객체를 self가 아닌 cls라는 클래스로 받을 수 있는 기능을 제공하는 장식자
- @property : 메서드를 마치 속성처럼 사용할 수 있도록 재설계해주는 장식자
- `__slots__` : 클래스로 만든 객체의 메모리 효율성을 크게 개선할 수 있는 클래스 지시어. 약간의 융통성이 필요함

[자세한 내용](https://docs.python.org/3/)

## 문자열 포맷 등 

- `+ 연산자`로 문자열을 연결해 메시지 만들기
- `% 문법`으로 고전 형식의 문자열 만들기
- 문자열에서 제공하는 `format 메서드`로 메시지 만들기
- `f-string`을 이용해서 문자열 만들기 

f-string 말고 앞선 3가지 방식에 대한 자세한 문서 [링크](https://peps.python.org/pep-3101)

```
>>> price = 49.99 
>>> tag = 'is a real bargain'
>>> 
>>> msg = 'At ' + str(price) + ', Head First Python ' + tag
>>> msg
'At 49.99, Head First Python is a real bargain'
>>>  
>>> msg = 'At %2.2f, Head First Python %s' % (price, tag)
>>> msg
'At 49.99, Head First Python is a real bargain'
>>>
>>> msg = 'At {}, Head First Python {}'.format(price, tag)
>>> msg
'At 49.99, Head First Python is a real bargain'

>>> msg = f'At {price}, Head First Python {tag}'
>>> msg
'At 49.99, Head First Python is a real bargain'
```

## 정렬하기 

Python은 훌륭한 내장 정렬 기능을 제공한다. 리스트와 같은 일부 자료구조는 데이터를 바로 정렬할 수 있는 `sort 메서드`를 제공한다. 

하지만, Python에서는 `sorted`라는 BIF(Built-In-Function)을 제공한다는 점이 특별하다. 모든 내장 자료구조에서 이 BIF를 사용할 수 있다. 

```
>>> product = {'Book' : 49.99, 
...             'PDF' : 43.99,
...             'Video' : 199.99}
>>> 
>>> for k in product : # 정렬되지 않은 product 딕셔너리 출력 
...     print(k, '->', product[k])
... 
Book -> 49.99
PDF -> 43.99
Video -> 199.99
>>>
>>> 
>>> for k in sorted(product) : # key값을 기준으로 딕셔너리 정렬
...     print(k, '->', product[k])
... 
Book -> 49.99
PDF -> 43.99
Video -> 199.99
>>>
>>> for k in sorted(product, key = product.get) : # value를 기준으로 딕셔너리 정렬 
...     print(k, '->', product[k])
...
PDF -> 43.99
Book -> 49.99
Video -> 199.99
>>> for k in sorted(product, key = product.get, reverse = True) : # value를 기준으로 딕셔너리 역순 정렬 
...     print(k, '->', product[k])
...
Video -> 199.99
Book -> 49.99
PDF -> 43.99
```

[자세한 정렬 기능](https://docs.python.org/3/howto/sorting.html#sortinghowto)

## 표준 라이브러리 기능 

Python 표준 라이브러리는 유용한 기능이 정말 많다.  
시간이 날 때마다 20분 정도 할애해서 표준 라이브러리에서 어떤 기능을 제공하는지 확인해볼 것을 권장한다. 

- [링크](https://docs.python.org/3/library/index.html)
- [Doug Hellmann의 Python 자료](https://pymotw.com/3/)

표준 라이브러리에 어떤 기능이 포함되어 있으며 모든 모듈이 어떤 작업을 수행할 수 있는지 이해하는 건 정말 중요하다. 

### collections 

내장 자료구조인 리스트, 튜플, 딕셔너리, 집합 외에도 import할 수 있는 여러 가지 유용한 자료구조를 많이 제공한다.  
다음은 collections에서 제공하는 일부 자료구조다. 

- OrderedDict : 삽입 순서를 유지하는 딕셔너리
- Counter : 쉽게 셀 수 있는 기능을 제공하는 클래스
- ChainMap : 한 개 이상의 딕셔너리를 합쳐 하나로 나타냄

### itertools 

커스텀 방복을 만드는데 필요한 여러 가지 컬렉션 도구를 제공한다. 그 중에서도 product, permutations, combinations를 자세히 살펴보자. 

### functools 

함수 객체를 인자로 갖는 함수인 고차원 함수 컬렉션을 제공한다.  
많이 사용하는 `partial`을 사용하면 기존 함수의 인자값을 `동결시킬(freeze)` 수 있으며 이후에 새로운 이름을 함수에 붙여 호출할 수 있다. 

## 코드를 병렬로 실행하기 

`11장 3/4`에서는 `스레드`를 이용해 기다리는 문제를 해결했다. 스레드는 프로그램에서 코드를 병렬로 실행하는 방법 중 하나에 불과하다.  
가장 많이 사용되지만 그만큼 남용되는 기능이기도 하다. 

한 번에 하나 이상의 작업을 수행하는 상황에서 사용할 수 있는 다양한 기술들이 있다. 이와 함께 Doug Hellmann이 제공하는 글도 살펴보자. 

- multiprocessing : Python에서 여러 프로세스를 이용할 수 있게 한다. PC에 CPU 코어가 여러 개 있으면 연산 load를 여러 CPU로 분산할 수 있다.
- asyncio : 동시 실행 루틴을 만들고 규칙을 정해 병렬 실행을 지정한다.
- concurrent.futures : 태스크 컬렉션을 관리하고 동시에 실행한다.

각 기능을 시도해보면서 이해해서 어떤 기능에 적합한지 판단해보자. 

### 새로운 키워드 : async & await 

Python 3.5에는 표준적인 방법으로 동시 실행 루틴을 만들 수 있도록 `async`와 `await` 키워드가 추가되었다. 

for, with, def 키워드 앞에 `async 키워드`를 사용할 수 있다. 

## Tkinter를 이용한 GUI & Turtle 

## Test 기능 

`자동 시험`은 `정말정말 중요`하다. 일단 아래의 두 가지 모듈을 살펴보자.

- doctest : 모듈의 docstring에 테스트를 추가할 수 있다.  
  a. 많은 사용자가 칭찬하는 모듈 
- unittest : Python에서 자체적인 유닛테스트 버전을 제공하는 모듈
  a. 다른 언어의 유닛테스트와 비슷한 기능 제공
  b. 하지만, 충분히 파이썬답지 않다는 불평 존재. 그래서 `py.test`라는 도구가 탄생함 


  







