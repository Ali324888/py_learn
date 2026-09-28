class BankAccount:
    next_account_number = 1001

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    @staticmethod
    def is_valid_balance(balance):
        return balance >= 0

    @classmethod
    def create_account(cls, name):
        return cls(name, 0)

    

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else: 
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else: 
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def show_balance(self):
        print("Balance: ", self.__balance)
    

    def __str__(self):
        return f"Account Holder: {self.name}, Balance: {self.__balance}"

    def __eq__(self, other):
        return self.account_number == other.account_number
    

class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate/100
        self.deposit(interest)

    def withdraw(self, amount):
        if self.get_balance() - amount < 500:
            print("Minimum balance of ₹500 required")
        else:
            super().withdraw(amount)



account1 = BankAccount("Adil", 10000)

account1.deposit(5000)
account1.withdraw(3000)

print(account1)
print(account1.get_balance())

account2 = BankAccount.create_account("Zee")
account2.deposit(20000)

print(account2)

savings = SavingsAccount("Rahul", 10000, 5)

savings.add_interest()
print(savings)

savings.withdraw(9700)

print(savings)
