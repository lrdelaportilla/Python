#more commands
import turtle


# this is a drawing of the sahara desert
self = "admin"
bob = turtle.Turtle()
bg = turtle.Screen()

bg.bgcolor("light blue")

bob.speed(100)
bob.penup()
bob.color("yellow")
bob.goto(150,250)

bob.pendown()
bob.begin_fill()
for a in range(4):
    bob.forward(100)
    bob.right(90)
bob.penup()

bob.goto(200,271)

bob.pendown()
bob.right(45)
for a in range(4):
    bob.forward(100)
    bob.right(90)
bob.end_fill()

bob.color("goldenrod")

bob.penup()
bob.goto(-300,-150)
bob.pendown()

bob.left(45)
bob.begin_fill()
bob.forward(300)
bob.left(120)
bob.forward(300)
bob.left(120)
bob.forward(300)
bob.left(120)
bob.end_fill()

bob.penup()
bob.goto(-350,-150)
bob.pendown()

bob.color("gold")
bob.begin_fill()
bob.forward(1200)
bob.right(90)
bob.forward(400)
bob.right(90)
bob.forward(1200)
bob.right(90)
bob.forward(400)
bob.right(90)
bob.end_fill()




