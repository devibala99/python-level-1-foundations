# 🏧 Simple ATM System (CLI)

## 📌 Project Overview

This is a **command-line based Simple ATM System** built using Python.

The application simulates a real-world ATM workflow including:

- Secure PIN authentication
- Balance inquiry
- Deposit and withdrawal operations
- Transaction history tracking
- Safe exit handling

This project focuses on **state management, validation, and menu-driven application design**, which are essential for real software systems.

---

## 🎯 Objectives

- Understand how state (balance, transactions) is managed
- Build a secure menu-driven CLI application
- Handle invalid input safely
- Simulate real-world ATM behavior
- Practice clean and modular Python functions

---

## 🧠 Concepts Used

- Functions
- Loops (`while`)
- Conditional statements
- Input validation
- Exception handling (`try / except`)
- Lists for transaction logs
- Guard clauses (early returns)
- Program entry point (`if __name__ == "__main__"`)

---

## ⚙️ Features

- PIN-based authentication (limited attempts)
- Balance check
- Deposit money
- Withdraw money
- Transaction history
- Input validation for all operations
- Clean exit option
- Prevents overdraft and invalid transactions

---

## 🔐 Security Rules

- Maximum **3 PIN attempts**
- Card is blocked after repeated failures
- PIN must match exactly
- No negative or zero transactions allowed

---

## 📋 Menu Options

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit

---

## 🧪 Sample Flow

### Input

Enter PIN: 1234
Choose option: 2
Enter amount: 500

### Output

✅ ₹500 deposited successfully.
💰 Current Balance: ₹10500

---

## 📂 Folder Structure

10_simple_atm_system/
│
├── main.py
└── README.md

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py

---------------------------------------

🚫 Validation Handled

-- Invalid PIN
-- Non-numeric input
-- Insufficient balance
-- Negative or zero deposit / withdrawal
-- Invalid menu choice

🔮 Future Improvements

-- Persistent storage (file/database)
-- Daily withdrawal limits
-- Multiple user accounts
-- PIN change feature
-- Admin mode

✅ Project Status

✔ Completed
✔ Tested
✔ GitHub-ready
✔ Industry-aligned
```
