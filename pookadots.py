import turtle
import random

bob = turtle.Turtle()
screen = turtle.colormode(255)
root = turtle.Screen()
root.bgcolor("light blue")
bob.speed(0)

#def random_square():
for i in range(99):
    
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    size = random.randint(10,100)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    bob.color(r,g,b)

    bob.penup()
    bob.goto(x,y)
    bob.pendown()

    
    #bob.forward(100)
    bob.fillcolor(r,g,b)
    bob.begin_fill()
    bob.circle(size)
    #for a in range(4):
    #        bob.forward(size)
    #        bob.right(5)
    bob.end_fill()

#for x in range(25):
#    random_square()

