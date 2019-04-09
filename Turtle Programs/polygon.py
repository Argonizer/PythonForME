import turtle

distance = 50
ttl = turtle.Turtle()
ttl.speed(5)

def polygon(sides, length, color):
    ttl.color(color)
    for i in range(sides):
        ttl.forward(length)
        ttl.left(360/sides)

sides = 3
polygon(sides, distance, "red")

turtle.done