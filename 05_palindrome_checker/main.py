def show_menu():
    print("\n🔁 Palindrome Checker")
    print("1. Check Palindrome")
    print("2. Exit")


def is_palindrome(text):
    cleaned = ""

    for ch in text.lower():
        if ch.isalnum():   
            cleaned += ch

    if not cleaned:        
        return False

    return cleaned == cleaned[::-1]
              

def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1–2): "))

            if choice == 2:
                print("👋 Exiting Palindrome Checker. Goodbye!")
                break

            if choice != 1:
                print("❌ Invalid choice. Try again.")
                continue

            user_input = input("Enter text or number: ").strip()

            if not user_input:
                print("⚠️ Input cannot be empty.")
                continue

            result = is_palindrome(user_input)

            if result:
                print("✅ Palindrome")
            else:
                print("❌ Not a Palindrome")

        except ValueError:
            print("❌ Invalid input. Numbers only for menu.")


if __name__ == "__main__":
    main()
