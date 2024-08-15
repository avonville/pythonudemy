import random
# Banker Roulette Coding Exercise
names_string = input("Give me everybody's names, separated by a comma. ")
if not names_string:
    print("No one is going to buy the meal today.")
else:
    names = names_string.split(", ")
    random_name = random.choice(names)
    print(f"{random_name} is going to buy the meal today!")
