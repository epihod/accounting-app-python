import maskpass
from time import sleep
import sqlite3
import datetime

def signup():
    conn =  sqlite3.connect('project/accounting.db')
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
    user = (name, last_name, number, username, password, city, email, birth, color)
    add_signup(conn, user)


def add_signup(conn,user):
    sql = ''' INSERT INTO users(name,last_name,number,username,password,city,email,birth,color)
                  VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()


def login():
    print('login')
    s = 0
    n = 0
    while s != 1:
        s = 1
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
    info = [username,password]
    return info


def revenue_expense_record(username,c2):
    conn = sqlite3.connect('project/accounting.db')
    if c2 == '1':
        print("Revenue record")
    elif c2 == '2':
        print("Expense record")
    amount = input("amount: ")
    c = 0
    while c!=1:
        c = 1
        if not amount.isnumeric() or int(amount) < 0:
            amount = input("input is not in the right form try again: ")
            c -= 1
    date = input("date(yyyy/mm/dd): ")
    c = 0
    l31 = [1, 3, 5, 7, 8, 10, 12]
    l30 = [4, 6, 9, 11]
    while c != 3:
        d1 = date.split('/')
        c = 3
        if int(d1[1]) in l31 and int(d1[2]) > 31:
            date = input("date is incorrect. try again: ")
            c -= 1
        elif int(d1[1]) in l30 and int(d1[2]) > 30:
            date = input("date is incorrect. try again: ")
            c -= 1
        elif int(d1[1]) == 2 and int(d1[2]) > 29:
            date = input("date is incorrect. try again: ")
            c -= 1
    cur = conn.cursor()
    cur.execute("select * from categories")
    c = cur.fetchall()
    print("existing categories: ")
    for i in c:
        if i[0]== username:
            print(i[1], end = '  ')
    source = input("\nsource: ")
    description = input("description(optional, inter '-' if you want to skip.): ")
    d2 = [*description]
    c = 0
    while c != 0:
        c = 1
        if len(d2)>100:
            description = input('description should have at most 100 characters. try again')
            c -= 1
    typee = input("enter the type : 1.cash 2.check 3.digital currency \n")
    data = (username,amount,date,source,description,typee)
    if c2 == '1':
        add_revenue_expense(conn, data, c2)
    elif c2 == '2':
        add_revenue_expense(conn, data, c2)


def add_revenue_expense(conn, revenue, c):
    if c == '1':
        sql = ''' INSERT INTO Revenue_record(username,amount,date,source,description,type)
                        VALUES(?,?,?,?,?,?) '''
    elif c == '2':
        sql = ''' INSERT INTO Expense_record(username,amount,date,source,description,type)
                        VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, revenue)
    conn.commit()
    print("Record finished successfully")


def category(username):
    conn = sqlite3.connect('project/accounting.db')
    cur = conn.cursor()
    cur.execute('SELECT * from categories')
    clist = cur.fetchall()
    c = input("choose number: 1.add category 2.show existing categories. ")
    if c == '1':
        category_name = input("category name: ")
        n = 0
        while n != 4:
            item = (username, category_name)
            n = 4
            a = 0
            if len(category_name) > 15 or len(category_name) == 0:
                print("category name should have at most 15 characters and can't be empty.")
                n -= 1
            for char in category_name:
                if char.isdigit():
                    a += 1
                elif char.isalpha():
                    a += 1
            if a != len(category_name):
                print("category name should only contain number or english alphabet.")
                n -= 1
            if item in clist:
                print('category already exists.')
                n -= 1
            if n != 4:
                category_name = input("try again: ")
        sql = ''' INSERT INTO categories(username,category_name)
                      VALUES(?,?) '''
        cur.execute(sql, item)
        conn.commit()
        print("category added successfully.")
    elif c == '2':
        for i in clist:
            if i[0] == username:
                print(i[1], end='  ')


def search(username):
    with sqlite3.connect('project/accounting.db') as conn:
        cursor = conn.cursor()
        sqlite_select_query1 = """SELECT * from Revenue_record"""
        cursor.execute(sqlite_select_query1)
        data1 = cursor.fetchall()
        sqlite_select_query2 = """SELECT * from Expense_record"""
        cursor.execute(sqlite_select_query2)
        data2 = cursor.fetchall()
    n = 0
    print("search")
    c = input("choose the action: 1.search without filters 2.search with filters \n")
    if c == '1':
        print("search without filters")
        search = input("search(enter number or word): ")
        for i in data1:
            if i[0] == username:
                for j in i[1::]:
                    if search in j:
                        print("Revenue: ", i[1::])
                        n += 1
        for i in data2:
            if i[0] == username:
                for j in i[1::]:
                    if search in j:
                        print("Expense: ", i[1::])
                        n += 1
        if n == 0:
            print("no result found")
    date = {"Revenue": [], "Expense": []}
    if c == '2':
        print("search with filter")
        c2 = input(
            "choose the action: 1.day 2.month 3.year 4.set range 5.just Revenue 6.just expense 7.specific fields: ")
        if c2 == '1':
            day = input("enter your desired date(yyyy/mm/dd): ")
            for i in data1:
                if i[0] == username and i[2] == day:
                    date["Revenue"].append(i[1::])
            for i in data2:
                if i[0] == username and i[2] == day:
                    date["Expense"].append(i[1::])
            if len(date["Revenue"]) == 0 and len(date["Expense"]) == 0:
                print("no result found")
            else:
                print("Revenue")
                for i in date["Revenue:"]:
                    print(i)
                print("Expense")
                for i in date["Expense:"]:
                    print(i)
        if c2 == '2':
            month = input("enter your desired month(yyyy/mm): ")
            for i in data1:
                if i[0] == username and month in i[2]:
                    date["Revenue"].append(i[1::])
            for i in data2:
                if i[0] == username and month in i[2]:
                    date["Expense"].append(i[1::])
            if len(date["Revenue"]) == 0 and len(date["Expense"]) == 0:
                print("no result found")
            else:
                print("Revenue:")
                for i in date["Revenue"]:
                    print(i)
                print("Expense:")
                for i in date["Expense"]:
                    print(i)
        if c2 == '3':
            year = input("enter your desired year(yyyy): ")
            for i in data1:
                if i[0] == username and year in i[2]:
                    date["Revenue"].append(i[1::])
            for i in data2:
                if i[0] == username and year in i[2]:
                    date["Expense"].append(i[1::])
            if len(date["Revenue"]) == 0 and len(date["Expense"]) == 0:
                print("no result found")
            else:
                print("Revenue:")
                for i in date["Revenue"]:
                    print(i)
                print("Expense:")
                for i in date["Expense"]:
                    print(i)
        if c2 == '4':
            number_range = input("set range: ")
            number_range = number_range.split(" ")
            for i in data1:
                if int(number_range[0]) < int(i[1]) < int(number_range[1]) and i[0] == username:
                    print("Revenue ", i[1::])
            for i in data2:
                if int(number_range[0]) < int(i[1]) < int(number_range[1]) and i[0] == username:
                    print("Expense ", i[1::])
        if c2 == '5':
            print("just Revenue")
            word = input("search: ")
            for i in data1:
                if i[0] == username:
                    for j in i[1::]:
                        if word in j:
                            print(i[1::])
                            n += 1
            if n == 0:
                print("no result found")
        if c2 == '6':
            print("just Expense")
            word = input("search: ")
            for i in data2:
                if i[0] == username:
                    for j in i[1::]:
                        if word in j:
                            print(i[1::])
                            n += 1
            if n == 0:
                print("no result found")
        if c2 == '7':
            source = {"Revenue": [], "Expense": []}
            description = {"Revenue": [], "Expense": []}
            typ = {"Revenue": [], "Expense": []}
            search = input("search: ")
            for i in data1:
                if i[0] == username:
                    if search in i[3]:
                        source["Revenue"].append(i[1::])
                    elif search in i[4]:
                        description["Revenue"].append(i[1::])
                    elif search in i[5]:
                        typ["Revenue"].append(i[1::])
            for i in data2:
                if i[0] == username:
                    if search in i[3]:
                        source["Expense"].append(i[1::])
                    elif search in i[4]:
                        description["Expense"].append(i[1::])
                    elif search in i[5]:
                        typ["Expense"].append(i[1::])
            c3 = input("choose the number: 1.Revenue 2.Expense ")
            c4 = input("choose the number 1.source 2.description 3.type \n you can choose more than one number ")
            c4 = c4.split(" ")
            if c3 == "1":
                if '1' in c4:
                    for i in source["Revenue"]:
                        print("Revenue", i)
                        n += 1
                if '2' in c4:
                    for i in description["Revenue"]:
                        print("Revenue", i)
                        n += 1
                if '3' in c4:
                    for i in typ["Revenue"]:
                        print("Revenue", i)
                        n += 1
            if c3 == "2":
                if '1' in c4:
                    for i in source["Expense"]:
                        print("Expense", i)
                        n += 1
                if '2' in c4:
                    for i in description["Expense"]:
                        print("Expense", i)
                        n += 1
                if '3' in c4:
                    for i in typ["Expense"]:
                        print("Expense", i)
                        n += 1
            if n == 0:
                print("no result found.")


def debriefing(username):
    print("debriefing")
    with sqlite3.connect('project/accounting.db') as conn:
        cursor = conn.cursor()
        sqlite_select_query1 = """SELECT * from Revenue_record"""
        cursor.execute(sqlite_select_query1)
        data1 = cursor.fetchall()
        sqlite_select_query2 = """SELECT * from Expense_record"""
        cursor.execute(sqlite_select_query2)
        data2 = cursor.fetchall()
        sqlite_select_query3 = """SELECT * from categories"""
        cursor.execute(sqlite_select_query3)
        data3 = cursor.fetchall()
    c1 = input(" choose a number:\n 1.day 2.month 3.year 4.specific range of money 5.specific field ")
    revenue = 0
    total_revenue = 0
    expense = 0
    total_expense = 0
    n1 = 0
    n2 = 0
    today = datetime.datetime.now()
    if c1 == '1':
        c2 = input("choose a number:\n 1.today 2.past three days 3.past week 4.specific time range ")
        if c2 == '1':
            today = today.strftime(format='%Y/%m/%d')
            for i in data1:
                if username == i[0]:
                    total_revenue += int(i[1])
                    n1 += 1
                    if i[2] == today:
                        revenue += int(i[1])
            for i in data2:
                if username == i[0]:
                    total_expense += int(i[1])
                    n2 += 1
                    if i[2] == today:
                        expense += int(i[1])
            print("total revenue:", revenue, "\ntotal expense:", expense)
            print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
                  round(expense / total_expense * 100, 2))
            print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2),
                  "\nratio to other revenues",
                  round(expense / (total_expense / n2) * 100, 2))
        if c2 == '2':
            days = []
            for i in range(3):
                n_days_ago = today - datetime.timedelta(days=i)
                days.append(n_days_ago.strftime(format='%Y/%m/%d'))
            for i in data1:
                if username == i[0]:
                    total_revenue += int(i[1])
                    n1 += 1
                    if i[2] in days:
                        revenue += int(i[1])
            for i in data2:
                if username == i[0]:
                    total_expense += int(i[1])
                    n2 += 1
                    if i[2] in days:
                        expense += int(i[1])
            print("total revenue:", revenue, "\ntotal expense:", expense)
            print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
                  round(expense / total_expense * 100, 2))
            print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2),
                  "\nratio to other revenues",
                  round(expense / (total_expense / n2) * 100, 2))
        if c2 == '3':
            days = []
            for i in range(7):
                n_days_ago = today - datetime.timedelta(days=i)
                days.append(n_days_ago.strftime(format='%Y/%m/%d'))
            for i in data1:
                if username == i[0]:
                    total_revenue += int(i[1])
                    n1 += 1
                    if i[2] in days:
                        revenue += int(i[1])
            for i in data2:
                if username == i[0]:
                    total_expense += int(i[1])
                    n2 += 1
                    if i[2] in days:
                        expense += int(i[1])
            print("total revenue:", revenue, "\ntotal expense:", expense)
            print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
                  round(expense / total_expense * 100, 2))
            print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2),
                  "\nratio to other revenues",
                  round(expense / (total_expense / n2) * 100, 2))
        if c2 == '4':
            days = []
            c3 = input("from(yyyy/mm/dd): ")
            c4 = input("to(yyyy/mm/dd): ")
            c3 = datetime.datetime.strptime(c3, '%Y/%m/%d')
            c4 = datetime.datetime.strptime(c4, '%Y/%m/%d')
            n = c3 - c4
            for i in range(n.days + 1):
                n_days_ago = c3 - datetime.timedelta(days=i)
                days.append(n_days_ago.strftime(format='%Y/%m/%d'))
            for i in data1:
                if username == i[0]:
                    total_revenue += int(i[1])
                    n1 += 1
                    if i[2] in days:
                        revenue += int(i[1])
            for i in data2:
                if username == i[0]:
                    total_expense += int(i[1])
                    n2 += 1
                    if i[2] in days:
                        expense += int(i[1])
            print("total revenue:", revenue, "\ntotal expense:", expense)
            print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
                  round(expense / total_expense * 100, 2))
            print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2),
                  "\nratio to other revenues",
                  round(expense / (total_expense / n2) * 100, 2))
    elif c1 == "2":
        month = input("enter the month(yyyy/mm): ")
        for i in data1:
            if username == i[0]:
                total_revenue += int(i[1])
                n1 += 1
                if month in i[2]:
                    revenue += int(i[1])
        for i in data2:
            if username == i[0]:
                total_expense += int(i[1])
                n2 += 1
                if month in i[2]:
                    expense += int(i[1])
        print("total revenue:", revenue, "\ntotal expense:", expense)
        print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
              round(expense / total_expense * 100, 2))
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
              round(expense / (total_expense / n2) * 100, 2))
    elif c1 == '3':
        year = input("enter the year(yyyy): ")
        for i in data1:
            if username == i[0]:
                total_revenue += int(i[1])
                n1 += 1
                if year in i[2]:
                    revenue += int(i[1])
        for i in data2:
            if username == i[0]:
                total_expense += int(i[1])
                n2 += 1
                if year in i[2]:
                    expense += int(i[1])
        print("total revenue:", revenue, "\ntotal expense:", expense)
        print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
              round(expense / total_expense * 100, 2))
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
              round(expense / (total_expense / n2) * 100, 2))
    elif c1 == '4':
        a = input("from: ")
        b = input("to: ")
        for i in data1:
            if username == i[0]:
                total_revenue += int(i[1])
                n1 += 1
                if int(a) <= int(i[1]) <= int(b):
                    revenue += int(i[1])
        for i in data2:
            if username == i[0]:
                total_expense += int(i[1])
                n2 += 1
                if int(a) <= int(i[1]) <= int(b):
                    expense += int(i[1])
        print("total revenue:", revenue, "\ntotal expense:", expense)
        print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
              round(expense / total_expense * 100, 2))
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
              round(expense / (total_expense / n2) * 100, 2))
    elif c1 == '5':
        c2 = input("choose the number: 1.category 2.type")
        if c2 == '1':
            print("existing categories: ")
            for i in data3:
                if i[0] == username:
                    print(i[1], end=", ")
            category = input("\nenter the category: ")
            for i in data1:
                if username == i[0]:
                    total_revenue += int(i[1])
                    n1 += 1
                    if category == i[3]:
                        revenue += int(i[1])
            for i in data2:
                if username == i[0]:
                    total_expense += int(i[1])
                    n2 += 1
                    if category == i[3]:
                        expense += int(i[1])
            print("total revenue:", revenue, "\ntotal expense:", expense)
            print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
                  round(expense / total_expense * 100, 2))
            print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2),
                  "\nratio to other revenues",
                  round(expense / (total_expense / n2) * 100, 2))
        elif c2 == '2':
            typ = input("enter the type(cash, check, digital currency): ")
            for i in data1:
                if username == i[0]:
                    total_revenue += int(i[1])
                    n1 += 1
                    if typ == i[5]:
                        revenue += int(i[1])
            for i in data2:
                if username == i[0]:
                    total_expense += int(i[1])
                    n2 += 1
                    if typ == i[5]:
                        expense += int(i[1])
            print("total revenue:", revenue, "\ntotal expense:", expense)
            print("ratio to overall revenue", round(revenue / total_revenue * 100, 2), "\nratio to overall expense",
                  round(expense / total_expense * 100, 2))
            print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2),
                  "\nratio to other revenues",
                  round(expense / (total_expense / n2) * 100, 2))


def setting(username):
    conn = sqlite3.connect('project/accounting.db')
    cur = conn.cursor()
    print("setting")
    c1 = input("choose the action: 1.changing information 2.delete user 3.delete transactions")
    symbols = '!@#$%^&*()'
    if c1 == '1':
        c2 = input("1.phone number 2.email 3.password \n")
        if c2 == '1':
            phone = input("new phone number: ")
            c = 0
            while c != 3:
                c = 3
                if not phone.isnumeric():
                    phone = input("phone number should contain only numbers. try again: ")
                    c -= 1
                elif not phone.startswith("09"):
                    phone = input("phone number should start with 09. try again: ")
                    c -= 1
                elif len(phone) != 11:
                    phone = input("phone number should have 11 digits. try again: ")
                    c -= 1
            sql = "UPDATE users set number = '%s' where username = '%s'" % (phone, username)
            cur.execute(sql)
            conn.commit()
            print("phone number updated successfully")
        elif c2 == '2':
            email = input("new email: ")
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
            sql = "UPDATE users set email = '%s' where username = '%s'" % (email, username)
            cur.execute(sql)
            conn.commit()
            print("email updated successfully")
        elif c2 == '3':
            password = maskpass.askpass(prompt="new Password:", mask="*")
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
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
                    password = maskpass.askpass(prompt="password should have at least one special character: ",
                                                mask="*")
                    c -= 1
                elif len(password) < 6:
                    password = maskpass.askpass(prompt="password should be at least 6 characters: ", mask="*")
                    c -= 1
            sql = "UPDATE users set password = '%s' where username = '%s'" % (password, username)
            cur.execute(sql)
            conn.commit()
            print("password updated successfully")
    elif c1 == '2':
        c2 = input("are you sure?(y/n): ")
        if c2 == "y":
            sql = "DELETE FROM users WHERE username = '%s'" % username
            cur.execute(sql)
            conn.commit()
            sql = "DELETE FROM categories WHERE username = '%s'" % username
            cur.execute(sql)
            conn.commit()
            sql = "DELETE FROM Expense_record WHERE username = '%s'" % username
            cur.execute(sql)
            conn.commit()
            sql = "DELETE FROM Revenue_record WHERE username = '%s'" % username
            cur.execute(sql)
            conn.commit()
            print("user deleted, you logged out.")
            exit()
    elif c1 == '3':
        c2 = input("choose the number: 1.revenue 2.expense 3.both ")
        if c2 == '1' or c2 == '3':
            sql = "DELETE FROM Revenue_record WHERE username = '%s'" % username
            cur.execute(sql)
            conn.commit()
            print("Revenue transactions deleted")
        if c2 == '2' or c2 == '3':
            sql = "DELETE FROM Expense_record WHERE username = '%s'" % username
            cur.execute(sql)
            conn.commit()
            print("Expense transaction deleted")


print("welcome, choose the action: \n 1.sign up \n 2.log in")
c1 = int(input())
if c1 == 1:
    signup()
    info = login()
if c1 == 2:
    info = login()
now = datetime.datetime.now()
print("you entered at", now)
c2 = input("choose the action.\n 1.Revenue record \n 2.Expense record \n 3.Categories \n 4.Search \n 5.Debriefing \n 6.Setting \n 7.Exit \n")
while c2 != '7':
    if c2 == '1':
        revenue_expense_record(info[0], c2)
    elif c2 == '2':
        revenue_expense_record(info[0], c2)
    elif c2 == '3':
        category(info[0])
    elif c2 =='4':
        search(info[0])
    elif c2 == '5':
        debriefing(info[0])
    elif c2 == '6':
        setting(info[0])
    c2 = input("\n choose the action.\n 1.Revenue record \n 2.Expense record \n 3.Categories \n 4.Search \n 5.Debriefing \n 6.Setting \n 7.Exit \n")