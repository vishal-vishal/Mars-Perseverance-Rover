
import turtle
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(500, 500)
screen.bgpic("mars-path-3.png")

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

# Mission 4
# Implement Rover Path...
size = 320
for i in range(0, 340, 20):
    rover.forward(size)
    rover.left(90)
    size -= 20

