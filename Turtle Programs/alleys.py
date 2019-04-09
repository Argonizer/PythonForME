import turtle

distance = 50
ttl = turtle.Turtle()
ttl.speed(100)
for i in range(4):
    for j in range(10):
        for direction in ["right", "left"]:
            ttl.color("green")
            ttl.forward(distance)
            if direction == "right":
                ttl.right(90)
            else:
                ttl.left(90)
            ttl.forward(10)
            if direction == "right":
                ttl.right(90)
            else:
                ttl.left(90)
    ttl.right(90)
turtle.done()