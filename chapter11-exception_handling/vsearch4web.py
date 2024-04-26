from flask import Flask, render_template, request, escape, copy_current_request_context
from vsearch import search4letters

from DBcm import UseDatabase, ConnectionError, CredentialError, SQLError

from threading import Thread

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    # log_request(request, results)
    
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """Log details of the web request and the results."""
        
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                req.user_agent.browser,
                                res, ))
    
    try : 
        t = Thread(target = log_request, args = (request, results))
        t.start
        
    except Exception as err: 
        print('*** Logging failed with this error :', str(err))
    
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    
    try : 
        # with문 내에서 발생하는 오류는 
        # 컨텍스트 매니저의 __enter__ 에서 오류 출력 
        with UseDatabase(app.config['dbconfig']) as cursor:
            
            # with문을 지나고 나서 발생하는 오류는
            # 컨텍스트 매니저의 __exit__ 에서 오류 출력 
            # 여기서 오류가 발생하면 __exit__ 메소드에 
            # 예외의 유형, 예외 값, 예외 역추적 정보 3가지 인자가 전달된다. 
            _SQL = """select phrase, letters, ip, browser_string, results
                    from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
            
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)
    
    # 컨텍스트 매니저의 __enter__에서 발생하는 2가지 예외를 처리하는 코드 
    # ConnectionError, CredentialError
    except ConnectionError as err : 
        print('Is your database switched on? Error:', str(err))
        
    except CredentialError as err : 
        print('User-id/Password issues. Error:', str(err))
    
    # __exit__에서 발생하는 예외를 처리하는 코드 
    except SQLError as err : 
        print('Is your query correct? Error:', str(err))
    
    except Exception as err : 
        print('Something went wrong:', str(err))


if __name__ == '__main__':
    app.run(debug=True)
