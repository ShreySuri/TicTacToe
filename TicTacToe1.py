import turtle
import random
import time

def vert_checker(list_1, counter):
    int_list = []
    for i in range (0, counter):
        rem = list_1[i] % 1
        int_1 = int(list_1[i] - rem)
        int_list.append(int_1)

    int_list.sort()
    for i in range (0, 2):
        int_list.append(10)
    
    def_counter = False
    for i in  range (0, counter):
        if int_list[i] == int_list[i+1] and int_list[i] == int_list[i+2]:
            def_counter = True
        else:
            def_counter = def_counter

    return(def_counter)
            

def hori_checker(list_1, counter_1):
    rem_list = []
    for i in range (0, counter_1):
        a = list_1[i] * 10
        b = int(a % 10)
        rem_list.append(b)

    c = vert_checker(rem_list, counter_1)
    return(c)


def diag_checker_1(list_1, counter):
    def_counter = 0
    for i in range (0, counter):
        if list_1[i] == 0.0 or list_1[i] == 1.1 or list_1[i] == 2.2:
            def_counter = def_counter + 1
        else:
            def_counter = def_counter

    if def_counter == 3:
        def_counter = True
    else:
        def_counter = False

    return(def_counter)

def diag_checker_2(list_1, counter):
    def_counter = 0
    for i in range (0, counter):
        if list_1[i] == 0.2 or list_1[i] == 1.1 or list_1[i] == 2.0:
            def_counter = def_counter + 1
        else:
            def_counter = def_counter

    if def_counter == 3:
        def_counter = True
    else:
        def_counter = False

    return(def_counter)




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
list_1_counter = 0
list_2_counter = 0

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
    list_1_counter = list_1_counter + 1

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

    l = vert_checker(player_1_list, list_1_counter)
    m = hori_checker(player_1_list, list_1_counter)
    n = diag_checker_1(player_1_list, list_1_counter)
    o = diag_checker_2(player_1_list, list_1_counter)

    if l == True or m == True or n == True or o == True:
        print("")
        print("Player 1 wins!")
        time.sleep(3600)
    else:
        toggle = True

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
    list_2_counter = list_2_counter + 1

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

    l = vert_checker(player_2_list, list_2_counter)
    m = hori_checker(player_2_list, list_2_counter)
    n = diag_checker_1(player_2_list, list_2_counter)
    o = diag_checker_2(player_2_list, list_2_counter)

    if l == True or m == True or n == True or o == True:
        win = True
    else:
        toggle = False


print("")
print("Player 2 wins!")
    

