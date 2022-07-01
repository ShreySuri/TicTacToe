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


while check_1 == 0:
    symbol_1 = input(print("Player 1, choose your symbol: circles, crosses, hearts, squares, or stars. "))
    symbol_1 = symbol_1.lower()
    for i in range (0, symbols_count):
        if symbols[i] == symbol_1:
            check_1 = check_1 + 1
        else:
            check_1 = check_1 + 0
            
while check_2 == 0:
    print("")
    symbol_2 = input(print("Player 2, choose your symbol: circles, crosses, hearts, squares, or stars. "))
    symbol_2 = symbol_2.lower()
    for i in range (0, symbols_count):
        if symbols[i] == symbol_2:
            check_2 = check_2 + 1
        else:
           check_2 = check_2 + 0
           
    if symbol_2 == symbol_1:
        check_2 = 0
        print("")
        print("This symbol has been selected by Player 1. Please choose a different signal.")
    else:
        toggle = True

t_grid = turtle.Pen()
t_grid.hideturtle()
t_grid.up()

width = 200
space = 10

t_grid.forward(width * 1.5)
t_grid.left(90)
t_grid.forward(width * 0.5)
t_grid.left(90)
for i in range (0,4):
    t_grid.down()
    t_grid.forward(width * 3)
    t_grid.up()
    t_grid.right(90)
    for j in range (0,2):
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
squares = []
occupied_count = 0
player_1_list = []
player_2_list = []

win = False


while win == False:

# Player 1

    checker = False

    while checker == False:

        guess_1 = 0
        while guess_1 % 1 != 0 or guess_1 < 1 or guess_1 > 9:
            print("")
            guess_1 = input(print("Player 1, please choose a square. Enter an integer from 1 to 9, inclusive. "))
            guess_1 = float(guess_1)
        guess_1 = int(guess_1)


        if occupied_count > 0:

            counter = 0
            
            for i in range (0, occupied_count):
                if squares[i] == guess_1:
                    counter = counter + 1
                else:
                    counter = counter

            if counter == 1:
                print("")
                print("This square has already been chosen. Please choose a different one.")
                checker = False
            else:
                print("")
                print("Marking square %s. " % guess_1)
                occupied_count = occupied_count + 1
                squares.append(guess_1)
                checker = True
        else:
            print("")
            print("Marking square %s. " % guess_1)
            occupied_count = occupied_count + 1
            squares.append(guess_1)
            checker = True


       
    guess_1 = guess_1 - 1
    x = guess_1 % 3
    y = int((guess_1 - x)/3)
    trinary = float(x + 0.1 * y)
    player_1_list.append(trinary)

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
        marker.up()
        marker.forward(20)
        marker.right(90)
        marker.forward(50)
        marker.left(180)
        marker.down()
        marker.begin_fill()
        for i in range (0,180):
            marker.forward(0.7)
            marker.right(1)
        marker.right(180)
        for i in range (0,180):
            marker.forward(0.7)
            marker.right(1)
        marker.right(30)
        marker.forward(160)
        marker.right(120)
        marker.forward(160)
        marker.right(30)
        marker.end_fill()
        marker.up()
        marker.forward(50)
        marker.left(90)
        marker.forward(20)

    elif symbol_1  == "squares":
        space = space * 2
        marker.up()
        marker.forward(space)
        marker.right(90)
        marker.forward(space)
        marker.left(90)
        marker.down()
        marker.begin_fill()
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

    marker.forward(x * width)
    marker.right(90)
    marker.forward(y * width)
    marker.right(90)


    print(player_1_list)

# Player 2

    checker = False

    while checker == False:

        guess_2 = 0
        while guess_2 % 1 != 0 or guess_2 < 1 or guess_2 > 9:
            print("")
            guess_2 = input(print("Player 2, please choose a square. Enter an integer from 1 to 9, inclusive. "))
            guess_2 = float(guess_2)
        guess_2 = int(guess_2)


        if occupied_count > 0:

            counter = 0
            
            for i in range (0, occupied_count):
                if squares[i] == guess_2:
                    counter = counter + 1
                else:
                    counter = counter

            if counter == 1:
                print("")
                print("This square has already been chosen. Please choose a different one.")
                checker = False
            else:
                print("")
                print("Marking square %s. " % guess_2)
                occupied_count = occupied_count + 1
                squares.append(guess_2)
                checker = True
        else:
            print("")
            print("Marking square %s. " % guess_2)
            occupied_count = occupied_count + 1
            squares.append(guess_2)
            checker = True

    guess_2 = guess_2 - 1    
    x = guess_2 % 3
    y = int((guess_2 - x)/3)
    trinary = float(x + 0.1 * y)
    player_2_list.append(trinary)


    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.left(90)
    marker.fillcolor(color_2)
    
    if symbol_2 == "circles":
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
    elif symbol_2 == "crosses":
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
    elif symbol_2 == "hearts":
        marker.up()
        marker.forward(20)
        marker.right(90)
        marker.forward(50)
        marker.left(180)
        marker.down()
        marker.begin_fill()
        for i in range (0,180):
            marker.forward(0.7)
            marker.right(1)
        marker.right(180)
        for i in range (0,180):
            marker.forward(0.7)
            marker.right(1)
        marker.right(30)
        marker.forward(160)
        marker.right(120)
        marker.forward(160)
        marker.right(30)
        marker.end_fill()
        marker.up()
        marker.forward(50)
        marker.left(90)
        marker.forward(20)
    elif symbol_2  == "squares":
        space = space * 2
        marker.up()
        marker.forward(space)
        marker.right(90)
        marker.forward(space)
        marker.left(90)
        marker.down()
        marker.begin_fill()
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
    elif symbol_2 == "stars":
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

    print(player_2_list)

