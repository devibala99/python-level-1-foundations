import random

CHOICES = ["rock", "paper", "scissors"]


def show_menu():
    print("\n🎮 Rock Paper Scissors")
    print("1. Play Game")
    print("2. Exit")


def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"


def play_game():
    player_score = 0
    computer_score = 0
    rounds = 0

    print("\n🔥 Best of 5 Game Started!")

    while rounds < 5:
        player_choice = input("Enter rock / paper / scissors: ").strip().lower()

        if player_choice not in CHOICES:
            print("❌ Invalid choice. Try again.")
            continue

        computer_choice = random.choice(CHOICES)
        print(f"🤖 Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)

        if winner == "player":
            print("✅ You win this round!")
            player_score += 1
        elif winner == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("⚖️ It's a draw!")

        rounds += 1
        print(f"📊 Score → You: {player_score} | Computer: {computer_score}")

    print("\n🏁 Game Over")
    if player_score > computer_score:
        print("🎉 You won the game!")
    elif computer_score > player_score:
        print("😞 Computer won the game!")
    else:
        print("🤝 Game ended in a draw!")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-2): "))

            if choice == 1:
                play_game()
            elif choice == 2:
                print("👋 Exiting game. Goodbye!")
                break
            else:
                print("❌ Invalid menu option.")

        except ValueError:
            print("❌ Please enter numbers only.")


if __name__ == "__main__":
    main()
