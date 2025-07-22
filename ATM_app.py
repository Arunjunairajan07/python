class ATM:
    def __init__(self, bal=1000):
        self.bal = bal

    def check_bal(self):
        return f"Your account bal is ${self.bal}"

    def deposit_amt(self, amt):
        self.bal += amt
        return f"Deposited ${amt}. Your new bal is ${self.bal}"

    def withdraw_amt(self, amt):
        if self.bal >= amt:
            self.bal -= amt
            return f"Withdraw ${amt}. Your new bal is ${self.bal}"
        else:
            return "Insufficient funds. Withdraw failed."

atm = ATM()
while True:
    print("1. Check Bal")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print(atm.check_bal())
    elif choice == '2':
        amt = float(input("Enter the deposit amt: "))
        print(atm.deposit_amt(amt))
    elif choice == '3':
        amt = float(input("Enter the withdraw amt: "))
        print(atm.withdraw_amt(amt))
    elif choice == '4':
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid choice. Please select a valid option.")
