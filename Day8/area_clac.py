import math


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


# Write your code above this line
test_h = int(input("Enter the height of the wall: "))
test_w = int(input("Enter the width of the wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
