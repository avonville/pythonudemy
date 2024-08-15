
# modifying global scope
enemies = 1


def increase_enemies():
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159


def calc():
    return 2 * PI


print(calc())
