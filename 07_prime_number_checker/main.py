def is_prime(n):

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


def show_menu():
    print("\n🔢 Prime Number Checker")
    print("1. Check Prime Number")
    print("2. Exit")


while True:
    show_menu()

    try:
        choice = int(input("Enter your choice (1-2): "))

        if choice == 2:
            print("👋 Exiting Prime Number Checker")
            break

        if choice != 1:
            print("❌ Invalid choice")
            continue

        num = int(input("Enter a number: "))

        if is_prime(num):
            print("✅ Prime Number")
        else:
            print("❌ Not a Prime Number")

    except ValueError:
        print("❌ Enter numbers only")
