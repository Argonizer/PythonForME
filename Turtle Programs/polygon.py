import turtle

ttl = turtle.Turtle()
no_of_sides = 3
for i in range(no_of_sides):
    ttl.forward(200/no_of_sides)
    ttl.right(360/no_of_sides)

turtle.done()