# expense tracking python project(first time in python

print("\n \n====Simple Expense Traker====")


def show_menu():
    print()
    print("1.Add an expense")
    print("2.See all expenses")
    print("3.Show total expenses")
    print("4.Delete expense(s)")
    print("5.Quit")


def add_expenses(expenses):
    item = input("What did you buy? ")

    while True:
        try:
            amount = float(input("Cost? "))
            break
        except ValueError:
            print("Enter a number!")

    expense = {"item": item, "amount": amount}

    expenses.append(expense)
    print("Added! What do you want next?")


def show_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses yet.")

    else:
        print()
        print("Expenses:")

        for i, e in enumerate(expenses):
            print(f"  {i + 1}.{e['item']} : {e['amount']:.2f} rupees")


def show_total(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")

    else:
        total = sum(e["amount"] for e in expenses)
        print(f"Total expenses = {total:.2f} rupees")


def delete_expense(expenses):

    if len(expenses) == 0:
        print("Nothing to delete.")

    else:
        for i, e in enumerate(expenses):
            print(f"  {i + 1}.{e['item']} : {e['amount']:.2f} rupees")

        try:
            num = int(input("Enter the number of item to delete: "))
            removed = expenses.pop(num - 1)
            print(f"{removed['item']} removed from the list.")

        except ValueError:
            print("Enter a number.")

        except IndexError:
            print("Enter only availabe number.")


expenses = []  # list that holds all the expenses


def main():
    while True:
        show_menu()
        choice = input("Choose: ")
        print()

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Invalid Input!")


if __name__ == "__main__":
    main()
