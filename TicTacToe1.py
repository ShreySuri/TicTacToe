symbols = ["circles", "crosses", "hearts"]
symbols_count = 3

symbol_1 = None
symbol_2 = None
check_1 = 0
check_2 = 0

while check_1 == 0 and check_2 == 0:
    while check_1 == 0:
        symbol_1 = input(print("Player 1, choose your symbol: circles, crosses, or hearts. "))
        symbol_1 = symbol_1.lower()
        for i in range (0, symbols_count):
            if symbols[i] == symbol_1:
                check_1 = check_1 + 1
            else:
                check_1 = check_1 + 0
    while check_2 == 0:
        symbol_2 = input(print("Player 2, choose your symbol: circles, crosses, or hearts. "))
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

width = 100

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
    
