import turtle
 
 
def s(n, m):
    if n == 0:
        turtle.color('black')
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(m)
            turtle.left(90)
        turtle.end_fill()
 
    else:
        for _ in range(4):
            s(n - 1, m / 3)
            turtle.forward(m / 3)
 
            s(n - 1, m / 3)
            turtle.forward(m / 3)
 
            turtle.forward(m / 3)
            turtle.left(90)
 
 
turtle.tracer(10)
s(4, 400)
turtle.done()