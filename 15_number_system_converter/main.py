def show_menu():
    print("\n🔢 Number System Converter")
    print("1. Decimal → Binary")
    print("2. Decimal → Octal")
    print("3. Decimal → Hexadecimal")
    print("4. Binary → Decimal")
    print("5. Exit")


def decimal_to_binary(n):
    return bin(n)[2:]


def decimal_to_octal(n):
    return oct(n)[2:]


def decimal_to_hexadecimal(n):
    return hex(n)[2:].upper()


def binary_to_decimal(b):
    return int(b, 2)


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1–5): ").strip())

            if choice == 5:
                print("👋 Exiting Number System Converter.")
                break

            if choice < 1 or choice > 5:
                print("❌ Invalid choice. Please select between 1 and 5.")
                continue

            if choice in [1, 2, 3]:
                num = int(input("Enter a decimal number: ").strip())

                if num < 0:
                    print("❌ Please enter a non-negative decimal number.")
                    continue

                if choice == 1:
                    result = decimal_to_binary(num)
                    print(f"✅ Binary: {result}")

                elif choice == 2:
                    result = decimal_to_octal(num)
                    print(f"✅ Octal: {result}")

                elif choice == 3:
                    result = decimal_to_hexadecimal(num)
                    print(f"✅ Hexadecimal: {result}")

            elif choice == 4:
                binary = input("Enter a binary number: ").strip()

                if not all(ch in "01" for ch in binary):
                    print("❌ Invalid binary number.")
                    continue

                result = binary_to_decimal(binary)
                print(f"✅ Decimal: {result}")

        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()
