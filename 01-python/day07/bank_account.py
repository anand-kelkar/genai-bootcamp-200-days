# program to maintain bank account and it's operations like deposit , withdraw and display account balance
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        print(type(self.balance))

    def deposit(self, amount):
        self.__balance += amount
        self.display_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            self.display_balance()       

    def display_balance(self):
            print(f"Your account balance is : {self.balance}")

    @property
    def balance(self):
        return self.__balance
    
continue_banking = True
bank_account = BankAccount(1000.00) # default bank account balance is 1000
while continue_banking:
     customer_input = input("Hello! what do you want to do today ,enter DEPOSIT/WITHDRAW/BALANCE/EXIT : ")
     match customer_input.upper():        
        case "DEPOSIT":
            deposit_amount = float(input("Enter Amount to Deposit :"))
            bank_account.deposite(deposit_amount)
        case "WITHDRAW":
            withdraw_amount = float(input("Enter Amount to withdraw :"))
            bank_account.withdraw(withdraw_amount)
        case "BALANCE":            
            bank_account.display_balance()
        case "EXIT":            
            continue_banking = False
        case _:
            pass
     
