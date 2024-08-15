# import another_module

# print(another_module.another_variable) 


# from turtle import Turtle, Screen

# timmy = Turtle() # This will create a new turtle

# print(timmy) # This will print the object's memory address

# timmy.shape("turtle") # This will change the shape of the turtle
# timmy.color("red") # This will change the color of the turtle
# timmy.forward(100) # This will move the turtle forward by 100 units

# my_screen = Screen() # This will create a new screen

# print( my_screen.canvheight ) # This will print the height of the screen

# my_screen.exitonclick() # This will close the screen when clicked


from prettytable import PrettyTable as pt

table = pt()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table) # This will print an empty table
