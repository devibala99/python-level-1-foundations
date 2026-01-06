# 🔁 Palindrome Checker (CLI)

## 📌 Project Overview

This is a command-line based **Palindrome Checker** built using Python.

The application checks whether a given **string or number** is a palindrome by:

- Ignoring case differences
- Ignoring spaces
- Ignoring punctuation and symbols
- Handling numeric and textual input uniformly

This project focuses on **string normalization, input validation, and clean logic design**.

---

## 🎯 Objectives

- Understand real-world string processing
- Handle both numeric and textual palindromes
- Normalize input before applying logic
- Build a menu-driven CLI application

---

## 🧠 Concepts Used

- Strings and slicing
- String normalization
- Loops
- Conditional statements
- Functions
- Input validation
- Exception handling (`try / except`)

---

## ⚙️ Features

- Menu-driven interface
- Works for both numbers and strings
- Case-insensitive palindrome checking
- Ignores spaces and punctuation
- Handles invalid and empty input safely
- Clean exit option

---

## 📋 Menu Options

```
1. Check Palindrome
2. Exit
```

---

## 🧪 Rules Applied

### Palindrome Rules

- Case-insensitive comparison
- Spaces are ignored
- Symbols and punctuation are ignored
- Only alphanumeric characters are considered

### Valid Examples

| Input                            | Result     |
| -------------------------------- | ---------- |
| `madam`                          | Palindrome |
| `MadAm`                          | Palindrome |
| `12321`                          | Palindrome |
| `nurses run`                     | Palindrome |
| `A man, a plan, a canal: Panama` | Palindrome |

### Invalid / Non-Palindrome Examples

| Input   | Result           |
| ------- | ---------------- |
| `hello` | Not a Palindrome |
| `12345` | Not a Palindrome |
| `!!`    | Invalid Input    |

---

## ▶️ How to Run

Ensure Python is installed, then run:

```bash
python main.py
```

---

## 📌 Sample Input

```
A man, a plan, a canal: Panama
```

## 📌 Sample Output

```
✅ Palindrome
```

---

## 📂 Folder Structure

```
05-palindrome-checker/
│
├── main.py
└── README.md
```

---

## 🔮 Future Improvements

- File-based palindrome checking
- GUI version
- Performance optimization for large text
- Support for multiple checks in batch

---

## ✅ Status

✔ Completed  
✔ Tested  
✔ GitHub-ready
