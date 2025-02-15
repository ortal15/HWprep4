def create_table():
    import os
    import sqlite3

    if os.path.exists("prep4.db"):
        os.remove("prep4.db")
    else:
        print("The file does not exist")
    conn = sqlite3.connect('prep4.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE garage (
    fix_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_number TEXT UNIQUE NOT NULL,
    car_problem TEXT NOT NULL,
    fixed BOOLEAN DEFAULT FALSE,
    owner_ph TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()


def insert_into():
    import sqlite3

    conn = sqlite3.connect('prep4.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
    VALUES 
    ('23', 'Engine overheating after long drives', TRUE, '555-1023');
    ''')
    cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
    VALUES 
    ('34', 'Brake pads worn out, needs replacement', TRUE, '555-1034');''')
    cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
    VALUES 
    ('30', 'Check engine light on, possible sensor issue', TRUE, '555-1030');''')
    cursor.execute('''INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
    VALUES 
    ('24', 'Battery drains overnight, needs diagnosis', FALSE, '555-1024');
    ''')
    cursor.execute('''
    INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
    VALUES 
    ('3', 'Strange noise from suspension when turning', FALSE, '555-1003');''')
    conn.commit()
    conn.close()


def option_1():
    import sqlite3

    conn = sqlite3.connect('prep4.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    '''הצג למשתמש את התפריט הבא:
    o אופציה :1 הכנס רכב חדש לטיפול-
    קלוט מספר רישוי של הרכב, בעיה, מס' ט לפון:
    הוסף באמצעות INSERT דרך הפייטון רשומה חדשה עם הפרטים
    עבור רכב הנכנס למוסך ה- fixed הוא 0'''
    car_number = input("Enter the license number of the car: ")
    car_problem = input("Enter the car's problem: ")
    owner_ph = input("Enter the car owner's phone number: ")
    cursor.execute("""
        INSERT INTO garage (car_number, car_problem, fixed, owner_ph)
        VALUES (?, ?, 0, ?)
    """, (car_number, car_problem, owner_ph))
    conn.commit()


def option_2():
    import sqlite3

    conn = sqlite3.connect('prep4.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    car_number = input("Enter the license number of the car: ")

    cursor.execute("SELECT * FROM garage WHERE car_number = ?", (car_number,))
    car = cursor.fetchone()

    if car is None:
        print("The car is not in the garage.")
    elif car[3] == 1:
        print("The treatment is already over.")
    else:
        cursor.execute("UPDATE garage SET fixed = 1 WHERE car_number = ?", (car_number,))
        conn.commit()


def option_3():
    import sqlite3

    conn = sqlite3.connect('prep4.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    car_number = input("Enter the license number of the car: ")

    cursor.execute("SELECT * FROM garage WHERE car_number = ?", (car_number,))
    car = cursor.fetchone()

    if car is None:
        print("The car is not in the garage.")
    elif car[3] == 0:
        print("The treatment is not over yet.")
    else:
        cursor.execute("DELETE FROM garage WHERE car_number = ?", (car_number,))
        conn.commit()


def option_4():
    import sqlite3

    conn = sqlite3.connect('prep4.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM garage WHERE fixed = 0")
    count = cursor.fetchone()[0]
    print(f"The number of cars waiting to be serviced at the garage:{count}")


def menu():
    while True:
        print("\nSelect an option:")
        print("1.Put in a new car for service")
        print("2.End of treatment")
        print("3. Taking the car out of the garage")
        print("4.Treatment load test")
        print("5. exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            option_3()
        elif choice == '4':
            option_4()
        elif choice == '5':
            print("Exit plan.")
            break
        else:
            print("Invalid selection, please try again.")
