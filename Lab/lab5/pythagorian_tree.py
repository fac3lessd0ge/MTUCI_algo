from turtle import *
import math
shape('turtle')
wheel = 12
pensize = 2

def iterate(step, depth):
    if depth <= 0:
        forward(step)
    else:
        new_step = step * math.sqrt(2)/2
        right(135)
        forward(new_step)
        left(90)
        iterate(new_step, depth - 1)
        left(90)
        forward(new_step)
        left(90)
        forward(new_step)
        right(135)

        forward(step)

        right(135)
        forward(new_step)
        left(90)
        forward(new_step)
        left(90)
        iterate(new_step, depth - 1)
        left(90)
        forward(new_step)
        right(135)


def run(step, depth):
    forward(step)
    left(90)
    forward(step)
    left(90)
    iterate(step, depth)
    left(90)
    forward(step)
    mainloop()


speed(0)
hideturtle()
run(30, 6)

