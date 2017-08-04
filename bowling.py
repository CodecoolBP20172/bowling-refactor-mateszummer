def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            result += get_value(game[i+1])
            if game[i].upper() == 'X':
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        if game[i].upper() == 'X':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char.upper() == 'X':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
