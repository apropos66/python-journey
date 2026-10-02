# expense tracking python project(first time in python

expenses = [] # list that holds all the expenses
while True:
    print("")
    print("1.Add an expense")
    print("2.See all expenses")
    print("3.Quit")
    choice = input("Choose: ")
    if choice == "1":
        item = input("What did you buy? ")
        amount = float(input("Cost?" ))

        expense = {"item": item, "amount": amount}
        expenses.append(expense)
        print("Added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet")

        else:
            print()
            print("Expenses:")
            for e in expenses:
                print(f"  -{e['item']} : {e['amount']}")

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Are you dumb or sth??")


