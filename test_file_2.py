


    def_counter = 0
    bool_def_counter = False
    for i in range (0, 3):
        target_rem = i * 0.1
        for i in range (0, counter):
            rem = list_1[i] % 1
            if rem == target_rem:
                def_counter = def_counter + 1
            else:
                def_counter = def_counter + 0

        if def_counter == 3:
            bool_def_counter = True
        else:
            bool_def_counter = bool_def_counter

    return(bool_def_counter)
