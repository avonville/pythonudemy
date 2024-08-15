import random

print("Welcome to the My Password Generator!")
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# Create a list of letters, numbers, and symbols
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# Create lists for each type of character based on user input
choice_letters = random.choices(letters, k=num_letters)
choice_numbers = random.choices(numbers, k=num_numbers)
choice_symbols = random.choices(symbols, k=num_symbols)

# Create a random password easy way
password_easy = "".join(choice_letters + choice_numbers + choice_symbols)

print(f"Your password is: {password_easy}")

# Create a random password hard way
# Create a list and append each character type to it
password_list = []
for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))
for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

# Create a random list of numbers to hold the order of the characters
my_order = random.sample(range(1, len(password_list)+1), len(password_list))

# Create a new list with the characters in the random order
password_list = [password_list[i-1] for i in my_order]

# Convert the list to a string
password_hard = "".join(password_list)

print(f"Your password is: {password_hard}")
