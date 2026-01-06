# 🔢 Fibonacci Generator (CLI)

## 📌 Project Overview

The **Fibonacci Generator** is a command-line Python application that generates Fibonacci numbers using efficient loop-based logic.

This project supports two real-world use cases:

- Generating the **first N Fibonacci numbers**
- Generating Fibonacci numbers **up to a maximum value**

The application is menu-driven, user-friendly, and handles invalid inputs safely.

---

## 🎯 Objectives

- Understand Fibonacci sequence generation
- Practice loop-based mathematical logic
- Handle user input validation
- Build clean, modular, and reusable functions
- Implement exit-safe CLI applications

---

## 🧠 Concepts Used

- While loops
- Variables and state tracking
- Functions
- Conditional statements
- Input validation
- Exception handling (`try / except`)
- Menu-driven program design

---

## ⚙️ Features

- Menu-driven interface
- Generate first **N** Fibonacci numbers
- Generate Fibonacci numbers **up to a maximum value**
- Handles invalid and non-numeric input
- Prevents negative and zero values
- Clean and safe exit option

---

## 📋 Menu Options

1. Generate first N Fibonacci numbers
2. Generate Fibonacci numbers up to a maximum value
3. Exit

---

## 📐 Fibonacci Rules

- Sequence starts with: `0, 1`
- Each number is the sum of the previous two numbers
- Only positive integers are accepted as input

---

## 🧪 Sample Runs

### Example 1: First N Fibonacci Numbers

**Input**
Choice: 1
Enter number: 7

**Output**
0 1 1 2 3 5 8

---

### Example 2: Fibonacci Up to Maximum Value

**Input**
Choice: 2
Enter number: 20

**Output**
0 1 1 2 3 5 8 13

---

## ▶️ How to Run

Ensure Python is installed, then execute:

```bash
python main.py

### Folder Structure
08-fibonacci-generator/
│
├── main.py
└── README.md


🚫 Error Handling

-- Non-numeric input → rejected
-- Zero or negative numbers → rejected
-- Invalid menu choices → handled gracefully

🔮 Future Improvements

-- Recursive implementation option
-- Store output in a file
-- Graphical visualization of sequence
-- Performance comparison (loop vs recursion)

✅ Status

✔ Completed
✔ Tested
✔ Beginner-friendly
✔ Industry-standard CLI design
```
