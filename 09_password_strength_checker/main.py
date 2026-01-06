import string

def show_menu():
    print("\n🔐 Password Strength Checker")
    print("1. Check Password Strength")
    print("2. Exit")

def check_password_strength(password):
    
    score  = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase check
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    # Lowercase check
    if any(ch.islower() for ch in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        feedback.append("Add at least one number.")
    
    # Special character check
    if any(ch in string.punctuation for ch in password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc.)")

    # Stength rating
    if score <= 2:
        strength = "❌ Weak"
    elif score <= 4:
        strength = "⚠️ Medium"
    else:
        strength = "✅ Strong"
    
    return strength, score, feedback

def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1-2): "))

            if choice == 2:
                print("👋 Exiting Password Strength Checker.")
                break

            if choice != 1:
                print("❌ Invalid choice. Select 1 or 2.")
                continue

            password = input("Enter password to check: ").strip()

            if not password:
                print("❌ Password cannot be empty.")
                continue

            strength, score, feedback = check_password_strength(password)

            print("\n🔎 Password Analysis")
            print(f"Strength : {strength}")
            print(f"Score    : {score}/5")

            if feedback:
                print("\n🛠 Suggestions:")
                for tip in feedback:
                    print(f"- {tip}")
        
        except ValueError:
            print("❌ Please enter a numeric choice only.")

if __name__ == "__main__":
    main()