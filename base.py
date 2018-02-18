import sqlite3

con = sqlite3.connect('base.db')


cur = con.cursor()


sql = """
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL)"""

cur.execute(sql)
con.commit()
con.close()
