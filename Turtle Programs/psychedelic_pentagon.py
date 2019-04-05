import turtle

distance = 50
ttl = turtle.Turtle()
ttl.speed(100)
for i in range(100):
    for color in ["red", "green", "blue", "purple"]:
        ttl.color(color)
        ttl.forward(distance)
        ttl.right(288)
    distance += 10
turtle.done()