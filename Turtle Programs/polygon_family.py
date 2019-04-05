import turtle

distance = 50
ttl = turtle.Turtle()
ttl.speed(100)

def polygon(sides, length, color):
    for i in range(sides):
        ttl.forward(length)
        ttl.color(color)
        ttl.left(360/sides)

sides = 3
for i in range(10):
    for color in ["red","purple", "green", "blue"]:
        polygon(sides, distance, color)
        sides += 1
turtle.done()