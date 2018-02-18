import sqlite3

def commit_close(func):
    def decorator(* agrs):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*agrs)
        cur.execute(sql)
        con.commit()
        con.close
    return decorator

@commit_close
def db_insert(idusers, name, phone, email):
    return """
    INSERT INTO users (id, name, phone, email)
        VALUES({}, '{}', '{}', '{}')
    """.format(idusers, name, phone, email)

@commit_close
def db_update(name, email):
    return """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name, email)

@commit_close
def db_delete(email):
    return """
    DELETE FROM users WHERE email = '{}'
    """.format(email)

con = sqlite3.connect('base.db')
cur = con.cursor()

sql = 'SELECT * FROM users WHERE email = ?'
sql2 = 'SELECT * FROM users'

def db_select (email):
    for val in cur.execute(sql, (email, )):
        print(val)

def db_select_total():
    print(' ===> ( DADOS COMPLETOS DE TODOS USER ) <===')
    print('========================================================\n')
    for val in cur.execute(sql2):
        print(val)
    print('========================================================')
