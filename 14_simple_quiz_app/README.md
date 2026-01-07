# 🧠 Simple Quiz App (MCQ | CLI)

## 📌 Project Overview

This is a **command-line based Simple Quiz Application** built using Python.

The application presents multiple-choice questions (MCQs) to the user, enforces a time limit per question, evaluates answers, calculates the final score, and assigns a grade based on performance.

This project focuses on **lists, dictionaries, loops, input validation, timing logic, and clean function-based design**, making it a strong beginner-to-intermediate level Python project.

---

## 🎯 Objectives

- Build a real-world MCQ-based quiz system
- Practice using lists and dictionaries together
- Implement time-based constraints for user input
- Calculate score, percentage, and grade
- Design a clean and modular CLI application
- Handle invalid user input safely

---

## 🧠 Concepts Used

- Lists and dictionaries
- Functions and modular design
- Loops (`for`, `while`)
- Conditional statements
- Input validation
- Exception handling (`try / except`)
- Time handling using `time` module
- Guard clauses (early exits)
- Program entry point (`if __name__ == "__main__"`)

---

## ⚙️ Features

- Multiple-choice questions (MCQs)
- 4 options per question
- Time limit of 10 seconds per question
- Automatic question skip if time exceeds
- Instant feedback for each answer
- Final score calculation
- Percentage-based grading system
- Beginner-friendly CLI interface

---

## ⏳ Quiz Rules

- Each question has **10 seconds** to answer
- Only one option (1–4) is allowed
- Invalid inputs are handled gracefully
- Unanswered or late questions are skipped
- No negative marking

---

## 🧪 Grading System

| Percentage    | Grade |
| ------------- | ----- |
| 80% and above | A     |
| 60% – 79%     | B     |
| 40% – 59%     | C     |
| Below 40%     | Fail  |

---

## ▶️ How to Run

Ensure Python is installed on your system, then run:

```bash
python main.py

📌 Sample Flow
### Input
Enter your option (1-4): 2

### Output
✅ Correct!

📊 Sample Result
📊 Quiz Result
-------------------
Total Questions : 5
Correct Answers : 4
Score Percentage: 80.00%
Grade           : A
🎉 Well done!

📂 Folder Structure
14_simple_quiz_app/
│
├── main.py
└── README.md

🚫 Validation Handled

-- Non-numeric option input
-- Option numbers outside valid range (1–4)
-- Time limit exceeded per question
-- Safe handling of invalid entries

🔮 Future Improvements

-- Randomized question order
-- Question bank from file or database
-- GUI-based quiz app
-- Difficulty levels
-- Leaderboard system
-- Persistent score storage

✅ Project Status

✔ Completed
✔ Tested
✔ CLI-based
✔ GitHub-ready
✔ Industry-aligned beginner project
```
