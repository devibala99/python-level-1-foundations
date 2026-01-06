def show_menu():
    print("\n🔢 Fibonacci Generator")
    print("1. Generate first N Fibonacci numbers")
    print("2. Generate Fibonacci numbers up to a maximum value")
    print("3. Exit")


def generate_first_n(n):
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

    print()


def generate_upto_max(limit):
    a, b = 0, 1

    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b

    print()


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1-3): "))

            if choice == 3:
                print("👋 Exiting Fibonacci Generator")
                break

            if choice not in (1, 2):
                print("❌ Invalid choice. Select 1, 2, or 3.")
                continue

            num = int(input("Enter a positive number: "))

            if num <= 0:
                print("❌ Number must be greater than 0.")
                continue

            if choice == 1:
                generate_first_n(num)

            elif choice == 2:
                generate_upto_max(num)

        except ValueError:
            print("❌ Invalid input. Numbers only.")


if __name__ == "__main__":
    main()
