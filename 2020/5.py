import math


def calculate_id(seat):
    lower_row, higher_row = 0, 127
    lower_col, higher_col = 0, 7
    for letter in seat:
        if letter == 'F':
            higher_row = (lower_row + higher_row) // 2
        elif letter == 'B':
            lower_row = math.ceil((lower_row + higher_row) / 2)
        elif letter == 'R':
            lower_col = math.ceil((lower_col + higher_col) / 2)
        else:
            higher_col = (lower_col + higher_col) // 2
    return higher_row * 8 + higher_col


with open("input/5.txt") as r:
    ids = [calculate_id(seat.strip()) for seat in r.readlines()]
    min_no = min(ids) - 1
    max_no = max(ids)
    # print(max_no) # Solution to 1)
    full_sum = max_no * (max_no + 1) / 2
    small_sum = min_no * (min_no + 1) / 2
    print(full_sum - small_sum - sum(ids))
