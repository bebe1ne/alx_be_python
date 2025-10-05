class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")
        elif amount > self.account_balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

# class BankAcount:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: ${amount:.2f}")
#         elif amount > self.balance:
#             print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def get_balance(self):
#         return self.balance

#     def __str__(self):
#         return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"