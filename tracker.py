expenses = []

while True:
    print("1) Add Expenses")
    print("2) List Expenses")
    print("3) Show Total Expenses")
    print("4) Quit")

    choice = input("> ")

    if choice == "1":
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        expense = {"amount": amount, "category": category}
        expenses.append(expense)
        print("Added expense:", expense)
    elif choice == "2":
        for item in expenses:
            print(item["amount"], "-", item["category"])
    elif choice == "3":
        total = 0
        for item in expenses:
            total+=item["amount"]
        print("Total: ", total)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")