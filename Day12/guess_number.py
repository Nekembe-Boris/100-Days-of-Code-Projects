import random
from art import logo
import os

os.system('cls')
print(logo)

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

random_num = random.randrange(1, 101)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    lives = 10
else:
    lives = 5

def game():
    global lives

    game_over = False

    print(f"You have {lives} attempts remaining to guess the number")

    while lives > 1 or game_over != True:

        guess = int(input("Make a guess: "))

        if guess == random_num:
            print(f"You got it. The answer was {random_num}")
            game_over = True
            break
        elif guess < random_num:
            lives -= 1
            print("You guessed too low")
            print(f"You have {lives} attempts remaining to guess the number")
        else:
            lives -= 1
            print("You guessed too high")
            print(f"You have {lives} attempts remaining to guess the number")

        if lives == 0:
            print(f"You lose. The answer was {random_num}")
            game_over = True

game()