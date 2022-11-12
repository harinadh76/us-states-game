import turtle
from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title('US States Game')
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
ttt = 0
while ttt < 50:

    answer_text = screen.textinput(title=f'{ttt} / 50  Guess the state', prompt="what's another state name: ").title()
    print(answer_text)

    if answer_text in all_states:
        ttt += 1
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_text]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_text)



