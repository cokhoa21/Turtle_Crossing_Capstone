from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
TIME_CHANGE_SPEED = 0.1


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.reset_position()
        self.move_distance = MOVE_DISTANCE
        self.time_change_speed = TIME_CHANGE_SPEED

    def increase_speed(self):
        self.time_change_speed *= 0.9

    def up(self):
        new_y = self.ycor() + self.move_distance
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
