import turtle

def main(step, level, function):
    turtle.tracer(0)
    turtle.penup()
    turtle.setpos(-100,-150)
    turtle.pendown()
    turtle.hideturtle()
    function(step, level)
    turtle.done()