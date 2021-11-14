import turtle
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(500, 500)
screen.bgpic("mars-path-4.png")

# Initialise the rover...
rover = turtle.Turtle()
# screen.addshape('rover.png')
# rover.shape('rover.png')
rover.shape("square")
rover.speed(100)

rover.color("#810000")
rover.pensize(4)
rover.penup()
rover.goto(-160,-135)
rover.pendown()

rover.speed(5)

# Mission 5
rover.left(17)
rover.forward(230)
rover.left(45)
rover.forward(150)
rover.left(107)
rover.forward(205)
rover.left(80)
rover.forward(250)
