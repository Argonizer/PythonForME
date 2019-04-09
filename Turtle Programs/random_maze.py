import turtle
import random

distance = 300
wall_thickness = 10
ttl = turtle.Turtle()
ttl.speed(5)

def maze_layer(length, wall_thickness, color):
    ttl.color(color)
    for i in range(3):
        ttl.forward(length)
        ttl.right(90)
    rand_len = random.randint(0.2 * length, 0.8 * length)
    ttl.forward(rand_len)
    ttl.right(90)
    ttl.forward(wall_thickness)
    ttl.right(90)
    ttl.forward(rand_len - wall_thickness)
    for(i) in range(3):
        ttl.left(90)
        ttl.forward(length - 2 * wall_thickness)
    ttl.left(90)
    ttl.forward(length - rand_len - 2*wall_thickness)
    ttl.right(90)
    ttl.forward(wall_thickness)
    ttl.right(90)
    ttl.forward(length - rand_len - wall_thickness)
    ttl.right(90)
    ttl.forward(length - 2 * wall_thickness)
    ttl.right(90)
    ttl.penup()
    ttl.forward(2 * wall_thickness)
    ttl.pendown()
ttl.penup()
ttl.goto(-200, 200)
ttl.pendown()
color_list = ["red", "orange", "purple", "green"]
while(distance >= 4 * wall_thickness):
    color = color_list[random.randint(0, 3)]
    maze_layer(distance, wall_thickness, color)
    distance -= 4 * wall_thickness

turtle.done()