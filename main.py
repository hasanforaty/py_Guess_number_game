from art import logo
import random


def playTheGame():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    selected_number = random.randint(1, 100)
    if difficulty == "easy":
        num_attempt = 10
    else:
        num_attempt = 5
    while num_attempt > 0:
        print(f"You have {num_attempt} attempts remaining to guess the number.")
        guess = int(input("make a Guess: "))
        num_attempt -= 1
        if guess == selected_number:
            print("Congratulations! You Winn")
            return
        elif guess < selected_number:
            print("Too Low!")
        else:
            print("Too High!")
    print(f"You have ran out of your guesses! you Loss,number was {selected_number}")


print(logo)
playTheGame()
