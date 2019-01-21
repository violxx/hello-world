import turtle
sides = int(raw_input('please input how many sides do you want draw: \n'))
length = 200/sides
angle = 360/sides
for again in range(sides):
    turtle.forward(length)
    turtle.right(angle)
turtle.done()
