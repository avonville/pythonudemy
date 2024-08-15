print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# Decision 1
direction = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if direction == "left":
    # Decision 2
    action = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if action == "wait":
        # Decision 3
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ")
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
