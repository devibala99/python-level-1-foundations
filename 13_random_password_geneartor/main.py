import random
import string


def show_menu():
    print("\n🔐 Random Password Generator")
    print("1. Generate password by length")
    print("2. Generate password by strength")
    print("3. Exit")


def generate_by_length(length):
    if length < 4:
        return None

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password


def generate_by_strength(strength):
    if strength == 1:  # Weak
        chars = string.ascii_lowercase
        length = 6
    elif strength == 2:  # Medium
        chars = string.ascii_letters + string.digits
        length = 8
    elif strength == 3:  # Strong
        chars = string.ascii_letters + string.digits + string.punctuation
        length = 12
    else:
        return None

    password = "".join(random.choice(chars) for _ in range(length))
    return password


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Choose an option (1-3): "))

            if choice == 3:
                print("👋 Exiting Password Generator. Goodbye!")
                break

            if choice == 1:
                length = int(input("Enter password length (min 4): "))
                password = generate_by_length(length)

                if password:
                    print(f"✅ Generated Password: {password}")
                else:
                    print("❌ Password length must be at least 4.")

            elif choice == 2:
                print("\nChoose Strength:")
                print("1. Weak")
                print("2. Medium")
                print("3. Strong")

                strength = int(input("Enter strength (1-3): "))
                password = generate_by_strength(strength)

                if password:
                    print(f"✅ Generated Password: {password}")
                else:
                    print("❌ Invalid strength option.")

            else:
                print("❌ Invalid menu choice.")

        except ValueError:
            print("❌ Please enter numeric values only.")


if __name__ == "__main__":
    main()
