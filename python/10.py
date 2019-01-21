import turtle
def drawSquare(sides,length):
    angle = 360/sides
    turtle.fillcolor('green')
    turtle.begin_fill()
    for again in range(sides):
        turtle.forward(length)
        turtle.right(angle)
def moveTurtle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
drawSquare(4,30)
moveTurtle(100,100)
drawSquare(5,30)
turtle.end_fill()
moveTurtle(-100,100)
drawSquare(6,40)
turtle.done()
