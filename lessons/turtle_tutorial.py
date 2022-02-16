from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -100)
leo.pendown()

leo.pencolor(99, 204, 250)
leo.fillcolor(219, 138, 215)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()

bob.pencolor(30, 30, 30)
bob.fillcolor(75, 190, 140)

bob.penup()
bob.goto(-150, -100)
bob.pendown()

bob.speed(50)
i: int = 0
side_length: float = 300.0
angle: float = 120.0

while (i < 50):
    bob.forward(side_length)
    bob.left(angle)
    side_length = side_length * 0.95
    angle += 0.5
    i += 1

done()
