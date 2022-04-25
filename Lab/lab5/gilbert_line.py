from turtle import Screen, Turtle

def hilbert_curve(turtle, step, parity, n):

    if n < 1:
        return

    turtle.left(parity * 90)
    hilbert_curve(turtle, step, - parity, n - 1)

    turtle.forward(step)
    turtle.right(parity * 90)
    hilbert_curve(turtle, step, parity, n - 1)

    turtle.forward(step)
    hilbert_curve(turtle, step, parity, n - 1)

    turtle.right(parity * 90)
    turtle.forward(step)
    hilbert_curve(turtle, step, - parity, n - 1)

    turtle.left(parity * 90)

screen = Screen()
ttl = Turtle()
ttl.speed(0)

hilbert_curve(ttl, 10, 1, 6)
ttl.done()