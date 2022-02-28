"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int] 

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150


# Access a value by its key ("Looking up")
# print(f"UNC has {schools['UNC']} students.")


# Removing a key-value pair from the  by its key
schools.pop("Duke")

# Test for the existence of a key 
is_duke_present: bool = "Duke" in schools
# print(f"Duke is present: {is_duke_present}")


# Update/ resassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Print a dictionary literal representation
# print(schools)


# Demonstration of dictionary literals
schools = {}  # same as dict()
# print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
# print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dictionary
for school in schools: 
    print(f"key: {school} -> Value: {schools[school]}")