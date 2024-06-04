import sqlite3
username = 'epihod'
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
        if i[0]==username:
            for j in i[1::]:
                if search in j:
                    print("Revenue: ",i[1::])
                    n += 1
    for i in data2:
        if i[0]==username:
            for j in i[1::]:
                if search in j:
                    print("Expense: ",i[1::])
                    n += 1
    if n == 0:
        print("no result found")
date = {"Revenue": [], "Expense": []}
if c == '2':
    print("search with filter")
    c2 = input("choose the action: 1.day 2.month 3.year 4.set range 5.just Revenue 6.just expense 7.specific fields: ")
    if c2 == '1':
        day = input("enter your desired date(yyyy/mm/dd): ")
        for i in data1:
            if i[0] == username and i[2] == day:
                date["Revenue"].append(i[1::])
        for i in data2:
            if i[0] == username and i[2] == day:
                date["Expense"].append(i[1::])
        if len(date["Revenue"])==0 and len(date["Expense"])==0:
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
        if len(date["Revenue"])==0 and len(date["Expense"])==0:
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
        if len(date["Revenue"])==0 and len(date["Expense"])==0:
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
            if int(number_range[0]) < int(i[1]) < int(number_range[1]) and i[0]==username:
                print("Revenue ", i[1::])
        for i in data2:
            if int(number_range[0]) < int(i[1]) < int(number_range[1]) and i[0]==username:
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
        typ = {"Revenue": [], "Expense":[]}
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
                    print("Revenue",i)
                    n += 1
            if '2' in c4:
                for i in description["Revenue"]:
                    print("Revenue",i)
                    n += 1
            if '3' in c4:
                for i in typ["Revenue"]:
                    print("Revenue",i)
                    n += 1
        if c3 == "2":
            if '1' in c4:
                for i in source["Expense"]:
                    print("Expense",i)
                    n += 1
            if '2' in c4:
                for i in description["Expense"]:
                    print("Expense",i)
                    n += 1
            if '3' in c4:
                for i in typ["Expense"]:
                    print("Expense",i)
                    n += 1
        if n == 0:
            print("no result found.")
