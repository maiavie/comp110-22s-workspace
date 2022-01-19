"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5. What is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You've guessed correctly! Congrats!! ")
    print("Have a wonderful day, love! ")
else: 
    print("Sorry pal, you guessed incorrectly. :( ")
    if guess > SECRET:
        print("Try guessing a little lower. ")
    else: 
        print("Too low! Aim a little higher. ")

print("Game over. ")