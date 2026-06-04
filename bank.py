class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹s{amount} successfully deposited")
        else:
            print(f"Invalid amount: ₹{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Invalid amount: ₹{amount}")
        elif self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully")

    def display(self):
        print("\nAccount Details:\n")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")

#Create an object of bankAccount

account = BankAccount('12345678', 5000)

account.display()

account.deposit(5000)

account.withdraw(1200)

account.display()