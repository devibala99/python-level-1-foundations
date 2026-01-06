def show_menu():
    print("\n📊 Word & Character Counter")
    print("1. Word Count")
    print("2. Character Count (excluding spaces)")
    print("3. Word + Character Count")
    print("4. Exit")


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    count = 0
    for char in text:
        if not char.isspace():
            count += 1
    return count


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1–4): "))

            if choice == 4:
                print("👋 Exiting Word & Character Counter. Goodbye!")
                break

            if choice < 1 or choice > 4:
                print("❌ Invalid choice. Please select between 1 and 4.")
                continue

            text = input("Enter a sentence or word: ").strip()

            if not text:
                print("⚠️ Input cannot be empty. Please try again.")
                continue

            if choice == 1:
                words = count_words(text)
                print(f"📝 Word Count: {words}")

            elif choice == 2:
                characters = count_characters(text)
                print(f"🔠 Character Count (excluding spaces): {characters}")

            elif choice == 3:
                words = count_words(text)
                characters = count_characters(text)
                print(f"📝 Word Count: {words}")
                print(f"🔠 Character Count (excluding spaces): {characters}")

        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")


main()
