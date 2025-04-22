def add_expense(expenses):
    categories = {
        1: "Food",
        2: "Rent",
        3: "Transport",
        4: "Entertainment",
        5: "Utilities",
        6: "Other"
    }
    print("\nChoose a category:")
    for key, value in categories.items():
        print(f"{key}. {value}")

    try:
        category_num = int(input("Enter category number: "))
        category = categories.get(category_num, "Other")
        amount = float(input("Enter amount spent: $"))
        date = input("Enter date (YYYY-MM-DD): ")
        note = input("Optional note (e.g., Starbucks, Uber): ")
        expenses.append({"category": category, "amount": amount, "date": date, "note": note})
        print("Expense added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter valid numbers.\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    total = 0
    print("\n--- Personal Expense Summary ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} - ${exp['amount']:.2f} | {exp['note']}")
        total += exp['amount']
    print(f"Total Expenses: ${total:.2f}\n")

def export_to_txt(expenses):
    try:
        with open("personal_expenses.txt", "w") as file:
            file.write("--- Personal Expense Summary ---\n")
            total = 0
            for i, exp in enumerate(expenses, start=1):
                file.write(f"{i}. {exp['date']} | {exp['category']} - ${exp['amount']:.2f} | {exp['note']}\n")
                total += exp['amount']
            file.write(f"\nTotal Expenses: ${total:.2f}\n")
        print("Expenses exported to 'personal_expenses.txt' successfully.\n")
    except IOError:
        print("Error: Unable to write to file.\n")

def main():
    expenses = []
    while True:
        print("--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Export to TXT")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            export_to_txt(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
