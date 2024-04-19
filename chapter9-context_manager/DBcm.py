"""DB Context Manager
"""

import mysql.connector

class UseDatabase : 
    
    def __init__(self, dbconfig : dict) -> None :
        """ self.host = dbconfig['host']
        self.user = dbconfig['user']
        self.password = dbconfig['password']
        self.database = dbconfig['database']
        self.port = dbconfig['port'] """
        
        self.configuration = dbconfig
    
    def __enter__(self) : 
        pass
    
    def __exit__(self) : 
        pass
    