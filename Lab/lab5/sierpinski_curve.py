from init import main
import turtle
import math

turtle = turtle.Turtle()
turtle.right(180)
turtle.up()
turtle.fd(300)
turtle.left(90)
turtle.fd(200)
turtle.right(90)
turtle.down()
turtle.left(225)

def half_sierpinski(step, level):
    if level == 0:
        turtle.fd(step)
        return
    half_sierpinski(step, level-1)
    turtle.left(45)
    turtle.fd(step * math.sqrt(2))
    turtle.left(45)
    half_sierpinski(step, level-1)
    turtle.right(90)
    turtle.fd(step)
    turtle.right(90)
    half_sierpinski(step, level-1)
    turtle.left(45)
    turtle.fd(step * math.sqrt(2))
    turtle.left(45)
    half_sierpinski(step, level-1)


def sierpinski(step, level):
    half_sierpinski(step, level)
    turtle.right(90)
    turtle.fd(step)
    turtle.right(90)
    half_sierpinski(step, level)
    turtle.right(90)
    turtle.fd(step)
    turtle.right(90)

main(15, 3, sierpinski)
turtle.done()