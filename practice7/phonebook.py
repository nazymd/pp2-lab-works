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

def insert_from_csv(file):
    with open(file, 'r') as f:
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
    print(cur.fetchall())
    

def menu():
    while True:
        print("\n1. CSV")
        print("2. Add")
        print("3. Update")
        print("4. Search name")
        print("5. Search phone")
        print("6. Delete")
        print("7. Show all contacts")
        print("0. Exit")


        c = input("Choose: ")

        if c == '1':
            insert_from_csv('contacts.csv')
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
        elif c == '0':
            break
create_table()
menu()