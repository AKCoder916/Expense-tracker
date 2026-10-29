expenses = []

while True:
    print("1) Add Expenses")
    print("2) List Expenses")
    print("3) Quit")

    choice = input("> ")

    if choice == "1":
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        expense = {"amount": amount, "category": category}
        expenses.append(expense)
        print("Added expense:", expense)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Not built yet!")