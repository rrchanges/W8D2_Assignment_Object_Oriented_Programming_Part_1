class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Current Balance: ${self.__balance}")

# Main program
if __name__ == "__main__":
    account1 = BankAccount("12345", "Alice", 1000)
    account2 = BankAccount("67890", "Bob", 2000)

    account1.deposit(500)
    account1.withdraw(200)
    account1.display_account_info()

    account2.withdraw(2500)
    account2.deposit(100)
    account2.display_account_info()