import turtle

ttl = turtle.Turtle()
for i in range(4):
    for i in range(10):
        ttl.forward(10)
        ttl.penup()
        ttl.forward(10)
        ttl.pendown()
    ttl.right(90)


turtle.done()