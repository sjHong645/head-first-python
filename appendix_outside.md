## 웹 개발 기술

`장고(Django)`라는 기술이 Python 웹앱을 구현하는 기술로 널리 알려져 있다. 
`장고`는 플라스크와 달리 어느 정도 이해하고 배워야 장고 웹앱을 만들 수 있다. 

스스로를 웹 개발자라고 생각한다면 `최소한 장고의 튜토리얼은 확인`하는 것이 좋다. 그래야 플라스크를 계속 사용할 지 아니면 장고로 갈아탈지 선택할 수 있기 때문이다. 

장고 뿐만 아니라 다양한 웹 프레임워크가 있다. [링크](https://wiki.python.org/moin/WebFrameworks)

## 웹 데이터 작업 

requests 모듈을 사용하면 간단하면서도 강력한 Python API를 통해 HTTP, 웹 서비스와 상호작용할 수 있다. 

[requests와 관련한 더 자세한 내용](https://requests.readthedocs.io/en/latest/)

### 웹 데이터 스크랩 

Python은 웹과 궁합이 잘 맞으며 표준 라이브러리는 JSON, HTML, XML 및 비슷한 텍스트 기반 형식과 관련 인터넷 프로토콜을 사용할 수 있도록 다양한 모듈을 제공한다.  
표준 라이브러리에서 어떤 모듈을 제공하고 웹/인터넷 프로그래머에게 인기 있는 모듈이 무엇인지 아래 파이썬 문서에서 확인해보자. 

- [인터넷 데이터 처리](https://docs.python.org/3/library/netdata.html)
- [구조화된 마크업 처리 도구](https://docs.python.org/3/library/markup.html)
- [인터넷 프로토콜과 지원](https://docs.python.org/3/library/internet.html)

정적 웹 페이지에서만 이용할 수 있는 데이터를 작업해야 한다면 데이터를 스크랩하고 싶을거다. [스크랩 관련 정보](https://en.wikipedia.org/wiki/Web_scraping)

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Scrapy](https://scrapy.org/)

## sqlalchemy : 고차원적이며 Python에 기반한 RDBMS에 필요한 기술 집합 

[더 자세한 내용](https://www.sqlalchemy.org/)

### SQL말고 데이터를 질의하는 방법 

JSON 형식이나 테이블이 아닌 다른 형식으로 구성된 데이터를 처리하는 상황에서는 [MongoDB](https://www.mongodb.com/)가 적합한 선택일 수 있다. 

[pymongo 데이터베이스 드라이버](https://www.mongodb.com/ko-kr/docs/drivers/pymongo/)를 이용해 몽고디비로 Python 프로그램을 구현할 수 있다. 

## 테스트를 도와주는 도구 [py.test](https://doc.pytest.org/en/latest/)

