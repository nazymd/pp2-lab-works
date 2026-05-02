import json
import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()


# ---------- ADD CONTACT ----------
def add_contact():
    name = input("name: ")
    email = input("email: ")
    birthday = input("birthday YYYY-MM-DD: ")
    group = input("group: ")

    cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING", (group,))
    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    gid = cur.fetchone()[0]

    cur.execute("""
    INSERT INTO contacts(first_name,email,birthday,group_id)
    VALUES (%s,%s,%s,%s)
    """, (name, email, birthday, gid))

    conn.commit()
    print("added")


# ---------- ADD PHONE ----------
def add_phone():
    cur.execute(
        "CALL add_phone(%s,%s,%s)",
        (input("name: "), input("phone: "), input("type home/work/mobile: "))
    )
    conn.commit()
    print("phone added")


# ---------- MOVE GROUP ----------
def move_group():
    cur.execute(
        "CALL move_to_group(%s,%s)",
        (input("name: "), input("group: "))
    )
    conn.commit()
    print("moved")


# ---------- FILTER GROUP ----------
def filter_group():
    g = input("group: ")

    cur.execute("""
    SELECT c.first_name, c.email, g.name
    FROM contacts c
    JOIN groups g ON g.id = c.group_id
    WHERE g.name = %s
    """, (g,))

    for r in cur.fetchall():
        print(r)


# ---------- SEARCH ----------
def search():
    q = input("search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for r in cur.fetchall():
        print(r)


# ---------- SEARCH EMAIL ----------
def search_email():
    e = input("email: ")
    cur.execute(
        "SELECT first_name,email FROM contacts WHERE email ILIKE %s",
        ('%' + e + '%',)
    )
    print(cur.fetchall())


# ---------- SORT ----------
def sort_contacts():
    print("1 name 2 birthday 3 date")
    ch = input(">> ")

    field = "first_name"
    if ch == "2":
        field = "birthday"
    elif ch == "3":
        field = "created_at"

    cur.execute(f"""
    SELECT first_name,email,birthday
    FROM contacts
    ORDER BY {field}
    """)

    for r in cur.fetchall():
        print(r)


# ---------- PAGINATION ----------
def pagination():
    page = 0

    while True:
        cur.execute(
            "SELECT first_name,email FROM contacts LIMIT 5 OFFSET %s",
            (page * 5,)
        )

        print("\nPAGE", page + 1)
        print(cur.fetchall())

        cmd = input("n-next p-prev q-quit: ")

        if cmd == "n":
            page += 1
        elif cmd == "p" and page > 0:
            page -= 1
        else:
            break


# ---------- EXPORT JSON ----------
def export_json():
    cur.execute("""
    SELECT c.id,c.first_name,c.email,g.name
    FROM contacts c
    LEFT JOIN groups g ON g.id=c.group_id
    """)
    contacts = cur.fetchall()

    data = []

    for c in contacts:
        cur.execute("SELECT phone,type FROM phones WHERE contact_id=%s",(c[0],))
        phones = cur.fetchall()

        data.append({
            "name": c[1],
            "email": c[2],
            "group": c[3],
            "phones": phones
        })

    with open("contacts.json","w") as f:
        json.dump(data,f,indent=2)

    print("exported")


# ---------- IMPORT JSON ----------
def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    for d in data:
        cur.execute("SELECT id FROM contacts WHERE first_name=%s",(d["name"],))
        ex = cur.fetchone()

        if ex:
            ch = input(f"{d['name']} exists skip/overwrite s/o: ")
            if ch == "s":
                continue
            cid = ex[0]
            cur.execute("DELETE FROM phones WHERE contact_id=%s",(cid,))
        else:
            cur.execute("""
            INSERT INTO contacts(first_name,email)
            VALUES(%s,%s) RETURNING id
            """,(d["name"],d["email"]))
            cid = cur.fetchone()[0]

        for p in d["phones"]:
            cur.execute("""
            INSERT INTO phones(contact_id,phone,type)
            VALUES(%s,%s,%s)
            """,(cid,p[0],p[1]))

    conn.commit()
    print("imported")


# ---------- CSV IMPORT ----------
def import_csv():
    with open("contacts.csv") as f:
        r = csv.DictReader(f)

        for row in r:
            cur.execute("INSERT INTO groups(name) VALUES(%s) ON CONFLICT DO NOTHING",(row["group"],))
            cur.execute("SELECT id FROM groups WHERE name=%s",(row["group"],))
            gid = cur.fetchone()[0]

            cur.execute("""
            INSERT INTO contacts(first_name,email,birthday,group_id)
            VALUES(%s,%s,%s,%s) ON CONFLICT (first_name) DO NOTHING RETURNING id
            """,(row["name"],row["email"],row["birthday"],gid))

            res = cur.fetchone()

            if res:
                cid = res[0]
            else:
                cur.execute("SELECT id FROM contacts WHERE first_name=%s",(row["name"],))
                cid = cur.fetchone()[0]

            cur.execute("""
            INSERT INTO phones(contact_id,phone,type)
            VALUES(%s,%s,%s)
            """,(cid,row["phone"],row["type"]))

    conn.commit()
    print("csv done")


def show_all():
    cur.execute("""
    SELECT 
        c.first_name,
        c.email,
        c.birthday,
        g.name,
        p.phone,
        p.type
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    ORDER BY c.id
    """)

    rows = cur.fetchall()

    for r in rows:
        print(r)


def delete_contact():
    print("1 by name  2 by phone")
    ch = input(">> ")

    if ch == "1":
        name = input("name: ")

        cur.execute("""
        DELETE FROM contacts
        WHERE first_name = %s
        """, (name,))

    elif ch == "2":
        phone = input("phone: ")

        cur.execute("""
        DELETE FROM phones
        WHERE phone = %s
        """, (phone,))

    conn.commit()
    print("deleted")

# ---------- MENU ----------
def menu():
    while True:
        print("""
1 add contact
2 add phone
3 move group
4 filter group
5 search
6 search email
7 sort
8 pagination
9 export json
10 import json
11 import csv
12 show all
13 delete
0 exit
""")

        ch = input(">> ")

        if ch == "1": add_contact()
        elif ch == "2": add_phone()
        elif ch == "3": move_group()
        elif ch == "4": filter_group()
        elif ch == "5": search()
        elif ch == "6": search_email()
        elif ch == "7": sort_contacts()
        elif ch == "8": pagination()
        elif ch == "9": export_json()
        elif ch == "10": import_json()
        elif ch == "11": import_csv()
        elif ch == "12": show_all()
        elif ch == "13": delete_contact()
        elif ch == "0": break


menu()

cur.close()
conn.close()