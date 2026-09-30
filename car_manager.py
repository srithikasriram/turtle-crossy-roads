from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_car(self):
        car = Turtle()
        car.setheading(180)
        car.shape("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        random_y = random.randint(-250, 280)
        car.goto(280, random_y)
        car.color(random.choice(COLORS))
        return car

    def move(self, car):
        car.forward(self.speed)

    def inc_level(self):
        self.speed += MOVE_INCREMENT

