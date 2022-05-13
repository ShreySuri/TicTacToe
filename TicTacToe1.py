symbols = ["circles", "crosses", "hearts", "squares"]
symbols_count = 4

symbol_1 = None
symbol_2 = None
check_1 = 0
check_2 = 0

while check_1 == 0 and check_2 == 0:
    while check_1 == 0:
        symbol_1 = input(print("Player 1, choose your symbol: circles, crosses, hearts, or squares. "))
        symbol_1 = symbol_1.lower()
        for i in range (0, symbols_count):
            if symbols[i] == symbol_1:
                check_1 = check_1 + 1
            else:
                check_1 = check_1 + 0
    while check_2 == 0:
        symbol_2 = input(print("Player 2, choose your symbol: circles, crosses, hearts, or squares. "))
        symbol_2 = symbol_2.lower()
        for i in range (0, symbols_count):
            if symbols[i] == symbol_2:
                check_2 = check_2 + 1
            else:
                check_2 = check_2 + 0
            
import turtle

t_grid = turtle.Pen()
t_grid.hideturtle()
t_grid.up()

width = 200
space = 10

t_grid.forward(width * 1.5)
t_grid.left(90)
t_grid.forward(width * 0.5)
t_grid.left(90)
for i in range (1,5):
    t_grid.down()
    t_grid.forward(width * 3)
    t_grid.up()
    t_grid.right(90)
    for j in range (1,3):
        t_grid.forward(width)
        t_grid.right(90)

marker = turtle.Pen()
marker.hideturtle()
marker.up()
marker.right(180)
marker.forward(width * 1.5)
marker.right(90)
marker.forward(width * 1.5)
marker.right(90)
squares = [1, 2, 3, 4, 5,  6, 7, 8, 9]
vacant_squares = 9

win = True
vacancy = 0

while win == True:
    guess_1 = 0
    while guess_1 % 1 != 0 or guess_1 < 1 or guess_1 > 10 or vacancy == 0:
        guess_1 = input(print("Player 1, which square would you like to mark? 1 - 9. "))
        for i in range (0, vacant_squares):
            if squares[i] == guess_1:
                squares.remove[i]
                vacant_squares = vacant_squares - 1
                vacancy = vacancy + 1
            else:
                vacancy = vacancy + 0
            
    guess_1 = guess_1 - 1
    x = guess_1 % 3
    y = int((guess_1 - x)/3)
    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.left(90)
    
    if symbol_1 == "circles":
        marker.forward(width * 0.5)
        marker.right(90)
        marker.up()
        marker.forward(space)
        marker.right(90)
        marker.down()
        marker.circle(width * 0.5 - space)
        marker.up()
        marker.forward(width * 0.5)
        marker.right(90)
        marker.forward(space)
        marker.left(90)
    elif symbol_1 == "crosses"
        marker.right(45)
        marker.up()
        marker.forward(2 ** 0.5 * space)
        for i in range (1, 5):
            marker.forward((width - 2 * space) * 2 ** 0.5)
            marker.left(135)
            marker.up()
            marker.forward(width - 2 * space)
            marker.left(135)
            marker.down()
        marker.up()
        marker.right(180)
        marker.forward(2 ** 0.5 * space)
        marker.left(45)
    elif symbol_1  = "squares"
        marker.right(45)
        marker.up()
        marker.forward(2 ** 0.5 * space)
        marker.left(45)
        marker.down()
        for i in range (1, 5):
            marker.forward(width - 2 * space)
            marker.right(90)
        marker.right(180)
        marker.up()
        marker.forward(2 ** 0.5 * space)
        marker.left(45)
