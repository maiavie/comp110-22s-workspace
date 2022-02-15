from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -100)
leo.pendown()

leo.color(99,204,250)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

done()