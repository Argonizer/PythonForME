import turtle
from random import randint


screen = turtle.Screen()
distance = 50
ttl = turtle.Turtle()
ttl.speed(100)
for i in range(500):
    op = ["right", "left", "forward"]
    move = op[randint(0,2)]
    if move == "forward":
        ttl.forward(randint(9, 12))
    elif move == "right":
        ttl.right(randint(0,90))
    elif move == "left":
        ttl.left(randint(0,90))

turtle.done()