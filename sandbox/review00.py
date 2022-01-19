"Response to Challenge Question 1."

choice: int = int(input("Guess a number between 0 and 100. "))

if choice < 50:
    if choice < 25:
        print("A, alpha, alphonse. ")
    else:
        print("B, beta, betagalactosidase. ")
else:
    if choice < 75:
        print("D, Delta, delta airlines. ")
    else: 
        print("C, Charlie, charli xcx. ")
