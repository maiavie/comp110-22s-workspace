"""Wordle, but the game ends after each guess."""

__author__ = "730225263"

# Codes for Emoji boxes! 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "whore alert <3"
guess: str = input(str(f"Guess a {len(secret)}-letter word. "))

index: int = 0
square: str = "" 
# Checking to see that the length of the input guess matches
# the length of the secret word. 

while len(guess) != len(secret):
    guess: str = input(f"That was not {len(secret)} letters! Try again. ")

# Checking to see if exact letter matches exact position. 
while index < len(secret):
    if guess[index] == secret[index]:
        square += GREEN_BOX

# Scanning through secret word to check for correct-character, incorrect
# placement matches. 
    else:
        secret_char: bool = False
        secret_index: int = 0
        while secret_index < len(secret) and secret_char is False:
            if secret[secret_index] == guess[index]: 
                secret_char = True
                square += YELLOW_BOX
            else: 
                secret_index += 1
# When we have checked all the letters for right-character, wrong place,
# the secret index will match the length and give up (white box.)
        if secret_index == len(secret):
            square += WHITE_BOX
    index += 1
print(square)

if guess == secret:
    print("Nice job! You got it! :)")
else:
    print("Not quite. Play again soon! ")