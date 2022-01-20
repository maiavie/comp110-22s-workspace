"""EX01 - Chardle: A cute step toward Wordle."""

__author__ = "730225263"

inst: int = 0

five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    print("Error: That's not a five character word. Try again!")
    exit()

sing_char: str = input("Enter a single character: ")
if len(sing_char) != 1:
    print("Error: Please enter only a single character.")
    exit()

print("Searching for " + sing_char + " in " + five_char_word)
if sing_char == five_char_word[0]:
    print(sing_char + " found at index 0")
    inst = inst + 1 
if sing_char == five_char_word[1]:
    print(sing_char + " found at index 1")
    inst = inst + 1 
if sing_char == five_char_word[2]:
    print(sing_char + " found at index 2")
    inst = inst + 1 
if sing_char == five_char_word[3]:
    print(sing_char + " found at index 3")
    inst = inst + 1 
if sing_char == five_char_word[4]:
    print(sing_char + " found at index 4")
    inst = inst + 1 

if inst == 0:
    print("No instances of " + sing_char + " found in " + five_char_word)
else:
    if inst == 1:
        print(str(inst) + " instance of " + sing_char + " found in " + five_char_word)
    else: 
        print(str(inst) + " instances of " + sing_char + " found in " + five_char_word)


