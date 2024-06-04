import sqlite3
conn = sqlite3.connect('accounting.db')
c = conn.cursor()
c.execute('CREATE TABLE  IF NOT EXISTS users (name text NOT NULL, last_name text, number text, username text, password text, city text, email text, birth text, color text);')
c.execute('CREATE TABLE  IF NOT EXISTS Revenue_record (username text, amount INTEGER, date text, source text, description text, type text);')
c.execute('CREATE TABLE  IF NOT EXISTS Expense_record (username text, amount INTEGER, date text, source text, description text, type text);')