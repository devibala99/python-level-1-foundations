# 📊 Word & Character Counter (CLI)

## 📌 Project Overview

This is a command-line based **Word & Character Counter** built using Python.

The application allows users to:

- Count the number of words in a given text
- Count the number of characters (excluding spaces)
- Perform both operations together

This project focuses on **string handling, input validation, loops, and clean function design**, simulating real-world text processing logic.

---

## 🎯 Objectives

- Strengthen string manipulation skills
- Handle user input safely
- Build menu-driven CLI applications
- Apply real-world constraints (spaces, empty input, punctuation)

---

## 🧠 Concepts Used

- Strings and string methods
- Loops (`while`)
- Conditional statements (`if / elif / else`)
- Functions
- Input validation
- Exception handling (`try / except`)

---

## ⚙️ Features

- Menu-driven interface
- Word count functionality
- Character count (excluding spaces)
- Combined word + character count
- Handles empty input safely
- Handles invalid menu selections
- Clean exit option

---

## 📋 Menu Options

- Word Count
- Character Count (Excluding spaces)
- Word + Character Count
- Exit

---

## 🧪 Rules Applied

### Word Count

- Words are separated by whitespace
- Multiple spaces are ignored
- Punctuation does not break word counting

### Character Count

- Counts all characters except:
  - Spaces
  - Tabs
  - Newlines
- Includes letters, numbers, and symbols

### Input Validation

- Only numeric menu input allowed
- Empty or whitespace-only text is rejected
- Program does not crash on invalid input

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python main.py

## Sample Input

Hello,   world! Python is awesome.

## Sample Output

Word Count: 5
Character Count (excluding spaces): 26

## 📂 Folder Structure
04-word-character-counter/
│
├── main.py
└── README.md

##🔮 Future Improvements

- Ignore punctuation in character count (optional)
- File-based input support
- Sentence count feature
- GUI version
```
