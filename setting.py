import sqlite3
import maskpass
username = 'dori'
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
        sql = "UPDATE users set number = '%s' where username = '%s'" % (phone,username)
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
        sql = "UPDATE users set email = '%s' where username = '%s'" % (email,username)
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
                password = maskpass.askpass(prompt="password should have at least one special character: ", mask="*")
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