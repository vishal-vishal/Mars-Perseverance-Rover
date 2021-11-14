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
rover.goto(-160,160)
rover.pendown()

rover.speed(5)

#Mission 6
rover.right(80)
rover.forward(200)
rover.left(20)
rover.forward(130)
rover.left(80)
rover.forward(80)
rover.left(35)
rover.forward(250)
rover.left(90)
rover.forward(50)
