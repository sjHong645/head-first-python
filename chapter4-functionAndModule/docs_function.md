# 코드 재사용

## 함수, 모듈, 라이브러리의 관계 
여러 줄의 코드를 모아놓은 걸 `함수(function)`라 한다.

`함수`를 여러 개 묶어 놓은 파일을 `모듈(module)`이라 한다. 

`모듈`을 여러 개 묶어서 `라이브러리`를 만들 수 있다.

## 파이썬은 매개변수와 함수의 반환 타입 지정을 강제하지 않는다. 

`어노테이션`을 이용해서 어떤 자료형을 사용할 지 권고할 수는 있다. 물론 강제할 수는 없다. 

인터프리터는 매개변수와 함수의 유형에 아무 관심이 없기 때문이다. 

### PEP(Python Enhancement Proposals) 8은 꼭 읽어보자

- 링크 : https://peps.python.org/pep-0008/

- `문자열`은 가능하면 `작은따옴표`를 사용할 것
    - docstring은 큰따옴표를 사용할 것

### 결과값을 반환할 때

- 결과값이 empty인지 쉽게 확인할 수 있는 메서드 - `bool`
    - bool 메소드의 인자에 뭐라도 있으면 true / 아니면 false를 반환하기 때문
    - bool([]), bool(''), bool({}) => false
    - bool(42), bool('apple'), bool([23, 33]) => true 


## 파이썬에서는 매개변수를 전달할 때 값을 전달할까? 레퍼런스를 전달할까? 

- call by value(값에 의한 호출방식) : 함수 인자의 변수에 `값이 사용`되는 기법 

함수의 suite에서 값이 변경되더라도 함수가 호출한 코드의 변수값은 바뀌지 않는다. 
즉, 원래 변수값을 복사해서 인자로 전달한다고 생각할 수 있다.

만약에 함수 suite에서 변경된 값을 전달받고 싶다면
해당 함수의 return을 통해서 전달받아야 한다. 

- call by reference(레퍼런스에 의한 호출방식) : 함수를 호출한 코드의 변수에 링크를 유지한다. 

함수 suite에서 변수값이 변경된다면 함수를 호출한 코드의 변수값도 바뀐다. 

원래 변수에 이름만 다르게 붙여 인자로 전달한다고 생각할 수 있다. 

그렇기 때문에 굳이 함수 suite에서 변경된 값을 받기 위해 return을 이용할 필요가 없다. 

- 예시 메소드 
```
def double(arg) : 
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

def change(arg) : 
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)
```

- 상황 1
```
nums = 10
double(num)을 한 이후에 
nums는 여전히 10 
```

- 상황 2 
```
numbers = [42, 256, 16]
change(numbers)을 한 이후에
numbers = [42, 256, 16, 'More data']로 변경됨 
```

그렇다. 파이썬 함수 인자는 call by value, call by reference 모두 지원한다. 

p.227

