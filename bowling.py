def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            result += get_value(game[i + 1])
            if game[i].upper() == 'X':
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        if game[i].upper() == 'X':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    chars = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
             "7": 7, "8": 8, "9": 9, "X": 10, "/": 10, "-": 0}
    if char.upper() in chars:
        return chars[char.upper()]
    else:
        raise ValueError()
