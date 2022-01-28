"""An oracle that predicts the future...wooOOOoo. """

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0,3)

if response == 0:
    print("Most definitely. ")
elif response == 1:
        print("It's very likely. ")
elif response == 2:
    print("Ask again later. ")
elif response == 3:
    print("It's a no from me. ")



