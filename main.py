from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your guess", prompt="which turtle will win the race, enter a color: ")
print(user_bet)

colors = ["yellow","blue","orange", "red","grey", "brown"]
start_positions = [-150,-100,-50,0,50,100]
list_of_turtles = []
for x in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_positions[x])
    list_of_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for some_turtle in list_of_turtles:
        if some_turtle.xcor() > 230:
            is_race_on = False
            winning_color = some_turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won, the {winning_color} turtle won the race ")
            else:
                print(f"you lost, the {winning_color} turtle won the race ")
        random_distance = random.randint(0,10)
        some_turtle.forward(random_distance)



screen.exitonclick()