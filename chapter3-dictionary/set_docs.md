# 집합 

- 특징 : 중복 자료를 허용하지 않는다. & 순서가 정해져 있지 않는다. 

- 사용법 
    - 기본 : 중괄호(`{}`)를 사용해서 구현한다.
        - ex. set_test = {'a', 'e', 'i', 'o'}

    - set() 메소드
        - ex. set_test = set('aeio') 
        - 출력 형태 : {'a', 'e', 'i', 'o'}

    - 집합에 있는 내용을 list로 저장하고 싶다면? 
        - ex. set_list = list(set_test) # 정렬하고 싶다면 sorted 메소드를 쓰면 된다. 

- 합집합, 차집합, 교집합, 

    - union(합집합)
        ex. vowels = set('aeiou')
            word = 'hello'
            u = vowels.union(set(word)) # vowel라는 집합과 set(word) 집합의 합집합을 u에 할당 
    
    - difference(차집합)
        ex. vowels = set('aeiou')
            word = 'hello'
            d = vowels.difference(set(word)) # vowel라는 집합에서 set(word) 집합에 있는 내용을 제외
                                             # 즉, vowel 집합에서 set(word) 집합을 차집합

    - intersection(교집합)
        ex. vowels = set('aeiou')
            word = 'hello'
            i = vowels.intersection(set(word)) # vowel라는 집합과 set(word) 집합의 공통 부분
                                             # 즉, vowel 집합에서 set(word) 집합을 차집합