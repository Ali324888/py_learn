import datetime
import json


class Expense:
    def __init__(self,name,amount,category):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = datetime.date.today()

    def show_details(self):
        print("Name: ",self.name)
        print("Amount: ",self.amount)
        print("Name: ",self.category)
        print("Date: ",self.date)


def save_expenses():

    data = []

    for expense in expenses:
        data.append({
            "name": expense.name,
            "amount": expense.amount,
            "category": expense.category,
            "date": str(expense.date)
        })

    with open("expenses.json", "w") as file:
        json.dump(data,file,indent=4)



def load_expenses():

    try:

        with open("expenses.json", "r") as file:
            data = json.load(file)

        loaded_expenses = []

        for item in data:

            expense = Expense(
                item["name"],
                item["amount"],
                item["category"]
            )

            loaded_expenses.append(expense)

        return loaded_expenses

    except FileNotFoundError:

        return []


expenses = load_expenses()

def add_expense():
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Please enter valid value")
        return

    category = input("Enter expense category: ")

    expense = Expense(name, amount, category)

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expense found!")
        return

    for expense in expenses:
        print("==================")
        print("Name: ", expense.name)
        print("Amount: ", expense.amount)
        print("Category: ", expense.category)
        print("Date: ", expense.date)

def show_total():
    if len(expenses) == 0:
        print("No expense found!")
        return

    total = 0

    for expense in expenses:
        total = total + expense.amount

    print("Total: ", total)


def search_category():
    category = input("Enter expense category: ")

    for expense in expenses:
        if category.lower() == expense.category.lower():
            print("==================")
            print("Name: ", expense.name)
            print("Amount: ", expense.amount)
            print("Category: ", expense.category)
            print("Date: ", expense.date)

    print("No expenses found in this category!")


def delete_expense():
    name = input("Enter expense name: ")

    for expense in expenses:
        if name.lower() == expense.name.lower():
            expenses.remove(expense)
            save_expenses()
            print("Expense deleted successfully!")
            return

    print("Expense not found!")



while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Show Total Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_category()

    elif choice == "4":
        show_total()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
    