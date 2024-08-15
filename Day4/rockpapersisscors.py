import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

# Get user input
user_choice = int(input())

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
    exit()

# Get computer input
computer_choice = random.randint(0, 2)

# Create a list of choices
choices = ["Rock", "Paper", "Scissors"]

# Print the choices
print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

# Compare the choices
if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")
