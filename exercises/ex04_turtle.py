"""Forest with a lake."""

__author__ = "730225263"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entry point of my scene."""
    tyrone: Turtle = Turtle()
    tyrone.speed(15)
    line(tyrone, -300, 0, 600)
    rectangle(tyrone, -50, 50, 45)
    multi_triangle(tyrone, -74, 210, 94)
    star(tyrone, -250, 150, 40)
    circle(tyrone, -200, -450, 200)
    done()


def rectangle(uniqua: Turtle, x: float, y: float, width: int) -> None:
    """Drawing skinny rectangles to appear as tree trunks at coordinates x, y."""
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
    """Draw a triangle starting at coordinate x, y."""
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


def multi_triangle(pablo: Turtle, x: float, y: float, side_length: int) -> None:
    """Breaking up complex function: triangles."""
    m: int = 0
    while m < 2:
        n: int = 0
        x += -m * 300
        y += m * 60
        while n < 3:
            triangle(pablo, x, y, side_length)
            x += 100
            y += -20
            n += 1
        y += -40
        m += 1 


def star(austin: Turtle, x: float, y: float, size: int) -> None:
    """Drawing a star at point x, y."""
    austin.penup()
    austin.goto(x, y)
    austin.pendown()
    austin.pencolor(189, 153, 5)
    austin.fillcolor(255, 218, 51)

    austin.begin_fill()
    i: int = 0
    angle: float = 144
    while (i < 5):
        austin.forward(size)
        austin.left(angle)
        i += 1
    austin.end_fill()


def line(sasha: Turtle, x: float, y: float, length: int) -> None:
    """Drawing a line."""
    sasha.penup()
    sasha.goto(x, y)
    sasha.pendown()
    sasha.pencolor(249, 187, 125)
    sasha.fillcolor(249, 187, 125)

    sasha.begin_fill()
    sasha.forward(length)
    sasha.end_fill()


def circle(ninja: Turtle, x: float, y: float, radius: int) -> None:
    """Trying something fun: a circle for a lake."""
    ninja.penup()
    ninja.goto(x, y)
    ninja.pendown()
    ninja.pencolor(59, 181, 224)
    ninja.fillcolor(39, 191, 245)

    ninja.begin_fill()
    ninja.circle(radius)
    ninja.end_fill()


main()