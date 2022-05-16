import turtle
import random

symbols = ["circles", "crosses", "hearts", "squares", "stars"]
symbols_count = 5

colors = ["red", "pink", "orange","yellow","green","teal","blue","indigo","purple", "tan"]
color_picker= random.randint(0,9)
color_1 = colors[color_picker]
color_2 = color_1
while color_2 == color_1:
    color_picker = random.randint(0,9)
    color_2 = colors[color_picker]

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

win = False


while win == False:

# Player 1

    guess_1 = 0
    checker = 0
    while checker == 0:
        while guess_1 % 1 != 0 or guess_1 < 1 or guess_1 > 10 or vacancy == 0:
            guess_1 = input(print("Player 1, which square would you like to mark? 1 - 9. "))
        for i in range (0,9):
            if guess_1 == squares[i]:
                checker = checker + 1
                squares[i] = "placeholder"
            else:
                print("That square has already been chosen. ")
                
    guess_1 = guess_1 - 1
    x = guess_1 % 3
    y = int((guess_1 - x)/3)
    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.left(90)
    marker.fillcolor(color_1)
    
    if symbol_1 == "circles":
        marker.forward(width * 0.5)
        marker.right(90)
        marker.up()
        marker.forward(space)
        marker.right(90)
        marker.down()
        marker.begin_fill()
        marker.circle(width * 0.5 - space)
        marker.end_fill()
        marker.up()
        marker.forward(width * 0.5)
        marker.right(90)
        marker.forward(space)
        marker.left(90)
    elif symbol_1 == "crosses":
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
    elif symbol_1 == "hearts":
        marker.right(45)
        marker.up()
        marker.forward(20)
        marker.right(90)
        marker.forward(45)
        marker.right(180)
        marker.down()
        marker.begin_fill()
        for i in range (1,181):
            marker.forward(0.7)
            marker.right(1)
        marker.right(180)
        for i in range (1,181):
            marker.forward(0.7)
            marker.right(1)
        marker.right(30)
        marker.forward(160)
        marker.right(120)
        marker.forward(160)
        marker.right(30)
        marker.end_fill()
        marker.up()
        marker.forward(45)
        marker.left(90)
        marker.forward(space)
    elif symbol_1  == "squares":
        marker.forward(2 ** 0.5 * space)
        marker.left(45)
        marker.down()
        marker.begin_fill()
        for i in range (1, 5):
            marker.forward(width - 2 * space)
            marker.right(90)
        marker.right(180)
        marker.end_fill()
        marker.up()
        marker.forward(2 ** 0.5 * space)
        marker.left(45)
    elif symbol_1 == "stars":
        marker.up()
        marker.forward(space)
        marker.right(90)
        marker.forward(80)
        marker.left(90)
        marker.down()
        marker.begin_fill()
        for i in range (1,6):
            marker.forward(70)
            marker.left(72)
            marker.forward(70)
            marker.right(144)
        marker.end_fill()
        marker.up()
        marker.left(90)
        marker.forward(80)
        marker.left(90)
        marker.forward(space)

    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.right(90)

# Player 2

    guess_1 = 0
    checker = 0
    while checker == 0:
        while guess_1 % 1 != 0 or guess_1 < 1 or guess_1 > 10 or vacancy == 0:
            guess_1 = input(print("Player 1, which square would you like to mark? 1 - 9. "))
        for i in range (0,9):
            if guess_1 == squares[i]:
                checker = checker + 1
                squares[i] = "placeholder"
            else:
                print("That square has already been chosen. ")
                
    guess_1 = guess_1 - 1
    x = guess_1 % 3
    y = int((guess_1 - x)/3)
    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.left(90)
    marker.fillcolor(color_1)
    
    if symbol_1 == "circles":
        marker.forward(width * 0.5)
        marker.right(90)
        marker.up()
        marker.forward(space)
        marker.right(90)
        marker.down()
        marker.begin_fill()
        marker.circle(width * 0.5 - space)
        marker.end_fill()
        marker.up()
        marker.forward(width * 0.5)
        marker.right(90)
        marker.forward(space)
        marker.left(90)
    elif symbol_1 == "crosses":
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
    elif symbol_1 == "hearts":
        marker.right(45)
        marker.up()
        marker.forward(20)
        marker.right(90)
        marker.forward(45)
        marker.right(180)
        marker.down()
        marker.begin_fill()
        for i in range (1,181):
            marker.forward(0.7)
            marker.right(1)
        marker.right(180)
        for i in range (1,181):
            marker.forward(0.7)
            marker.right(1)
        marker.right(30)
        marker.forward(160)
        marker.right(120)
        marker.forward(160)
        marker.right(30)
        marker.end_fill()
        marker.up()
        marker.forward(45)
        marker.left(90)
        marker.forward(space)
    elif symbol_1  == "squares":
        marker.forward(2 ** 0.5 * space)
        marker.left(45)
        marker.down()
        marker.begin_fill()
        for i in range (1, 5):
            marker.forward(width - 2 * space)
            marker.right(90)
        marker.right(180)
        marker.end_fill()
        marker.up()
        marker.forward(2 ** 0.5 * space)
        marker.left(45)
    elif symbol_1 == "stars":
        marker.up()
        marker.forward(space)
        marker.right(90)
        marker.forward(80)
        marker.left(90)
        marker.down()
        marker.begin_fill()
        for i in range (1,6):
            marker.forward(70)
            marker.left(72)
            marker.forward(70)
            marker.right(144)
        marker.end_fill()
        marker.up()
        marker.left(90)
        marker.forward(80)
        marker.left(90)
        marker.forward(space)

    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.right(90)

