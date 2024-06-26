p.47 
## 인터프리터 

`파이썬`이라는 단어는
- 프로그래밍 언어의 이름이면서
- 파이썬 인터프리터의 이름이다. 
    - 인터프리터란 파이썬 코드를 실행하는 기술

- Java VM과의 차이점
    - 어떻게 코드를 실행하느냐에 따라 다르다.
        - 파이썬 : 컴파일이라는 개념이 없음(소스 코드를 바이트코드로 변환하지 않고 바로 실행)
        - 자바 : 소스 코드를 바이트코드로 변환하는 compile 과정이 필요함

파이썬은 인터프리터를 사용하기 때문에 1줄씩 코드를 실행하는 것이 가능 
그래서 자바와 달리 main() 메소드 안에 원하는 코드를 넣지 않더라도 프로그램 실행 가능

파이썬에서는 코드를 블록이라 하지 않고 `스위트(suite)`라고 표현하는 걸 더 선호함

p.69
## import문을 사용할 수 있는 2가지 방식 

1. 프로그램의 namespace로 함수 이름을 import 
ex. from datetime import timedelta
    - 이걸 선언하고 나면 timedelta(days = 1) 사용가능
    - datetime이라는 큰 모듈에서 timedelta를 곧바로 사용


2. 모듈전체를 임포트 
ex. import time 
    - 이걸 선언하고 나면 time.sleep() 과 같이 메소드를 사용해줘야 함
    - 모듈 내의 변수 또는 메서드를 사용하기 위해서 `모듈.변수` 형식을 사용 

두 가지 모두 혼합해서 사용하고 있고 상황에 따라 더 적합한 방법이 있다. 

ex. 똑같은 이름의 메소드 F가 있다.

from A import F, from B import F
=> 이렇게 선언하면 `F` 메소드를 호출할 때 어떤 모듈의 F인지 모른다. 

그래서 import A, import B라고 선언하면
A.F(), B.F() 라고 사용함으로써 어떤 모듈의 F메소드인지 구분해서 사용할 수 있다. 

