"""Forest with a lake. """

__author__ = "730225263"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entry point of my scene. """
    tyrone: Turtle = Turtle()
    rectangle(tyrone, -50, 50, 45)
    triangle(tyrone, -74, 210, 94)
    done()


def rectangle(uniqua: Turtle, x: float, y: float, width: int) -> None:
    """Drawing skinny rectangles to appear as tree trunks at coordinates x, y. """
    n: int = 0
    while n < 3:
        uniqua.penup()
        uniqua.goto(x, y)
        uniqua.pendown()
        uniqua.pencolor(108, 84, 30)
        uniqua.fillcolor(136, 107, 41)
        uniqua.begin_fill()
        i: int = 0
        while (i < 2):
            uniqua.forward(width)
            uniqua.left(90)
            uniqua.forward(200)
            uniqua.left(90)
            i += 1
        uniqua.end_fill()  
        x += 100
        y += -20
        n += 1
      

def triangle(pablo: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw a triangle at coordinate x, y. """
    m: int = 0
    while m < 2:
        n: int = 0
        x += -m * 300
        y += m * 60
        while n < 3:
            pablo.penup()
            pablo.goto(x, y)
            pablo.pendown()
            pablo.pencolor(47, 108, 30)
            pablo.fillcolor(47, 108, 30)

            pablo.begin_fill()
            i: int = 0
            while (i < 3):
                pablo.forward(side_length)
                pablo.left(120)
                i += 1
            pablo.end_fill()
            x += 100
            y += -20
            n += 1
        y += -40
        m += 1 


main()