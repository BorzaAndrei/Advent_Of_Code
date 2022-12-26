import math


def snafu_to_dec(snafu):
    no = 0
    ind = len(snafu) - 1
    for ch in snafu:
        if ch == '0' or ch == '1' or ch == '2':
            no += int(ch) * pow(5, ind)
        elif ch == '-':
            no += pow(5, ind) * -1
        else:
            no += pow(5, ind) * -2
        ind -= 1
    return no


def dec_to_snafu(original_no):
    try_list = []
    for ind in range(0, 20):
        for el in range(-2, 3):
            new_no = abs(original_no - pow(5, ind) * el)
            try_list.append((new_no, ind, el))
    try_list.sort(key=lambda x: x[0])
    while len(try_list) > 0:
        to_try = try_list.pop(0)
        snafu = f"{to_try[2]}"
        no = original_no
        no = no - pow(5, to_try[1]) * to_try[2]
        max_ind = to_try[1]
        max_ind -= 1
        while max_ind >= 0:
            min_no = math.inf
            found_el = 0
            for el in range(-2, 3):
                new_no = abs(no - pow(5, max_ind) * el)
                if new_no < min_no:
                    min_no = new_no
                    found_el = el
            match found_el:
                case 0 | 1 | 2:
                    snafu += str(found_el)
                case -1:
                    snafu += '-'
                case -2:
                    snafu += '='
            no = no - pow(5, max_ind) * found_el
            max_ind -= 1
        if no == 0:
            return snafu
    return "Pula"


decoded_numbers = []
with open("input.txt") as file:
    for line in file:
        decoded_numbers.append(snafu_to_dec(line.strip()))

print(dec_to_snafu(sum(decoded_numbers)))
