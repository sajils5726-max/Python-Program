class Customer:
    "Common base class for all Customers"

    def getData(self, name, accno, acctype, balance):
        self.name = name
        self.accno = accno
        self.acctype = acctype
        self.balance = balance

    def displayCustomer(self):
        print("Customer Name:", self.name)
        print("Account Number:", self.accno)
        print("Account Type:", self.acctype)
        print("Balance Amount:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)


# ----- Main Program -----
ch = 0
obj = None  # To store customer object

while ch != 5:
    print("\n*------ Menu ------*")
    print("1. New Customer")   
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Display")
    print("5. Exit")     

    ch = int(input("Enter your choice (1/2/3/4/5): "))

    if ch == 1:
        obj = Customer()
        n = input("Enter Name: ")
        no = int(input("Enter Account Number: "))
        t = input("Enter Account Type (SB/C): ")
        b = int(input("Enter the Amount: "))
        obj.getData(n, no, t, b)

    elif ch == 2:
        if obj:
            amt = int(input("Enter the amount to be deposited: "))
            obj.deposit(amt)
        else:
            print("Please create a customer first (option 1).")

    elif ch == 3:
        if obj:
            amt = int(input("Enter the amount to be withdrawn: "))
            obj.withdrawal(amt)
        else:
            print("Please create a customer first (option 1).")

    elif ch == 4:
        if obj:
            obj.displayCustomer()
        else:
            print("Please create a customer first (option 1).")

    elif ch == 5:
        print("Exiting Bank Account. Goodbye!")
    else:
        print("Invalid choice! Please try again.")
     
