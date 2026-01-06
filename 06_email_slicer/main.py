def show_menu():
    print("\n📧 Email Slicer Application")
    print("1. Slice Email")
    print("2. Exit")


def is_valid_email(email):
    if not email:
        return False

    # Check @ symbol
    if email.count("@") != 1:
        return False

    if email.startswith("@") or email.endswith("@"):
        return False

    username, domain = email.split("@")

    if not username:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    domain_name, extension = domain.rsplit(".", 1)

    if not domain_name or not extension:
        return False

    if len(extension) < 2:
        return False

    return True


def slice_email(email):
    username, domain = email.split("@")
    domain_name, extension = domain.rsplit(".", 1)
    return username, domain_name, extension


def main():
    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice (1-2): "))

            if choice == 2:
                print("👋 Exiting Email Slicer. Goodbye!")
                break

            if choice != 1:
                print("❌ Invalid choice. Please select 1 or 2.")
                continue

            email = input("Enter email address: ").strip().lower()

            if not is_valid_email(email):
                print("❌ Invalid email format.")
                continue

            username, domain, extension = slice_email(email)

            print("\n✅ Email Details")
            print(f"Username   : {username}")
            print(f"Domain     : {domain}")
            print(f"Extension  : {extension}")

        except ValueError:
            print("❌ Please enter a numeric choice only.")


if __name__ == "__main__":
    main()
