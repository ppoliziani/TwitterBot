import turtle
import random


def draw_square():
    turtle.forward(random.randint(0, 100))
    turtle.left(random.randint(0, 360))
    turtle.forward(random.randint(0, 360))
    turtle.left(random.randint(0, 360))
    turtle.forward(random.randint(0, 100))
    turtle.left(random.randint(0, 360))
    turtle.forward(random.randint(0, 100))
    turtle.left(random.randint(0, 360))


colours = ['green', 'red', 'blue', 'yellow', 'pink', 'purple']
for i in range(360):
    turtle.color(colours[random.randint(0, 2)])
    turtle.speed(1000)
    draw_square()
    turtle.left(random.randint(0, 360))