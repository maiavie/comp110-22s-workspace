"""Example of if-else statement with DHW."""

SECRET: str = ("Lynette")

print("Can you guess my favorite desperate housewife? ")
guess: str = input("What's your guess? ")

if guess == SECRET:
    print("Congrats on guessing the best housewife! ")
else: 
    print("Wrong. Try again!")
    if guess == str("Edie"):
        print("Close! Think: smarter. ")
    else:
        print("Try one of the blonder girls. ")