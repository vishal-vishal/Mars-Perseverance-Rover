#Mars Perseverance Rover - Challenge #5 - www.101computing.net/mars-perseverance-rover/
import turtle
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400)
screen.bgpic("mars-path-5.png")

# Initialise the rover...
rover = turtle.Turtle()
screen.addshape("rover.png")
rover.shape("rover.png")
rover.speed(100)

rover.color("#810000")
rover.pensize(4)
rover.penup()
rover.goto(-40,-160)
rover.pendown()

# Mission 7
#Implement Rover Path...
for i in range(12):
    rover.forward(90)
    rover.left(30)
