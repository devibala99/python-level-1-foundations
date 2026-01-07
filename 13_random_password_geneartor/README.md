# 🔐 Random Password Generator (CLI)

## 📌 Project Overview

This is a **command-line based Random Password Generator** built using Python.

The application allows users to generate secure passwords based on:

- Desired password length
- Selected password strength (Weak / Medium / Strong)

This project focuses on **input validation, randomness, modular functions, and menu-driven CLI design**, which are essential skills for real-world Python development.

---

## 🎯 Objectives

- Understand random data generation
- Learn how to use Python standard libraries (`random`, `string`)
- Build a menu-driven CLI application
- Practice clean function-based design
- Handle invalid inputs safely
- Generate secure passwords programmatically

---

## 🧠 Concepts Used

- Functions
- Loops (`while`)
- Conditional statements
- Input validation
- Exception handling (`try / except`)
- Python standard libraries:
  - `random`
  - `string`
- Guard clauses (early returns)
- Program entry point (`if __name__ == "__main__"`)

---

## ⚙️ Features

- Menu-driven command-line interface
- Generate password by custom length
- Generate password by strength level
- Weak / Medium / Strong password modes
- Uses letters, digits, and special characters
- Input validation for all user inputs
- Clean exit option
- Fully beginner-friendly and readable code

---

## 🔐 Password Strength Rules

### 1️⃣ Weak

- Only lowercase letters
- Fixed length: 6 characters

### 2️⃣ Medium

- Uppercase + lowercase letters + digits
- Fixed length: 8 characters

### 3️⃣ Strong

- Uppercase + lowercase letters + digits + symbols
- Fixed length: 12 characters

---

## 📋 Menu Options

1. Generate password by length
2. Generate password by strength
3. Exit

---

## 🧪 Sample Flow

**Input**
Choose an option (1-3): 2
Choose Strength:

1. Weak
2. Medium
3. Strong
   Enter strength (1-3): 3

**Output**
✅ Generated Password: A@9k!Pz#2Xq$

---

## 📂 Folder Structure

13_random_password_generator/
│
├── main.py
└── README.md

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py

🚫 Validation Handled

-- Non-numeric input
-- Invalid menu choices
-- Invalid strength selection
-- Password length less than minimum requirement
-- Safe exit handling

🔮 Future Improvements

-- Copy password to clipboard
-- User-defined strength rules
-- Save generated passwords securely
-- GUI version
-- Password strength score meter

✅ Project Status

✔ Completed
✔ Tested
✔ Beginner-friendly
✔ GitHub-ready
✔ Industry-aligned
```
