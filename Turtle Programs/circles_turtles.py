import turtle

distance = 150
ttl = turtle.Turtle()
ttl.speed(300)
for i in range(10):
    for color in ["purple", "orange"]:
        ttl.color(color)
        ttl.circle(distance)
        ttl.right(45)
    distance -= 10
turtle.done()