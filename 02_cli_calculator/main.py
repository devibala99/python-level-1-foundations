def calculator(choice, a, b):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        return a / b


def show_menu():
    print("\nWelcome to the Calculator Application 😎")
    print("1. Addition ➕")
    print("2. Subtraction ➖")
    print("3. Multiplication ✖️")
    print("4. Division ➗")
    print("5. Exit ❌")


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 5:
                print("👋 Exiting Calculator. Thank you!")
                break

            if choice < 1 or choice > 5:
                print("❌ Invalid choice. Please select between 1 and 5.")
                continue

            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            if choice == 4 and b == 0:
                print("❌ Cannot divide by zero.")
                continue

            result = calculator(choice, a, b)
            print(f"✅ Result: {result}")

        except ValueError:
            print("❌ Invalid input. Please enter numeric values only.")


main()
