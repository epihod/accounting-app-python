import maskpass
import sqlite3


def signup():
    print("welcome, choose the action: \n 1.sign up \n 2.log in")
    c1 = int(input())
    if c1 == 1:
        print("sign up")
        name = input("first name: ")
        c = 0
        while c != 1:
            c = 1
            if not name.isalpha():
                name = input("name should only contain english letters.try again: ")
                c -= 1
        last_name = input("last name: ")
        c = 0
        while c != 1:
            c = 1
            if not last_name.isalpha():
                last_name = input("last name should only contain english letters.try again: ")
                c -= 1
        number = input("phone number: ")
        c = 0
        while c != 3:
            c = 3
            if not number.isnumeric():
                number = input("phone number should contain only numbers. try again: ")
                c -= 1
            elif not number.startswith("09"):
                number = input("phone number should start with 09. try again: ")
                c -= 1
            elif len(number) != 11:
                number = input("phone number should have 11 digits. try again: ")
                c -= 1
        username = input("username: ")
        password = maskpass.askpass(prompt="Password:", mask="*")
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        symbols = '!@#$%^&*()'
        while c != 5:
            c = 5
            for char in password:
                if char.isdigit():
                    a += 1
                elif char.isupper():
                    b += 1
                elif char.islower():
                    d += 1
                elif char in symbols:
                    e += 1
            if a < 1:
                password = maskpass.askpass(prompt="password should have at least one number: ", mask="*")
                c -= 1
            elif b < 1:
                password = maskpass.askpass(prompt="password should have at least one capital letter: ", mask="*")
                c -= 1
            elif d < 1:
                password = maskpass.askpass(prompt="password should have at least one lowercase letter: ", mask="*")
                c -= 1
            elif e < 1:
                password = maskpass.askpass(prompt="password should have at least one special character: ", mask="*")
                c -= 1
            elif len(password) < 6:
                password = maskpass.askpass(prompt="password should be at least 6 characters: ", mask="*")
                c -= 1
        password_repeat = maskpass.askpass(prompt="repeat password: ", mask="*")
        c = 0
        while c != 1:
            c = 1
            if password != password_repeat:
                password_repeat = maskpass.askpass(prompt="password and your input didn't match. try again:", mask="*")
            c -= 1
        cities = ['Tehran', 'Tabriz', 'Isfahan', 'Yazd', 'Shiraz', 'Mashhad', 'Kashan', 'Kerman', 'Rasht', 'Qazvin',
                  'Hamedan', 'Ardabil']
        print(cities)
        city = input("choose your city: ")
        email = input("email: ")
        c = 0
        while c != 2:
            c = 2
            if '@' not in email:
                email = input("email is not the right format.try again: ")
                c -= 1
            elif not email.endswith('gmail.com') and not email.endswith('yahoo.com'):
                email = input("email is not the right format. try again: ")
                c -= 1
            try:
                e1 = email.split("@")
                for i in e1[0]:
                    if i in symbols:
                        email = input("email is not the right format.try again: ")
                        c -= 1
            except Exception:
                email = input("email is not the right format.try again: ")
                c -= 1
        birth = input("birth date(yyyy/mm/dd): ")
        c = 0
        l31 = [1, 3, 5, 7, 8, 10, 12]
        l30 = [4, 6, 9, 11]
        while c != 4:
            b1 = birth.split('/')
            c = 4
            if 2005 < int(b1[0]) < 1920:
                birth = input("birth year should be at least 1920 and at most 2005. try again: ")
                c -= 1
            elif int(b1[1]) in l31 and int(b1[2]) > 31:
                birth = input("birth day is incorrect. try again: ")
                c -= 1
            elif int(b1[1]) in l30 and int(b1[2]) > 30:
                birth = input("birth day is incorrect. try again: ")
                c -= 1
            elif int(b1[1]) == 2 and int(b1[2]) > 29:
                birth = input("birth day is incorrect. try again: ")
                c -= 1
        color = input("what is your favorite colore? ")
        print("you signed up successfully.")
    with sqlite3.connect('project/accounting.db') as conn:
        user = (name, last_name, number, username, password, city, email, birth, color)
        add_signup(conn, user)
    info = [name, last_name, number, username, password, city, email, birth, color]
    return info


def add_signup(conn,user):
    sql = ''' INSERT INTO users(name,last_name,number,username,password,city,email,birth,color)
                  VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()


a = signup()
print(a)