import sqlite3
from datetime import datetime,timedelta,date
print("debriefing")
username = 'epihod'
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
today = datetime.now()
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
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
              round(expense / (total_expense / n2) * 100, 2))
    if c2 == '2':
        days = []
        for i in range(3):
            n_days_ago = today - timedelta(days= i)
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
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
              round(expense / (total_expense / n2) * 100, 2))
    if c2 == '3':
        days = []
        for i in range(7):
            n_days_ago = today - timedelta(days=i)
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
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
              round(expense / (total_expense / n2) * 100, 2))
    if c2 == '4':
        days = []
        c3 = input("from(yyyy/mm/dd): ")
        c4 = input("to(yyyy/mm/dd): ")
        c3 = datetime.strptime(c3, '%Y/%m/%d')
        c4 = datetime.strptime(c4, '%Y/%m/%d')
        n = c3-c4
        for i in range(n.days+1):
            n_days_ago = c3 - timedelta(days=i)
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
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
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
                print(i[1], end = ", ")
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
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
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
        print("ratio to other revenues", round(revenue / (total_revenue / n1) * 100, 2), "\nratio to other revenues",
              round(expense / (total_expense / n2) * 100, 2))