
class CountFromBy : 

    # v, i의 기본값을 0과 1로 설정
    def __init__(self, v : int = 0, i : int = 1) -> None : 
        
        self.val = v
        self.incr = i
        
    def __repr__(self) -> str : 
        return str(self.val)

    def increase(self) -> None : 
        self.val += self.incr

if __name__ == '__main__' : 
    
    countFromBy = CountFromBy(123, 4444)
    
    print(countFromBy) # __repr__를 이용해서
                       # str(self.val)을 반환하기 때문에
                       # 123을 출력한다. 