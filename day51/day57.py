import sqlite3

connection = sqlite3.connect("expenses.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    title TEXT,
    amount REAL,
    category TEXT,
    date TEXT
)
""")

connection.commit()

def add_expense(title, amount, category, date):
    cursor.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?,?,?,?)", (title, amount, category, date))
    connection.commit()

def show_expenses():
    cursor.execute("SELECT * FROM expenses")
    return cursor.fetchall()

def show_expense_by_category(category):
    cursor.execute("SELECT * FROM expenses WHERE category=?",(category,))
    return cursor.fetchall()

def get_total_expenses():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()
    return result[0]

def update_expense(expense_id, amount):
    cursor.execute("UPDATE expenses SET amount=? WHERE id=?", (amount, expense_id))
    connection.commit()

def delete_expense(expense_id):
    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
    connection.commit()

while True:

    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Search by Category")
    print("4. Show Total Expense")
    print("5. Update Expense")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter expense title: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        date = input("Enter expense date(YYYY-MM-DD): ")
        add_expense(title, amount, category, date)
        print("Expense added successfully!")
        pass

    elif choice == "2":
        expenses = show_expenses()
        for expense in expenses:
            print(expense)
        pass

    elif choice == "3":
        category = input("Enter expense category: ")
        expense_by_category = show_expense_by_category(category)
        for expense in expense_by_category:
            print(expense)
        pass

    elif choice == "4":
        total = get_total_expenses()
        print("Total Expenses: ", total)
        pass

    elif choice == "5":
        expense_id = int(input("Enter expense id: "))
        amount = float(input("Enter expense amount: "))
        update_expense(expense_id, amount)
        print("Expense updated successfully!")

        pass

    elif choice == "6":
        expense_id = int(input("Enter expense id: "))
        delete_expense(expense_id)
        print("Expense deleted successfully!")
        pass

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")