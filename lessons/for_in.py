"""An example of for in syntax. """

names: list[str] = ["Maia", "Jack", "Ashley", "Lianna"]

# Example of iteratinng through names using a while loop

print("while output: ")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# the following for...in is the same as the while loop above. 
print("for in output: ")
for name in names:
    print(name)