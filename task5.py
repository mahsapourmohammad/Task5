import os
import sqlite3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def connect_to_db():
    conn = sqlite3.connect("expenses.db")
    return conn.cursor()

def create_expenses_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT)
    ''')

def add_expense(cursor, date, category, amount, description):
    cursor.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)", 
        (date, category, amount, description)
    )
    print("Expense added successfully.")

def view_expenses(cursor):
    cursor.execute("SELECT * FROM expenses")
    for expense in cursor.fetchall():
        print(expense)

def update_expense(cursor, id, new_date, new_category, new_amount, new_description):
    cursor.execute(
        "UPDATE expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?", 
        (new_date, new_category, new_amount, new_description, id)
    )
    print("Expense updated.")

def remove_expense(cursor, id):
    cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
    print("Expense removed.")

def main():
    clear_screen()

    cursor = connect_to_db()
    create_expenses_table(cursor)

    while True:
        print('''
            1. Add expense
            2. View expenses
            3. Update expense
            4. Remove expense
            5. Exit
        ''')

        choice = input("Please enter your choice: ")

        if choice == '1':
            date = input("Please enter date: ")
            category = input('Please enter category: ')
            amount = float(input("Please enter amount: "))
            description = input("Please enter description: ")
            add_expense(cursor, date, category, amount, description)

        elif choice == '2':
            view_expenses(cursor)

        elif choice == '3':
            id = int(input("Enter expense id: "))
            new_date = input("Please enter new date: ")
            new_category = input("Please enter new category: ")
            new_amount = float(input("Please enter new amount: "))
            new_description = input("Please enter new description: ")
            update_expense(cursor, id, new_date, new_category, new_amount, new_description)

        elif choice == '4':
            id = int(input("Please enter expense id: "))
            remove_expense(cursor, id)

        elif choice == '5':
            print("See you later!")
            break

        else:
            print("Invalid input!")

    cursor.connection.close()

if __name__ == "__main__":
    main()