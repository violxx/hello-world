import turtle
def drawSquare(sides,length):
    angle = 360/sides
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)
drawSquare(360,40)
turtle.done()
