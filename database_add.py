import sqlite3
username = "epihod"
with sqlite3.connect('project/accounting.db') as conn:
    cur = conn.cursor()
    cur.execute("select * from categories")
    c = cur.fetchall()
    for i in c:
        if i[0]== username:
            print(i[1], end = ", ")