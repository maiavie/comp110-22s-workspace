"""Wordle: The Real Thing!"""

__author__ = "730225263" 

#The variables for the colored boxes used in the game. 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#Tying the other functions together to run the game.
def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess: str
    turn: int = 0
    while turn < 6:
        print(f"~~~ Turn {turn + 1}/6 ~~~")
        guess = input_guess(len(secret)) #Prompting the user for a guess.
        print(emojified(guess, secret))  #Color-coded square sequence for guess.
        if guess == secret: #Ending the game if answer is correct. 
            return print(f"Congratulations! You got today's wordle in {turn + 1}/6 turns. ")
        if guess != secret:
            turn += 1
    return print(f"X/6- Sorry, that's all the guesses you get. The correct word was {secret}. Try again tomorrow! ")

def contains_char(secret: str, char: str) -> bool: 
    """To check if the character matches anything in secret."""
    assert len(char) == 1 
    i: int = 0
    while i < len(secret):
        if char == secret[i]:
            return True
        i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """To assign colored boxes to our guess."""
    assert len(guess) == len(secret)
    i = 0
    square: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            square += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) == True:
                square += YELLOW_BOX#Utilizing contains_char to determine incorrect spot, right character.
            if contains_char(secret, guess[i]) == False:
                square += WHITE_BOX
        i += 1 
    return square

def input_guess(length: int) -> str:
    """To assure the guess is of the correct length."""
    guess: str = input(f"Enter a {length}-character word: ")
    while len(guess) != length:
        guess: str = input(f"That wasn't {length} characters! Try again: ")
    return guess

if __name__ == "__main__":
    main()