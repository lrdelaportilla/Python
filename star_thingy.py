import turtle

bob = turtle.Turtle()
bob.pensize(5)
bob.color("green")
def star_thingy(degree):
    for a in range(4):
        bob.forward(100)
        bob.right(90)
    bob.right(degree)

for i in range(6):
    star_thingy(60)
