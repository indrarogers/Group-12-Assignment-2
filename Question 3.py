import turtle

def shape_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        shape_edge(t, length, depth - 1)
        t.left(60)
        shape_edge(t, length, depth - 1)
        t.right(120)
        shape_edge(t, length, depth - 1)
        t.left(60)
        shape_edge(t, length, depth - 1)

def draw_shape(sides, length, depth):
    angle = 360 / sides
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-length/2, 0)
    turtle.pendown()
    for _ in range(sides):
        shape_edge(turtle, length, depth)
        turtle.right(angle)
    turtle.hideturtle()
    turtle.done()

sides = int(input("Input the number of sides: "))
length = int(input("Input the length of each side: "))
depth = int(input("Input the recursion depth of the shape: "))

draw_shape(sides, length, depth)