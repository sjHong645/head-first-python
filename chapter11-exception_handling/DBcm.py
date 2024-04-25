"""DB Context Manager
"""
import mysql.connector

# __enter__ 메서드 안에서 ProgrammingError가 발생하는 경우의 에러 
class ConnectionError(Exception) : 
    pass

# __enter__ 메서드 안에서 ProgrammingError가 발생하는 경우의 에러 
class CredentialError(Exception) : 
    pass

# __exit__ 메서드 안에서 ProgrammingError가 발생하는 경우의 에러 
class SQLError(Exception) : 
    pass

class UseDatabase : 
    
    def __init__(self, dbconfig : dict) -> None :
               
        self.configuration = dbconfig
        
        """ 
        # 내가 쓴 오답
        self.host = dbconfig['host']
        self.user = dbconfig['user']
        self.password = dbconfig['password']
        self.database = dbconfig['database']
        self.port = dbconfig['port'] 
        """
    
    def __enter__(self) -> 'cursor' : 
        
        try : 
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            
            return self.cursor
        
        # DBcm을 사용할 때 
        # __enter__ 메소드를 실행하는 와중에 mysql InterfaceError가 발생하면
        # ConnectionError가 발생하도록 했음 
        
        # 이러면 MySQL에서 다른 RDBMS로 바꾸더라도 
        # DBcm을 사용하던 파일들은 코드를 변경할 필요가 없음
        # 해당 파일들은 커스텀 예외인 ConnectionError만 처리해주면 되기 때문이다.
        except mysql.connector.errors.InterfaceError as err : 
                raise ConnectionError(err)
            
        except mysql.connector.errors.ProgrammingError as err : 
                raise CredentialError(err)
    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None: 
        
        # 여기에 코드를 추가하면 예외가 발생할 때 
        # 아래 3개 행의 코드가 실행되지 않음 
        
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        
        # 여기에 코드를 추가하면 예외가 발생할 때 
        # 예외를 처리하기 이전에 '__exit__'가 수행하던 동작을 완료할 수 있음 
        
        # ProgrammingError가 발생할 때 SQLError를 발생하도록 함 
        if exc_type is mysql.connector.errors.ProgrammingError : 
            raise SQLError(exc_value)
        
        # 예상치 못한 예외가 __exit__에 전달되는 경우
        # 해당 예외를 처리하는 부분 
        elif exc_type : 
            raise exc_type(exc_value)