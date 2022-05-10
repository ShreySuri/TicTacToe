symbols = ["circles", "crosses", "hearts"]
symbols_count = 3

symbol_1 = None
symbol_2 = None
check_1 = 0
check_2 = 0

while symbol_1 == symbol_2:
    while check_1 == 0:
        symbol_1 = input(print("Player 1, choose your symbol: circles, crosses, or hearts. "))
        symbol_1 = symbol_1.lower()
        for i in range (0, symbols_count):
            if symbol[i] == symbol_1:
                check_1 = check_1 + 1
            else:
                check_1 = check_1 + 0
    while check_2 == 0:
        symbol_2 = input(print("Player 2, choose your symbol: circles, crosses, or hearts. "))
        symbol_2 = symbol_2.lower()
        for i in range (0, symbols_count):
            if symbol[i] == symbol_1:
                check_1 = check_1 + 1
            else:
                check_1 = check_1 + 0
            

S
