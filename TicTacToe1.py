import turtle
import random

def int_checker(x, y, z):
    if x <= y:
        def_final = False
    else:
        def_final = 0

    if z == 1 or z == 2:
        def_final = 0
    else:
        def_final = False
        
    if def_final == 0:
        x = str(x)
        y = str(y)
        z = str(z)
        def_check = False
        
        while def_check == False:
            print("")
            def_input = input(print("Player %s, please choose a square. Enter an integer from %s to %s, inclusive. " % (z, x, y)))
            def_input = float(def_input)

            if def_input % 1 == 0 and def_input >= x and def_input <= y:
                def_check == True
                def_input = int(def_input)
            else:
                def_check = False

        def_final = def_check
        
    else:
        def_toggle = True

    return(def_final)


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
    symbol_1 = input(print("Player 1, choose your symbol: circles, crosses, hearts, or squares. "))
    symbol_1 = symbol_1.lower()
    for i in range (0, symbols_count):
        if symbols[i] == symbol_1:
            check_1 = check_1 + 1
        else:
            check_1 = check_1 + 0
            
while check_2 == 0:
    print("")
    symbol_2 = input(print("Player 2, choose your symbol: circles, crosses, hearts, or squares. "))
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
player_1_list = []
occupied_count = 0

win = False


while win == False:

# Player 1

    checker = None

    while checker = None or checker = False:

        guess_1 = int_checker(1, 9, 1)

        if occupied_count > 0:
            for i in range(0, occupied_count):
                if squares[i] == guess_1:
                    checker = False
                else:
                    checker = checker

            if checker == False:
                print("")
                print("This square has already been chosen. Please choose a different one.")
                checker = False
            else:
                occupied_count = occupied_count + 1
                squares.append(guess_1)
                checker = True
                print("Marking square %s." % guess_1)
          
        else:
            occupied_count = occupied_count + 1
            squares.append(guess_1)
            checker = True
            print("Marking square %s." % guess_1)


    guess_1 = guess_1 - 1
    x = guess_1 % 3
    y = int((guess_1 - x)/3)
    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.left(90)
    marker.fillcolor(color_1)
    trinary = 10 * x + y
    player_1_list.append(trinary)
    
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

    checker = None

    while checker = None or checker = False:

        guess_2 = int_checker(1, 9, 2)

        if occupied_count > 0:
            for i in range(0, occupied_count):
                if squares[i] == guess_1:
                    checker = False
                else:
                    checker = checker

            if checker == False:
                print("")
                print("This square has already been chosen. Please choose a different one.")
                checker = False
            else:
                occupied_count = occupied_count + 1
                squares.append(guess_2)
                checker = True
                print("Marking square %s." % guess_2)
          
        else:
            occupied_count = occupied_count + 1
            squares.append(guess_2)
            checker = True
            print("Marking square %s." % guess_2)


    
    guess_2 = guess_2 - 2
    x = guess_2 % 3
    y = int((guess_2 - x)/3)
    marker.forward(width * x)
    marker.right(90)
    marker.forward(width * y)
    marker.left(90)
    marker.fillcolor(color_1)
    trinary = 10 * x + y
    player_2_list.append(trinary)
    
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
    elif symbol_2  == "squares":
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

