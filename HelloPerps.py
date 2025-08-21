import random
secret_number = 75
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")
while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("YOU ARE AWESOME! You guessed it right!")
            break  
    except ValueError:
        print("Please enter a valid number.")