# Chris French 24.04.2020 - Epicycloid Generator using Python Turtle
#test
# Turtle Setup
import turtle
wn = turtle.Screen()
wn.bgcolor("light Blue")
wn.title("Turtle")
t = turtle.Turtle()
t.hideturtle()
t._tracer(0)
# test
# variable inputs
multiplier = int(input("what do you want the multiplier to be?"))
steps = int(input("How many steps do you want?"))
coordinates = {}

def PLotNumbers():
    global coordinates
    rotate = 360/steps
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    for i in range (steps):
        t.goto(0,0)
        t.forward(200)
        t.dot()
        CurrentPos = t.pos()
        coordinates[i] = (CurrentPos)
        t.left(rotate)


def ConnectNumbers():
    global coordinates
    for i in range(len(coordinates)):
        firstCoord = coordinates[i]
        # find the number to connect it to
        multiplied = int(i)*multiplier
        while multiplied >= steps: # if it too big, loop over
            multiplied = multiplied - steps
        # get the coord of the second number
        secondCoord = coordinates[multiplied]
        # draw the lines
        t.penup()
        t.goto(firstCoord)
        t.pendown()
        t.goto(secondCoord)

PLotNumbers()
ConnectNumbers()
turtle.done()