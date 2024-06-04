import sqlite3
conn = sqlite3.connect('project/accounting.db')
cur = conn.cursor()
cur.execute('SELECT * from categories')
clist = cur.fetchall()
c = input("choose number: 1.add category 2.show existing categories. ")
username = 'epihod'
if c == '1':
    category_name = input("category name: ")
    n = 0
    while n != 4:
        item = (username, category_name)
        n = 4
        a = 0
        if len(category_name)>15 or len(category_name)==0:
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
        if i[0]== username:
            print(i[1], end= '  ')
