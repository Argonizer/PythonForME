import turtle

distance = 10
ttl = turtle.Turtle()
ttl.speed(100)
for i in range(40):
    for color in ["red","purple", "green", "blue"]:
        ttl.color(color)
        ttl.circle(distance)
        ttl.right(60)
        distance += 2
turtle.done()