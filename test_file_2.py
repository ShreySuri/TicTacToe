import turtle

marker = turtle.Pen()

width = 200
space = 10




marker.left(90)
for i in range (0, 5):
    marker.forward(width)
    marker.right(90)






fill_color = red
space = space * 2
marker.up()
marker.forward(space)
marker.right(90)
marker.forward(space)
marker.left(90)
marker.down()
marker.begin_fill(red)
length = width - 2 * space
for i in range (0, 4):
    marker.forward(length)
    marker.right(90)
marker.end_fill()
marker.up()
marker.left(90)
marker.forward(space)
marker.left(90)
marker.forward(space)
space = int(space * 0.5)
