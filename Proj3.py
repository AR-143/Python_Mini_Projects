bank = 0

while True:
    print("1.Enter Amount \n2.Check Balance \n3.Withdraw Money \n4.Exit")

    amount = int(input("Choose any Option: "))

    if amount == 1:
        amount = int(input("Enter a amount: "))
        bank += amount
        print(f"{amount} is credited.")
        if amount == 1:
            pass

    elif amount == 2:
        amount = bank
        print(f"Rs.{amount} is availabe.")

    elif amount == 3:
        amount = int(input("Amount withdrawl: "))
        if amount > bank:
            print("Insufficient balance")
        else:
            bank -= amount
            print(f"You withdraw amount is Rs.{amount}.")

    elif amount == 4:
        print("Thank you!")
        break