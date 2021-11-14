import turtle
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(500, 500)
screen.bgpic("mars-path-2.png")

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

#Mission 3
angle = 90
width = 340
hight = 50
for i in range(5):
    rover.forward(width)
    rover.left(angle)
    rover.forward(hight)
    rover.left(angle)
    rover.forward(width)
    rover.right(angle)
    rover.forward(hight)
    rover.right(angle)
