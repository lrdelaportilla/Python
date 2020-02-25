import turtle
import random

bob = turtle.Turtle()
screen = turtle.colormode(255)
root = turtle.Screen()
root.bgcolor("darkblue")
bob.color("darkblue")
bob.speed(0)

#moon
bob.penup()
bob.goto(0,100)
bob.pendown()
bob.right(90)
bob.fillcolor("white")
bob.begin_fill()
bob.circle(120)
bob.end_fill()
bob.fillcolor("darkblue")
bob.penup()
bob.goto(-10,100)
bob.pendown()
bob.begin_fill()
bob.circle(100)
bob.end_fill()


#stars

def shape(length,corners,angles,border,fill,x,y):
  bob.penup()
  bob.goto(x,y)
  bob.color(border)
  bob.pendown()
  bob.fillcolor(fill)
  bob.begin_fill() 
  for x in range(corners):
    bob.forward(length)
    bob.right(angles)
    bob.forward(length)
    bob.right(72 - angles)
  bob.end_fill()


for i in range(30):
    
    x = random.randint(-300,300)
    y = random.randint(-300,300)

    size = random.randint(10,20)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    bob.color(r,g,b)

    bob.penup()
    bob.goto(x,y)
    bob.pendown()

    
    #bob.forward(100)
    #bob.fillcolor(r,g,b)
    #bob.begin_fill()
    #bob.circle(size)
    shape(size,5,144,"white",'#FFFFFF',x,y)
    #for a in range(4):
    #        bob.forward(size)
    #        bob.right(5)


    
    #bob.end_fill()

#for x in range(25):
#    random_square()

