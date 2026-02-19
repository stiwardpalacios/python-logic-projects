import random


def choose_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Try again.")


def play_game():
    print("\n Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    max_attempts = choose_difficulty()

    attempts = 0
    guesses = []

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            guesses.append(guess)

            if guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                print(f"\n✅ Correct! You guessed it in {attempts} attempts.")
                break

            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"\n❌ Game Over. The number was {secret_number}")

    print("Your guesses:", guesses)


def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
