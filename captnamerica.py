import turtle


bob = turtle.Turtle()
bob.speed(0)
#WARNING! This is a prototype, so this item may have some bugs that will be fixed in future updates

def sheild(x,y,size):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    bob.circle(size)

bob.fillcolor("red")
bob.begin_fill()
sheild(0,-200,200)
bob.end_fill()
bob.fillcolor("gray")
bob.begin_fill()
sheild(0,-170,170)
bob.end_fill()
bob.fillcolor("red")
bob.begin_fill()
sheild(0,-140,140)
bob.end_fill()
bob.fillcolor("blue")
bob.begin_fill()
sheild(0,-110,110)
bob.end_fill()


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
  bob.end_fill()

shape(200,5,144,"gray",'#808080',-100,30)
