from sqlite3 import *
from pingpong import *

con = connect('C:/Users/User/Desktop/ping-pong(Nick)/ping-pong-sql.db')
cursor = con.cursor()

def table_cr():
    cursor.execute(''' CREATE TABLE games(
        name 1 STR,
        score 1 INT,
        name 2 STR,
        score 2 INT
    )
    
    ''')

data = cursor.fetchall()

con.commit()

print(data)