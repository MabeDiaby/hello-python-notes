# If the age variable is below 21, the program should output that the person cannot enter because they are too young, if they are over 21 they can enter, and if age is not a number it outputs an error.

# Bonus: if age is 18 or older, but under 21, output that the person can enter the bar but cannot drink!

print("how old are you?")
age = int(input())

if age < 18:
    print("you can not enter the club you are too young")
elif age < 21:
    print("you can enter, but cant drink")
else:
    print("you can enter, drink responsibility!")
