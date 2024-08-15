print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Set both names to lower case

total_name = name1.lower() + name2.lower()

total_1 = total_name.count("t") + total_name.count("r") + \
    total_name.count("u") + total_name.count("e")
total_2 = total_name.count("l") + total_name.count("o") + \
    total_name.count("v") + total_name.count("e")

score = int(str(total_1) + str(total_2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
