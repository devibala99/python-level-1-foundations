import time

# ------------------ Quiz Data ------------------
questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["list", "set", "dictionary", "tuple"],
        "answer": "tuple"
    },
    {
        "question": "What does len() do?",
        "options": [
            "Returns memory size",
            "Returns number of elements",
            "Returns data type",
            "Returns index"
        ],
        "answer": "Returns number of elements"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
    }
]

# ------------------ Helper Functions ------------------
def show_question(q_data, q_no):
    print(f"\nQuestion {q_no}: {q_data['question']}")
    for idx, option in enumerate(q_data["options"], start=1):
        print(f"{idx}. {option}")


def get_user_answer():
    while True:
        try:
            choice = int(input("Enter your option (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("❌ Choose a number between 1 and 4.")
        except ValueError:
            print("❌ Enter numbers only.")


def calculate_grade(score, total):
    percentage = (score / total) * 100

    if percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return percentage, grade


# ------------------ Main Quiz Logic ------------------
def start_quiz():
    score = 0
    total_questions = len(questions)

    print("\n🧠 Welcome to the Python Quiz App!")
    print("⏳ You have 10 seconds per question.\n")

    for i, q in enumerate(questions, start=1):
        show_question(q, i)

        start_time = time.time()
        user_choice = get_user_answer()
        end_time = time.time()

        if end_time - start_time > 10:
            print("⏰ Time exceeded! Question skipped.")
            continue

        selected_answer = q["options"][user_choice - 1]

        if selected_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    percentage, grade = calculate_grade(score, total_questions)

    # ------------------ Final Result ------------------
    print("\n📊 Quiz Result")
    print("-------------------")
    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {score}")
    print(f"Score Percentage: {percentage:.2f}%")
    print(f"Grade           : {grade}")

    if grade == "Fail":
        print("❗ Keep practicing. You’ll improve!")
    else:
        print("🎉 Well done!")


# ------------------ Program Entry ------------------
if __name__ == "__main__":
    start_quiz()
