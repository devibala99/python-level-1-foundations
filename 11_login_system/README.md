# 🔐 Login System (Hardcoded) — CLI

## 📌 Project Overview

This is a **command-line based Login System** built using Python using **hardcoded user credentials**.

The application simulates a real authentication flow including:

- Username and password validation
- Limited login attempts
- Account lockout after repeated failures
- User session handling with logout option

This project focuses on **authentication logic, state handling, validation, and clean control flow**, which are core concepts in real-world software systems.

---

## 🎯 Objectives

- Understand basic authentication workflows
- Implement username and password validation
- Handle failed login attempts securely
- Simulate account lockout logic
- Practice clean, modular Python functions

---

## 🧠 Concepts Used

- Dictionaries
- Functions
- Loops (`while`)
- Conditional statements
- Input validation
- Exception handling (`try / except`)
- Guard clauses
- Program entry point (`if __name__ == "__main__"`)

---

## ⚙️ Features

- Hardcoded user credentials
- Secure login with limited attempts
- Account lockout after 3 failed attempts
- Menu-driven user session
- Logout functionality
- Clean exit handling
- Safe input validation

---

## 🔐 Security Rules

- Maximum **3 login attempts**
- Account locked after repeated failures
- Empty credentials are rejected
- Only valid username/password combinations allowed

---

## 📋 Menu Options (After Login)

1. View Profile
2. Logout

---

## 🧪 Sample Flow

### Input

Username: admin
Password: admin123

### Output

✅ Login successful. Welcome, admin!

--- User Menu ---

1. View Profile
2. Logout

---

## 📂 Folder Structure

11_login_system/
│
├── main.py
└── README.md

---

## ▶️ How to Run

Ensure Python is installed, then run:

```bash
python main.py

🚫 Validation Handled

-- Invalid username or password
-- Empty username or password
-- Exceeded login attempts
-- Invalid menu choices
-- Non-numeric menu input

🔮 Future Improvements

-- Password hashing
-- File or database-based users
-- Role-based access control
-- Password reset feature
-- Session timeout

✅ Project Status

✔ Completed
✔ Tested
✔ GitHub-ready
✔ Industry-aligned
```
