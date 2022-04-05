import random

# Starting with the following list...
planeteers = ["Earth", "Wind", "Captain Planet", "Fire", "Water"]

# Access the second value in `planeteers`
planeteers[1]

# Add "Heart" to the end of `planeteers`
planeteers.append("Heart")
print(planeteers)

# Remove "Captain Planet" from the list
planeteers.remove("Captain Planet")
print(planeteers)

# Combine `planeteers` with `rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]` and save the result in a variable called `heroes`
rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]
heroes = planeteers + rangers
# print(heroes)

# Alphabetize the contents of `heroes` using a function
heroes.sort()
print(heroes)
# or
print(sorted(heroes))

# Randomize the contents of `heroes` using a function. 
# The Python documentation might help: https://docs.python.org/2/library/random.html
(random.shuffle(heroes))
print(heroes)

# Bonus: Select a random element from `heroes` using a function
# The Python documentation might help: https://docs.python.org/2/library/random.html
print(random.choice(heroes))


# Initialize a dictionary called `ninja_turtle` with the properties `name`, `weapon` and `radical`
# They should have values of "Michelangelo", "Nunchuks" and a true boolean, respectively
ninja_turtle= {
    "name": "Michelangelo",
    "weapon": "Nunchucks",
    "radical": True
}
print(ninja_turtle)

# Add a key `age` to `ninja_turtle`. Set it to whatever numerical value you'd like
ninja_turtle["age"] = 15
print(ninja_turtle)

# Remove the `radical` key-value pair from `ninja_turtle`
del ninja_turtle["radical"]
print(ninja_turtle)

# Add a key `pizza_toppings` to `ninja_turtle`. Set it to an list of strings (e.g., `["cheese", "pepperoni", "peppers"]`)
ninja_turtle["pizza_toppings"] = ["cheese", "pepperoni", "peppers"]
print(ninja_turtle)
# Access the first element of `pizza_toppings`
print(ninja_turtle['pizza_toppings'][0])

# Produce an list containing all of `ninja_turtle`'s keys using a function. 
# The Python documentation might help: https://docs.python.org/3/tutorial/datastructures.html
print(ninja_turtle.keys())

# Produce a list containing all of `ninja_turtle`'s values using a function
print(ninja_turtle.values())

# Bonus: Write a function that prints out each key-value pair in the following format - "KEY is equal to VALUE"
#  The Python documentation might help: https://docs.python.org/3/tutorial/datastructures.html

for key, value in ninja_turtle.items():
    print(f"{key} is equal to {value}")
