# ---------- HARD CODED USERS ----------
USERS = {
    "admin": "admin123",
    "dev": "dev@123",
    "user": "user123"
}

MAX_ATTEMPTS = 3

def authenticate():

    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if not username or not password:
            print("❌ Username and password cannot be empty.")
            continue

        if username in USERS and USERS[username] == password:
            print(f"✅ Login successful. Welcome, {username}!")
            return username
        else:
            attempts += 1
            print(f"❌ Invalid credentials. Attempts left: {MAX_ATTEMPTS - attempts}")
    
    print("🔒 Account locked due to too many failed attempts.")
    return None

def show_menu():
    print("\n--- User Menu ---")
    print("1. View Profile")
    print("2. Logout")

def user_session(username):
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-2): "))
            
            if choice == 1:
                 print(f"👤 Logged in as: {username}")
            elif choice == 2:
                print("👋 Logged out successfully.")
                break
            else:
                print("❌ Invalid menu option.")
        except ValueError:
            print("❌ Please enter numbers only.")

def main():
    print("🔐 Login System")

    user = authenticate()

    if user:
        user_session(user)

    print("✅ Program ended.")


# ---------- ENTRY POINT ----------
if __name__ == "__main__":
    main()