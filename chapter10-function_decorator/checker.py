from flask import session

from functools import wraps

# 함수 장식자는 함수이고
# 인자로 장식된 함수를 받는다. 
def check_logged_in(func) : 

    # 장식자 내부에서 새로운 함수를 정의해서 
    # 반환한다. 

    # wrapper라고 부르는 이유는 
    # 장식된 함수인 func을 호출할 뿐만 아니라
    # 호출과 관련한 추가 코드를 감싸는 기능도 제공한다.

    # wrapper 함수가 임의 개수와 모든 유형의 인자를 처리할 수 있도록 
    # 인자를 *args, **kwargs로 설정함 
    # 이렇게 설정함으로써 장식자와 장식된 함수가 같은 개수의 인자와 유형을 갖게 됨 

    @wraps(func) # 해당 장식자를 사용함으로써 장식자 생성을 마무리한다. 
    def wrapper(*args, **kwargs): 

        # 해당 조건을 만족하면 
        # 장식된 함수를 그대로 실행 
        if 'logged_in' in session :
            return func(*args, **kwargs)
        
        # 만족하지 않는다면
        # 'You are NOT logged in' 문자열 출력 
        return 'You are NOT logged in'

    return wrapper