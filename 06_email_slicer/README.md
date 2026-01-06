# 📧 Email Slicer (CLI)

## 📌 Project Overview

The **Email Slicer** is a command-line Python application that validates an email address and extracts its core components:

- Username
- Domain name
- Domain extension

This project simulates **real-world string validation and parsing**, similar to what is used in login systems, user registration flows, and data pipelines.

---

## 🎯 Objectives

- Practice string manipulation in Python
- Implement real-world input validation rules
- Build a menu-driven CLI application
- Separate validation logic from processing logic
- Handle invalid inputs gracefully

---

## 🧠 Concepts Used

- String methods (`split`, `rsplit`, `count`, `startswith`, `endswith`, `lower`)
- Conditional statements
- Functions
- Loops (`while`)
- Input validation
- Exception handling (`try / except`)

---

## ⚙️ Features

- Menu-driven command-line interface
- Email format validation before processing
- Supports multi-level domains (e.g. `.edu.in`, `.co.uk`)
- Converts input to lowercase for consistency
- Clear and readable output
- Safe exit option

---

## 📋 Menu Options

1. Slice Email
2. Exit

---

## 🧪 Email Validation Rules

An email is considered **valid** if:

- It is not empty
- It contains **exactly one `@`**
- It does not start or end with `@`
- The username part is not empty
- The domain contains at least one `.`
- The domain does not start or end with `.`
- The domain extension length is **at least 2 characters**

✔ Valid examples:
user@gmail.com

deva@srmist.edu.in

admin@company.co.uk

❌ Invalid examples:

@gmail.com
user@
user@.com

user@domain
user@domain

---

## ▶️ How to Run

Ensure Python is installed, then run:

```bash
python main.py

## Sample Input
deva@abcist.edu.in

## Sample Output
✅ Email Details
Username   : deva
Domain     : abcist.edu
Extension  : in

## Folder Structure
06-email-slicer/
│
├── main.py
└── README.md

##🔮 Future Improvements
-- Optional regex-based validation
-- Bulk email slicing from file
-- GUI version
-- Email domain analytics

✅ Project Status
✔ Completed
✔ Tested
✔ Industry-aligned
✔ GitHub-ready
```
