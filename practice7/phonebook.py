from connect import connect
import csv


def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def update_contact(name, new_phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()


def delete_contact(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()


def search_contacts(keyword):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s OR phone LIKE %s",
        (f"%{keyword}%", f"%{keyword}%")
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    while True:
        print("\n1. Add")
        print("2. Show")
        print("3. Update")
        print("4. Delete")
        print("5. Search")
        print("6. Load from CSV")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            get_contacts()

        elif choice == "3":
            name = input("Name: ")
            phone = input("New phone: ")
            update_contact(name, phone)

        elif choice == "4":
            name = input("Name: ")
            delete_contact(name)

        elif choice == "5":
            keyword = input("Enter name or phone: ")
            search_contacts(keyword)

        elif choice == "6":
            insert_from_csv("contacts.csv")

        elif choice == "7":
            break