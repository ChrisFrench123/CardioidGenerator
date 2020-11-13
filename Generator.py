# Chris French 24.04.2020 - Epicycloid Generator using Python Turtle
import turtle


class EpicycloidGenerator:
    def __init__(self):
        self.coords = {}

        # User Inputs
        self.multiplier = int(input("What do you want the multiplier to be? "))
        self.steps = int(input("How many steps do you want? "))

        ### Turtle Setup ###
        self.wn = turtle.Screen()       # Create Screen
        self.wn.bgcolor("light Blue")   # Set the colour
        self.wn.title("Turtle")         # Set name of window

        self.t = turtle.Turtle()        # Create Turtle
        self.t.hideturtle()             # Remove the Turtle body
        self.t._tracer(0)                # Remove the tracing

    def plot_numbers(self):
        rotate = 360/self.steps
        self.t.penup()
        self.t.goto(0, 0)
        self.t.setheading(0)
        for i in range(self.steps):
            self.t.goto(0, 0)
            self.t.forward(200)
            self.t.dot()
            current_pos = self.t.pos()
            self.coords[i] = current_pos
            self.t.left(rotate)

    # I have changed some stuff for the Drawing Branch
    def connect_numbers(self):
        for i in range(len(self.coords)):
            first_coord = self.coords[i]
            # find the number to connect it to
            multiplied = int(i)*self.multiplier
            while multiplied >= self.steps: # if it too big, loop over
                multiplied = multiplied - self.steps
            # get the coord of the second number
            second_coord = self.coords[multiplied]
            # draw the lines
            self.t.penup()
            self.t.goto(first_coord)
            self.t.pendown()
            self.t.goto(second_coord)

    def draw(self):
        self.plot_numbers()
        self.connect_numbers()
        turtle.done()


if __name__ == '__main__':
    drawer = EpicycloidGenerator()
    drawer.draw()
