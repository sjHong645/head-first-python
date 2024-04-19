import mysql.connector

from DBcm import UseDatabase

def log_request(req : 'flask_request', res : str) -> None : 
    """Log details of the web request and the results
    """
    
    dbconfig = {
        'host' : 'localhost', 
        'user' : 'root', 
        'password' : 'asi', 
        'database' : 'vsearchlogDB', 
        'port' : 3308
    }
    
    with UseDatabase(dbconfig) as cursor : 
        _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
        
        
        cursor.execute(_SQL, (req.form['phrase'], 
                          req.form['letters'], 
                          req.remote_addr, 
                          req.user_agent.browser, 
                          res, ))

    
    