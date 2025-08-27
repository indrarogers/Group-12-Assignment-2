import turtle

# Function for modifying the shape's edges
def shape_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        shape_edge(t, length, depth - 1)
        t.right(60)
        shape_edge(t, length, depth - 1)
        t.left(120)
        shape_edge(t, length, depth - 1)
        t.right(60)
        shape_edge(t, length, depth - 1)

# Function for drawing the shape using Turtle
def draw_shape(sides, length, depth):
    angle = 360 / sides
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()
    for _ in range(sides):
        shape_edge(turtle, length, depth)
        turtle.right(angle)
    turtle.hideturtle()
    turtle.done()

# Customizes the shape sides, length, and recursion depth
sides = int(input("Input the number of sides: "))
length = int(input("Input the length of each side: "))
depth = int(input("Input the recursion depth of the shape: "))

# Draws the shape in Turtle
draw_shape(sides, length, depth)

