import csv
from connect import conn
conn = conn()
cur = conn.cursor()

def create_table():
    cur.execute("""
        create table if not exists phonebook(
            id serial primary key,
            name text,
            phone text
                )
                """)
    conn.commit()

def insert_from_csv ():
    with open("contacts.csv", 'r') as f:
        reader=csv.reader(f)
        next(reader)

        for r in reader:
            cur.execute(
                "insert into phonebook (name, phone) values (%s, %s)", 
                (r[0], r[1])
            )
    conn.commit()
    print("csv imported")

def insert_from_console():
    name=input("Name")
    phone=input("Phone")
    cur.execute(
        "insert into phonebook (name, phone) values (%s, %s)",
        (name, phone)
    )
    conn.commit()

def update_number():
    name=input("Name: ")
    phone=input("New number: ")

    cur.execute(
        "update phonebook set phone=%s where name=%s",
        (name, phone)
    )
    conn.commit()

def search_by_name():
    name=input("Name: ")
    cur.execute(
        "select * from phonebook where name like %s",
        ('%' + name+'%',)
    )
    print(cur.fetchall())
def search_by_phone():
    phone=input()
    cur.execute(
        "select * from phonebook where phone like %s",
        ( phone + '%',)
    )
    print(cur.fetchall())

def contact_delete():
    choice=input("1 - name, 2 - phone: ")
    if choice == '1':
        name=input()
        cur.execute("delete from phonebook where name=%s", (name,))
    else:
        phone=input()
        cur.execute("delete from phonebook where phone=%s", (phone,))
    conn.commit()

def show_all():
    cur.execute(
    "select * from phonebook"
    )
    numname=cur.fetchall()
    for i in numname:
        print(i[1], i[2], "\n")

def search_pattern_func():
    pattern = input("Search pattern: ")
    cur.execute(
        "SELECT * FROM search_pattern(%s)",
        (pattern,)
    )
    rows = cur.fetchall()
    for r in rows:
        print(r)

def show_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute(
        "SELECT * FROM get_phonebook_paginated(%s, %s)",
        (limit, offset)
    )
    rows = cur.fetchall()
    for r in rows:
        print(r)


def insert_or_update():
    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute(
        "CALL insert_or_update_user(%s, %s)",
        (name, phone)
    )
    conn.commit()

def insert_many():
    names = input("Names: ").split(',')
    phones = input("Phones: ").split(',')

    cur.execute(
        "CALL insert_many_users(%s, %s)",
        (names, phones)
    )
    conn.commit()

def delete_user_proc():
    value = input("Name or phone: ")

    cur.execute(
        "CALL delete_user(%s)",
        (value,)
    )
    conn.commit()
    

def menu():
    while True:
        print("\n1. CSV")
        print("2. Add")
        print("3. Update")
        print("4. Search name")
        print("5. Search phone")
        print("6. Delete")
        print("7. Show all contacts")
        print("8. Search")
        print("9. Pagination")
        print("10. Insert or Update")
        print("11. Insert many")
        print("12. Delete")
        print("0. Exit")


        c = input("Choose: ")

        if c == '1':
            insert_from_csv()
        elif c == '2':
            insert_from_console()
        elif c == '3':
            update_number()
        elif c == '4':
            search_by_name()
        elif c == '5':
            search_by_phone()
        elif c == '6':
            contact_delete()
        elif c == '7':
            show_all()
        elif c == '8':
            search_pattern_func()
        elif c == '9':
            show_paginated()
        elif c == '10':
            insert_or_update()
        elif c == '11':
            insert_many()
        elif c == '12':
            delete_user_proc()
        elif c == '0':
            break
create_table()
menu()
