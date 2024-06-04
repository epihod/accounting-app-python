def revenue_record():
    print("Revenue record")
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
    source = input(" ")
    description = input("description(optional, inter '-' if you want to skip.): ")
    d2 = [*description]
    c = 0
    while c != 0:
        c = 1
        if len(d2)>100:
            description = input('description should have at most 100 characters. try again')
            c -= 1
revenue_record()