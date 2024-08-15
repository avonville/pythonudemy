import random

random_int = random.randint(0, 5)
random_float = random.random()

# Get a random number between 0 and 5

# Bad Solution
print(random_int + random_float)
# Best Solution
print(random_float * 5)
