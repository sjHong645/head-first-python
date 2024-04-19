import mysql.connector

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
    
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor() 
    
    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s)"""
              
    cursor.execute(_SQL, (req.form['phrase'], 
                          req.form['letters'], 
                          req.remote_addr, 
                          req.user_agent.browser, 
                          res, ))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    