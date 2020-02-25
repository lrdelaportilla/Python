import turtle

bob = turtle.Turtle()
bob.speed(0)

#head
for i in range(36):
    bob.forward(18)
    bob.right(10)
#middle
for i in range(36):
    bob.forward(12)
    bob.left(10)
# head
bob.penup()
bob.goto(0,228)
bob.pendown()
for i in range(36):
    bob.forward(8)
    bob.right(10)

# eye right
bob.penup()
bob.goto(25,200)
bob.pendown()
for i in range(36):
    bob.forward(1)
    bob.right(10)

# eye left
bob.penup()
bob.goto(-20,200)
bob.pendown()
for i in range(36):
    bob.forward(1)
    bob.right(10)

# smile
bob.penup()
bob.goto(-20,180)
bob.pendown()
bob.right(90)
for i in range(18):
    bob.forward(4)
    bob.left(10)

    
bob.penup()
bob.goto(-200,-200)

