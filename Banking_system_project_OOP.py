
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_details(self):
        return {
            'Name': self.name,
            'Address': self.address,
            'Phone': self.phone
        }

''''
account class creation
-account_number,balance,owner
-method: deposit(amount), withdraw(amount), get_balance(), show_account_details()
'''

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, owner):
        self._account_number = account_number
        self._balance = 0.0
        self._owner = owner
        self._transactions = []

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(('Deposit', amount))
        else:
            raise ValueError("Amount must be greater than 0")

    def get_balance(self):
        return self._balance

    def show_account_details(self):
        return {
            'Account Number': self._account_number,
            'Owner': self._owner.name,
            'Balance': self._balance
        }
class Customer(Person):
    def __init__(self, name, address, phone):
        super().__init__(name, address, phone)
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_number):
        self.accounts = [acc for acc in self.accounts if acc._account_number != account_number]

    def get_accounts_summary(self):
        return [acc.show_account_details() for acc in self.accounts]


class Admin(Person):
    def __init__(self, name, address, phone, employee_id):
        super().__init__(name, address, phone)
        self.employee_id = employee_id

    def approve_account(self, customer, account):
        customer.add_account(account)

    def view_all_customers(self, customers):
        return [cust.get_details() for cust in customers]
class SavingsAccount(Account):
    def __init__(self, account_number, owner, interest_rate):
        super().__init__(account_number, owner)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append(('Withdrawal', amount))
        else:
            raise ValueError("Insufficient balance")

    def apply_interest(self):
        interest = self._balance * self.interest_rate / 100
        self._balance += interest
        self._transactions.append(('Interest Applied', interest))
class BusinessAccount(Account):
    def __init__(self, account_number, owner, overdraft_limit):
        super().__init__(account_number, owner)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            self._transactions.append(('Withdrawal', amount))
        else:
            raise ValueError("Overdraft limit exceeded")
from datetime import datetime
import uuid

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_id = str(uuid.uuid4())
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now()

    def get_transaction_details(self):
        return {
            'Transaction ID': self.transaction_id,
            'Type': self.transaction_type,
            'Amount': self.amount,
            'Date': self.date.strftime("%Y-%m-%d %H:%M:%S")
        }
class Bank:
    def __init__(self):
        self.customers = []
        self.admins = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_admin(self, admin):
        self.admins.append(admin)

    def create_customer_account(self, customer, account):
        customer.add_account(account)

    def delete_customer_account(self, customer, account_number):
        customer.remove_account(account_number)

    def view_transaction_history(self, account):
        return account._transactions

    def find_customer_by_account(self, account_number):
        for customer in self.customers:
            for account in customer.accounts:
                if account._account_number == account_number:
                    return customer
        return None


def main():
    bank = Bank()
    
    # Create a default admin
    admin = Admin("Alice", "123 Bank St", "1234567890", "ADM001")
    bank.add_admin(admin)

    while True:
        print("\n--- Welcome to Python Bank ---")
        print("1. Create Customer")
        print("2. Open Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Show Balance")
        print("6. Apply Interest (Savings Only)")
        print("7. View Transaction History")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            customer = Customer(name, address, phone)
            bank.add_customer(customer)
            print("Customer created successfully!")

        elif choice == "2":
            name = input("Enter customer name to open account: ")
            acc_type = input("Account type (savings/business): ").lower()
            account_number = input("Enter new account number: ")

            # Find the customer
            customer = next((c for c in bank.customers if c.name == name), None)
            if customer:
                if acc_type == "savings":
                    rate = float(input("Enter interest rate: "))
                    acc = SavingsAccount(account_number, customer, rate)
                elif acc_type == "business":
                    limit = float(input("Enter overdraft limit: "))
                    acc = BusinessAccount(account_number, customer, limit)
                else:
                    print("Invalid account type.")
                    continue
                admin.approve_account(customer, acc)
                print("Account opened successfully!")
            else:
                print("Customer not found.")

        elif choice == "3":
            acc_num = input("Enter account number to deposit: ")
            amount = float(input("Enter amount to deposit: "))
            customer = bank.find_customer_by_account(acc_num)
            if customer:
                acc = next(a for a in customer.accounts if a._account_number == acc_num)
                acc.deposit(amount)
                print("Amount deposited successfully!")
            else:
                print("Account not found.")

        elif choice == "4":
            acc_num = input("Enter account number to withdraw from: ")
            amount = float(input("Enter amount to withdraw: "))
            customer = bank.find_customer_by_account(acc_num)
            if customer:
                acc = next(a for a in customer.accounts if a._account_number == acc_num)
                try:
                    acc.withdraw(amount)
                    print("Amount withdrawn successfully!")
                except Exception as e:
                    print("Error:", e)
            else:
                print("Account not found.")

        elif choice == "5":
            acc_num = input("Enter account number: ")
            customer = bank.find_customer_by_account(acc_num)
            if customer:
                acc = next(a for a in customer.accounts if a._account_number == acc_num)
                print("Balance:", acc.get_balance())
            else:
                print("Account not found.")

        elif choice == "6":
            acc_num = input("Enter savings account number: ")
            customer = bank.find_customer_by_account(acc_num)
            if customer:
                acc = next((a for a in customer.accounts if a._account_number == acc_num), None)
                if isinstance(acc, SavingsAccount):
                    acc.apply_interest()
                    print("Interest applied.")
                else:
                    print("This is not a savings account.")
            else:
                print("Account not found.")

        elif choice == "7":
            acc_num = input("Enter account number: ")
            customer = bank.find_customer_by_account(acc_num)
            if customer:
                acc = next(a for a in customer.accounts if a._account_number == acc_num)
                for t in acc._transactions:
                    print(t)
            else:
                print("Account not found.")

        elif choice == "8":
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
