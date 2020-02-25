import turtle

smile = turtle.Turtle()
smile.speed(10)


def square():
  for y in range(4):
    smile.forward(240)
    smile.left(90)
def triangle():
  for x in range(3):
    smile.forward(100)
    smile.left(120)
def circle(size):
  smile.circle(size)
def arch():
  smile.left(90)
  smile.circle(120, 180)
def compl_square():
  #complaceted, indeed
  smile.fillcolor("black")
  smile.begin_fill()
  smile.forward(10)
  smile.left(90)
  smile.forward(240)
  smile.left(90)
  smile.forward(10)
  smile.left(90)
  smile.forward(240)
  smile.left(90)
  smile.end_fill()
  
#Begin Code  
#minion body
smile.fillcolor("yellow")
smile.begin_fill()  
arch()
square()
smile.end_fill()

#goggle strap 
compl_square()

#goggle
smile.penup()
smile.goto(-170,0)
smile.pendown()

smile.fillcolor("gray")
smile.begin_fill()
circle(60)
smile.end_fill()

smile.penup()
smile.goto(-150,0)
smile.pendown()

smile.fillcolor("white")
smile.begin_fill()
circle(40)
smile.end_fill()


smile.penup()
smile.goto(-130,0)
smile.pendown()

smile.fillcolor("red")
smile.begin_fill()
circle(20)
smile.end_fill()




#blue jumpsuit
smile.penup()
smile.goto(-240,-160)
smile.pendown()

smile.fillcolor("blue")
smile.begin_fill()
smile.left(90)
smile.forward(30)
smile.right(90)
smile.forward(30)
smile.left(90)
smile.forward(180)
smile.left(90)
smile.forward(30)
smile.right(90)
smile.forward(30)
smile.right(90)
smile.forward(80)
smile.right(90)
smile.forward(240)
smile.right(90)
smile.forward(80)
smile.end_fill()

smile.penup()
smile.goto(-150,-150,)
smile.pendown()

smile.right(90)
smile.circle(100,90)
#mathtell = 360 / 4
#print(mathtell)



smile.penup()
smile.goto(-120,120)
smile.pendown()

smile.forward(50)
smile.left(180)
smile.forward(50)

smile.left(135)
smile.forward(50)
smile.left(180)
smile.forward(50)

smile.right(90)
smile.forward(50)
smile.left(180)
smile.forward(50)
