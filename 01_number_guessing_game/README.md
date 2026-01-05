# 🎯 Number Guessing Game (CLI)

## 📌 Project Overview
This is a command-line based Number Guessing Game built using Python.  
The program randomly generates a number within a given range, and the user must guess the number within a limited number of attempts.

This project focuses on strengthening **control flow, input validation, loops, and functions**.

---

## 🧠 Concepts Used
- Variables and data types
- `if / elif / else` conditions
- `while` loops
- Functions
- Exception handling (`try / except`)
- Python standard library (`random`)

---

## ⚙️ How the Game Works
1. The program generates a random number between **1 and 50**
2. The user gets **5 attempts** to guess the number
3. After each guess, the program gives feedback:
   - Too high
   - Too low
4. The game ends when:
   - The user guesses correctly, or
   - All attempts are exhausted
5. The user is asked if they want to replay

---

## ▶️ How to Run
Make sure Python is installed, then run:

```bash
python main.py

### Sample Output

🎯 Welcome to Number Guessing Game
Guess a number between 1 and 50
You have 5 attempts

Enter your guess: 25
📉 Too high!
Attempts left: 4
