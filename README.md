# Number Guessing Game

This is a simple **Number Guessing Game** implemented in Python. The game generates a random number, and the player has to guess it within a limited number of attempts.

## Features

- Random number generation between a specified range (default: 1 to 100).
- User-friendly input validation.
- Feedback on whether the guess is too high or too low.
- Tracks total games played and total wins.
- Option to play multiple rounds.

## How to Play

1. Run the game using Python.
2. The game will generate a random number between 1 and 100.
3. You have 7 attempts to guess the number.
4. After each guess, the game will tell you if your guess is too high, too low, or correct.
5. If you guess the number correctly, you win the round.
6. After each round, you can choose to play again or exit the game.

## Installation

1. Clone this repository or download the `guess_game.py` file.
2. Ensure you have Python 3 installed on your system.

## Usage

Run the following command to start the game:

```bash
python guess_game.py


Example Gameplay:

Welcome to the Number Guessing Game!

Guess the number between 1 and 100!
You have 7 attempts.

Attempts left: 7
Enter your guess (1-100): 50
Too low!

Attempts left: 6
Enter your guess (1-100): 75
Too high!

Attempts left: 5
Enter your guess (1-100): 63
🎉 Congratulations! You guessed it in 3 attempts!

Your stats: 1/1 wins

Play again? (yes/no): no

Thanks for playing! Goodbye.

