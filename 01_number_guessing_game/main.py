import random

def play_game():
    random_number = random.randint(1, 50)
    attempts = 5

    print("\n🎯 Welcome to Number Guessing Game")
    print("Guess a number between 1 and 50")
    print(f"You have {attempts} attempts\n")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 50:
                print("❌ Number must be between 1 and 50")
                continue

            if guess == random_number:
                print("🎊 Congratulations! You guessed it right.")
                return
            elif guess > random_number:
                print("📉 Too high!")
            else:
                print("📈 Too low!")

            attempts -= 1
            print(f"Attempts left: {attempts}\n")

        except ValueError:
            print("❌ Invalid input. Please enter numbers only.\n")

    print(f"😞 Game Over! The correct number was {random_number}")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (Y/N): ").lower()

        if replay != 'y':
            print("👋 Thank you for playing!")
            break

main()
