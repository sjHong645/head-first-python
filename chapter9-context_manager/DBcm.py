"""DB Context Manager
"""

import mysql.connector

class UseDatabase : 
    
    def __init__(self, dbconfig : dict) -> None :
        """ 
        # 내가 쓴 오답
        self.host = dbconfig['host']
        self.user = dbconfig['user']
        self.password = dbconfig['password']
        self.database = dbconfig['database']
        self.port = dbconfig['port'] """
        
        self.configuration = dbconfig
    
    def __enter__(self) -> 'cursor' : 
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, exc_trace) -> None: 
        
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    