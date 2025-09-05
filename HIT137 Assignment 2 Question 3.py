import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")

# Function for modifying the shape's edges
def shape_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        depth = depth - 1
        shape_edge(t, length, depth)
        t.right(60)
        shape_edge(t, length, depth)
        t.left(120)
        shape_edge(t, length, depth)
        t.right(60)
        shape_edge(t, length, depth)

# Function for drawing the shape using Turtle
def draw_shape(sides, length, depth):
    angle = 360 / sides
    t.speed(0)
    t.penup()
    t.setposition(-length/2, length/2)
    t.pendown()
    for _ in range(sides):
        shape_edge(t, length, depth)
        t.right(angle)
    t.hideturtle()
    turtle.done()

# Customizes the shape sides, length, and recursion depth
sides = int(input("Input the number of sides: "))
length = int(input("Input the length of each side: "))
depth = int(input("Input the recursion depth of the shape: "))

# Draws the shape in Turtle
draw_shape(sides, length, depth)

