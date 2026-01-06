# ---------- ATM CONFIG ----------
PIN = "1234"
INITIAL_BALANCE = 10000
MAX_ATTEMPTS = 3


# ---------- AUTHENTICATION ----------
def authenticate():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        entered_pin = input("Enter your 4-digit PIN: ").strip()

        if entered_pin == PIN:
            print("✅ PIN verified successfully.\n")
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"❌ Incorrect PIN. Attempts left: {remaining}")

    print("\n🔒 Card blocked due to multiple failed attempts.")
    return False


# ---------- MENU ----------
def show_menu():
    print("\n🏧 ATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")


# ---------- OPERATIONS ----------
def check_balance(balance):
    print(f"\n💰 Current Balance: ₹{balance}")
    return balance


def deposit(balance, transactions):
    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return balance

        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print(f"✅ ₹{amount} deposited successfully.")
        return balance

    except ValueError:
        print("❌ Invalid input. Enter numbers only.")
        return balance


def withdraw(balance, transactions):
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return balance

        if amount > balance:
            print("❌ Insufficient balance.")
            return balance

        balance -= amount
        transactions.append(f"Withdrawn ₹{amount}")
        print(f"✅ ₹{amount} withdrawn successfully.")
        return balance

    except ValueError:
        print("❌ Invalid input. Enter numbers only.")
        return balance


def show_transactions(transactions):
    print("\n📄 Transaction History")

    if not transactions:
        print("No transactions yet.")
    else:
        for idx, txn in enumerate(transactions, start=1):
            print(f"{idx}. {txn}")


# ---------- MAIN ATM LOGIC ----------
def atm():
    if not authenticate():
        return

    balance = INITIAL_BALANCE
    transactions = []

    while True:
        show_menu()

        try:
            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                balance = check_balance(balance)

            elif choice == 2:
                balance = deposit(balance, transactions)

            elif choice == 3:
                balance = withdraw(balance, transactions)

            elif choice == 4:
                show_transactions(transactions)

            elif choice == 5:
                print("\n👋 Thank you for using the ATM. Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please select 1 to 5.")

        except ValueError:
            print("❌ Please enter a valid number.")


# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    atm()
