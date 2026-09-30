import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#create turtle
player = Player()

screen.listen()
screen.onkeypress(fun=player.up, key="Up")
car_man = CarManager()
scoreboard = Scoreboard()
game_is_on = True

cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 7) == 1:
        car = car_man.generate_car()
        cars.append(car)

    for car in cars:
        car_man.move(car)

        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

        if car.xcor() < -320:
            cars.remove(car)

    if player.detect_win():
        scoreboard.inc_level()
        car_man.inc_level()


screen.exitonclick()
