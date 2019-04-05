import turtle

distance = 50
ttl = turtle.Turtle()
ttl.speed(100)
for i in range(20):
    for color in ["red", "green", "blue", "purple", "black"]:
        ttl.color(color)
        ttl.forward(distance)
        ttl.right(144)
        distance += 10
turtle.done()