from turtle import Turtle, Screen

import pandas
screen = Screen()
screen.title("US States Game")
screen.setup(width=740, height=540)

image = "blank_states_img.gif"
screen.addshape(image)
bg = Turtle(image)
# get data from file 50_states.csv
data = pandas.read_csv("50_states.csv")

# get list name of state
list_states = data["state"].to_list()
correct_guess = []
is_on_game = True
while is_on_game:
    if len(correct_guess) >= 50:
        is_on_game = False
    answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                              prompt="What's another state name").title()
    if answer == "Exit":
        is_on_game = False
        new_data = pandas.DataFrame(list_states)
        new_data.to_csv("states_to_learn.csv")

    # Check if answer state is one of all the state in us
    elif answer in list_states:
        correct_guess.append(answer)
        list_states.remove(answer)
        t = Turtle()
        t.hideturtle()
        t.penup()
        answer_state = data[data.state == answer]
        t.goto(answer_state.x.item(), answer_state.y.item())
        t.write(answer)


