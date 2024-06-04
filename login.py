import maskpass
from time import sleep
import sqlite3
print('login')
s = 0
n = 0
while s!=1:
    s=1
    c = 0
    l = 0
    username = input('username: ')
    password = maskpass.askpass(prompt="password(if you forgot your password,enter -1): ", mask="*")
    try:
        conn = sqlite3.connect('project/accounting.db')
        cursor = conn.cursor()
        sqlite_select_query = """SELECT * from users"""
        cursor.execute(sqlite_select_query)
        userlist = cursor.fetchall()
        if password == '-1':
            c2 = input("enter your email or your username: ")
            for data in userlist:
                if data[3] == c2 or data[6] == c2:
                    c3 = input("what is your favorite color?: ")
                    if c3 == data[8]:
                        print('your password is', data[4])
                        s -= 1
        else:
            for data in userlist:
                if data[3] == username and data[4] == password:
                    print('login successful.')
                    l = 1
                else:
                    c += 1
            if l == 1:
                break
            if c == len(userlist):
                print('username or password incorrect, try again. ')
                s -= 1
                n += 1
            if n % 3 == 0 and n > 0:
                print("try again after 1 minute")
                sleep(60)
                print("1 minute has passed.")
    except sqlite3.Error as error:
        print("Failed to read data from table", error)
