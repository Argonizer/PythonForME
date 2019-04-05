import turtle

distance = 100
ttl = turtle.Turtle()
ttl.speed(100)
for i in range(10):
    for color in ["red", "green", "blue", "purple", "black"]:
        ttl.color(color)
        ttl.circle(distance)
        ttl.right(72)
        distance -= 10
turtle.done()