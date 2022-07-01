import turtle

marker = turtle.Pen()

width = 200
space = 10




marker.left(90)
for i in range (0, 5):
    marker.forward(width)
    marker.right(90)




marker.up()
marker.right(45)
marker.forward(25)
marker.right(90)
marker.down()
marker.begin_fill()
for i in range (0, 4):
    marker.forward(15)
    marker.left(90)
    marker.forward(100)
    marker.right(90)
    marker.forward(100)
    marker.left(90)
    marker.forward(15)
marker.end_fill()
marker.up()
marker.right(90)
marker.forward(25)
marker.left(45)
