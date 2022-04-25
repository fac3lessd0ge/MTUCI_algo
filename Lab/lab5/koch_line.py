from init import main
import turtle


def koch_line(step, n):
    if n == 0:
        turtle.fd(step)
        return
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch_line(step / 3, n - 1)


main(500, 4, koch_line)