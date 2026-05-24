import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    
    print("Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

number_guessing_game()