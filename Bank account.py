class BankAccount:
    def __init__(self, member, acc_no, name, account_type, balance=0.0):
        self.member = member
        self.acc_no = acc_no
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        """Display account details."""
        print("\n--- Account Details ---")
        print(f"Member ID     : {self.member}")
        print(f"Account No.   : {self.acc_no}")
        print(f"Name          : {self.name}")
        print(f"Account Type  : {self.account_type}")
        print(f"Balance       : ₹{self.balance:.2f}")
        print("-----------------------")




member = input("Enter Member ID: ")
acc_no = int(input("Enter Account Number: "))
name = input("Enter Account Holder Name: ")
account_type = input("Enter Type of Account (Savings/Current): ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(member, acc_no, name, account_type, balance)


while True:
    print("\nChoose an option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Display Account Details")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == '2':
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == '3':
        account.display()
    elif choice == '4':
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Please select again.")