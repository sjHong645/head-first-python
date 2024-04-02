## `with`문과 연결하기 

- 파이썬 언어는 상당히 유연해서 반드시 객체 지향으로 프로그래밍 할 필요는 없다. 
    - 오히려 `클래스를 이용해서 with문과 연결`하는 걸 권장한다.
    - 표준 라이브러리에서 클래스를 이용하지 않고도 비슷한 기능을 할 수 있도록 지원하지만 범용성이 떨어진다. 

with 문과 연결하려면 `클래스를 생성`해야 한다. 클래스를 만드는 방법을 배운 다음에 `컨텍스트 관리 프로토콜`을 준수하는 클래스를 구현할 것이다. 이 프로토콜을 준수해야 with문과 연결할 수 있다. 

### Question

1. 파이썬은 정확히 객체지향, 함수형, 절차형 중 어떤 종류의 프로그래밍 언어에 속하는가? 
- 3가지 종류의 프로그래밍 언어 특성을 모두 지원해서 필요하다면 모든 특성을 혼합할 수 있다.
- 그만큼 파이썬 프로그래밍은 유연해서 내가 선호하는 방식으로 코드를 작성하면 된다. 

2. 그러면 클래스를 만드는 프로그래밍 기법은 추천하지 않는 건지? 
- 그렇지 않다. 애플리케이션 클래스가 필요하다면 클래스를 만들면 된다. 

## 객체 지향 입문

여기서는 파이썬 클래스의 모든 것을 다루지 않음. 상속, 다형성 등의 개념은 다루지 않을 것임. 
(물론, 파이썬에서는 두 개념을 모두 지원함)

`컨텍스트 관리 프로토콜`을 구현하는데 필요한 클래스를 만들만큼 충분히 클래스를 배울 것이고 `캡슐화`를 주로 살펴볼 예정 

### Naming convention 

- 함수 : 소문자 사용 & 언더바로 구분
- 클래스 : Camel case 사용(단어의 첫 글자만 대문자로 사용)

## 던더 메소드(Double Underscore 메소드)

`__init__`의 의미는 이미 알고 있어서 자세히 써놓지는 않을 거다. 
여기서는 던더 메소드에 대해 소개한 내용만 적을 것이다. 

던더를 오버라이드 하지 않으면 object라 불리는 클래스로 표준동작이 구현되어 제공된다. 즉, 던더메소드는 object에서 제공한대로 쓰거나 원하는대로 오버라이드 해서 사용할 수도 있다. 

- 예시
    -  `__eq__` 메서드 
        - `== 연산자`를 사용했을 때 기본 동작을 정의한 메소드. 마찬가지로 원하는대로 오버라이딩해서 정의할 수 있다. 

    - `__ge__` 메서드 
        - `> 연산자`를 사용했을 때 기본 동작을 정의한 메소드. 마찬가지로 원하는대로 오버라이딩해서 정의할 수 있다. 

`__init__` 메소드 : 객체와 관련된 속성을 초기화할 때 사용하는 메서드 

그래서 객체의 생성자를 정의할 때 `__init__ 메서드`를 호출하면 된다. 이것도 메서드이기 때문에 첫 번째 인자로 `self`를 정의해줘야 한다. 

### 던더 repr 정의하기 (p.368)

내가 생성한 인스턴스를 그냥 출력했을 때 다음과 같은 형식으로 출력된다. 

```
<__main__.CountFromBy object at 0x000002AD06570190>
```

- `__main__.CountFromBy` : 해당 인스턴스의 type 값을 의미. type(인스턴스)를 했을 때 나타나는 결과값

- `0x000002AD06570190` : 해당 인스턴스의 고유 식별자인데 객체의 메모리 주소 정보를 의미. hex(id(인스턴스))를 했을 때 나타나는 결과값 

그렇다면 해당 인스턴스는 왜 이러한 값들을 출력하는 걸까? 