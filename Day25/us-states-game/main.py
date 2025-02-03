import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states=[]

while len(guessed_states) < 50:
    answer_state = screen.textinput( title=f"{len(guessed_states)}/50 States correct", prompt="What's a state's name?")

    selected_state = data[data.state == answer_state.title()]

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv( "states_to_learn.csv", index=False)
        break

    if not selected_state.empty:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(selected_state.x.item(),selected_state.y.item())
        t.write(selected_state.state.item())
        guessed_states.append(selected_state.state.item())
