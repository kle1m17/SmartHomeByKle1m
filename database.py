import sqlite3 as sq
from main import MainWindow

win = MainWindow()

def Register(login, email, password):
    with sq.connect("db.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Users Where Login='{login}';")
        value = cur.fetchall()
        if value != []:
            MainWindow.Message_Box('User already exists')
        else:
            cur.execute(f"INSERT INTO Users VALUES('{login}', '{password}', '{email}')")
        


def SignIn(login, password):
    with sq.connect("db.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Users Where Login='{login}';")
        value = cur.fetchall()
        if value != [] and value[0][2] == password:
            MainWindow.Message_Box('Succes!')
        else:
            print("ERROR")
        
