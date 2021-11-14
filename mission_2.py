import turtle
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(500, 500)
screen.bgpic("mars-path-1.png")

# Initialise the rover...
rover = turtle.Turtle()
# screen.addshape('rover.png')
# rover.shape('rover.png')
rover.shape("square")
rover.speed(100)


rover.color("#810000")
rover.pensize(4)
rover.penup()
rover.goto(-165,-165)
rover.pendown()

rover.speed(5)

#Mission 2
for i in range(4):
    rover.forward(340)
    rover.left(90)
