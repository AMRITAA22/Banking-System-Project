# 🏦 Banking System Project (OOP in Python)

A simple yet powerful command-line based banking system developed in Python. This project simulates real-world banking operations while demonstrating the full application of Object-Oriented Programming (OOP) principles such as **Abstraction**, **Encapsulation**, **Inheritance**, and **Polymorphism**.

## 📋 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [OOP Concepts Implemented](#-oop-concepts-implemented)
- [Project Structure](#-project-structure)
- [Class Overview](#-class-overview)
- [How to Run](#-how-to-run)
- [Sample Output](#-sample-output)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## 🚀 Features

- Create Customer and Admin profiles
- Open and manage different types of accounts:
  - Savings Account (with interest feature)
  - Business Account (with overdraft capability)
- Perform banking operations:
  - Deposit
  - Withdrawal
  - Balance Inquiry
  - Apply Interest (for savings accounts)
- View transaction history with timestamps
- Admin approval for account creation
- Admin can view customer details
- Robust error handling and data validation

## 🛠️ Technologies Used

- **Python 3.x**
- Built-in Modules:
  - `uuid`: Unique transaction IDs
  - `datetime`: Timestamp generation
  - `abc`: Abstract base classes

## 🧠 OOP Concepts Implemented

| Concept        | Implementation                                  |
|----------------|--------------------------------------------------|
| **Abstraction** | Abstract `Account` base class using `abc`       |
| **Encapsulation** | Protected attributes like `_balance`, `_transactions` |
| **Inheritance** | `SavingsAccount` and `BusinessAccount` extend `Account` |
| **Polymorphism** | Overridden `withdraw()` method in child classes |

## 📂 Project Structure

```plaintext
banking-system-oop/
├── Banking_system_project_OOP.py   # Main application file
├── README.md                       # Project documentation
```

## 📜 Class Overview

### 🔹 Person
- Attributes: `name`, `address`, `phone`
- Method: `get_details()`

### 🔹 Customer (inherits Person)
- Can open, view, and remove accounts
- Holds a list of `Account` objects

### 🔹 Admin (inherits Person)
- Approves accounts for customers
- Views all customer profiles

### 🔹 Account (Abstract Base Class)
- Attributes: `account_number`, `_balance`, `_owner`, `_transactions`
- Methods: `deposit()`, `withdraw()` (abstract), `get_balance()`, `show_account_details()`

### 🔹 SavingsAccount (inherits Account)
- Additional attribute: `interest_rate`
- Method: `apply_interest()`

### 🔹 BusinessAccount (inherits Account)
- Additional attribute: `overdraft_limit`

### 🔹 Transaction
- Attributes: `transaction_id`, `transaction_type`, `amount`, `date`
- Method: `get_transaction_details()`

### 🔹 Bank
- Manages lists of `Customer` and `Admin`
- Handles account creation, deletion, and transactions

## 📦 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/banking-system-oop.git
   cd banking-system-oop
   ```

2. Run the Python file:
   ```bash
   python Banking_system_project_OOP.py
   ```

3. Follow the interactive menu to perform banking operations.

## 📸 Sample Output

```plaintext
--- Welcome to Python Bank ---
1. Create Customer
2. Open Account
3. Deposit
4. Withdraw
5. Show Balance
6. Apply Interest (Savings Only)
7. View Transaction History
8. Exit
```

## 📈 Future Improvements

- Add persistent database (e.g., SQLite, MongoDB)
- Implement login system for customers and admins
- Build GUI with Tkinter or a web interface with Flask/Django
- Add support for fund transfers between accounts
- Export transaction history as CSV or PDF

## 👩‍💼 Author

**Amrita**  
Passionate developer and enthusiastic learner.  
Feel free to connect for ideas or feedback!


