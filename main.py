import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(player.time_change_speed)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    if player.ycor() > 280:
        player.reset_position()
        cars.increase_speed()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

    # Detect with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
