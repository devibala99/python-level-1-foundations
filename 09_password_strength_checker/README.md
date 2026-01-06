# 🔐 Password Strength Checker (CLI)

## 📌 Project Overview

The **Password Strength Checker** is a command-line based Python application that evaluates the strength of a user-provided password using commonly accepted industry rules.

The application analyzes the password and provides:

- A **strength rating**
- A **score**
- **Actionable feedback** to improve weak passwords

This project focuses on **string handling, condition checks, clean logic design, and real-world validation rules**.

---

## 🎯 Objectives

- Understand how password strength is evaluated in real systems
- Practice string operations and condition-based logic
- Implement a menu-driven CLI application
- Provide user-friendly feedback
- Handle invalid inputs safely

---

## 🧠 Concepts Used

- Strings and character inspection
- Conditional statements
- Loops
- Functions
- Python standard library (`string`)
- Input validation
- Exception handling (`try / except`)

---

## ⚙️ Features

- Menu-driven interface
- Checks minimum password length
- Validates presence of:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- Strength scoring system (0–5)
- Clear improvement suggestions
- Safe exit option

---

## 📋 Menu Options

1. Check Password Strength
2. Exit

---

## 🔍 Password Evaluation Rules

| Rule              | Description                     |
| ----------------- | ------------------------------- |
| Length            | Minimum 8 characters            |
| Uppercase         | At least one A–Z                |
| Lowercase         | At least one a–z                |
| Digit             | At least one 0–9                |
| Special Character | At least one symbol (!@#$ etc.) |

---

## 🧪 Strength Levels

| Score | Strength  |
| ----- | --------- |
| 0–2   | ❌ Weak   |
| 3–4   | ⚠️ Medium |
| 5     | ✅ Strong |

---

## 📌 Sample Input

Enter password to check: Dev@1234

## 📌 Sample Output

🔎 Password Analysis
Strength : ✅ Strong
Score : 5/5

---

## ▶️ How to Run

Ensure Python is installed, then run:

```bash
python main.py

## Folder Structure
09-password-strength-checker/
│
├── main.py
└── README.md

🔮 Future Improvements

-- Password blacklist check
-- Regex-based validation
-- Password entropy calculation
-- GUI version
-- File-based password analysis

✅ Status

✔ Completed
✔ Tested
✔ Industry-standard logic
✔ GitHub-ready

```
