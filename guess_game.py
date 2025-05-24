import random
from typing import Optional

class NumberGuessingGame:
    def __init__(self):
        self.min_num = 1
        self.max_num = 100
        self.max_attempts = 7
        self.secret_number: Optional[int] = None
        self.attempts = 0
        self.total_games = 0
        self.total_wins = 0

    def generate_number(self):
        """Generate a new random number for each game"""
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

    def get_valid_guess(self) -> int:
        """Handle user input with proper error checking"""
        while True:
            try:
                guess = int(input(f"Enter your guess ({self.min_num}-{self.max_num}): "))
                if self.min_num <= guess <= self.max_num:
                    return guess
                print(f"Please enter a number between {self.min_num} and {self.max_num}!")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def play_round(self):
        """Play one full round of the game"""
        self.generate_number()
        print(f"\nGuess the number between {self.min_num} and {self.max_num}!")
        print(f"You have {self.max_attempts} attempts.")

        while self.attempts < self.max_attempts:
            remaining = self.max_attempts - self.attempts
            print(f"\nAttempts left: {remaining}")
            
            guess = self.get_valid_guess()
            self.attempts += 1

            if guess < self.secret_number:
                print("Too low!")
            elif guess > self.secret_number:
                print("Too high!")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {self.attempts} attempts!")
                self.total_wins += 1
                return True

        print(f"\nGame over! The number was {self.secret_number}.")
        return False

    def play_game(self):
        """Main game loop with play again option"""
        print("Welcome to the Number Guessing Game!")
        
        while True:
            self.total_games += 1
            self.play_round()
            
            print(f"\nYour stats: {self.total_wins}/{self.total_games} wins")
            
            while True:
                play_again = input("\nPlay again? (yes/no): ").lower()
                if play_again in ('yes', 'no'):
                    break
                print("Please enter 'yes' or 'no'.")
            
            if play_again == 'no':
                print("\nThanks for playing! Goodbye.")
                break

# Start the game
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play_game()