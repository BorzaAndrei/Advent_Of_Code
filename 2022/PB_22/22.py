def find_start(b, m_line, m_col):
    for x in range(0, m_line + 1):
        for y in range(0, m_col + 1):
            if (x, y) in b and b[(x, y)] == '.':
                return x, y


def move(b, x, y, d, steps):
    if steps == 0:
        return x, y, d
    new_x = x + d[0]
    new_y = y + d[1]
    if (new_x, new_y) in b and b[(new_x, new_y)] == '.':
        return move(b, new_x, new_y, d, steps - 1)
    elif (new_x, new_y) in b and b[(new_x, new_y)] == '#':
        return x, y, d
    match (x, y):
        # 1 -> 6
        case (0, y) if 50 <= y <= 99 and d == (-1, 0):
            if b[(y + 100, 0)] == '#':
                return x, y, d
            return move(b, y + 100, 0, (0, 1), steps - 1)

        # 2 -> 6
        case (0, y) if 100 <= y <= 149 and d == (-1, 0):
            if b[(199, y - 100)] == '#':
                return x, y, d
            return move(b, 199, y - 100, (-1, 0), steps - 1)

        # 1 -> 5
        case (x, y) if 0 <= x <= 49 and y == 50 and d == (0, -1):
            if b[(149 - x, 0)] == '#':
                return x, y, d
            return move(b, 149 - x, 0, (0, 1), steps - 1)

        # 3 -> 5
        case (x, y) if 50 <= x <= 99 and y == 50 and d == (0, -1):
            if b[(100, x - 50)] == '#':
                return x, y, d
            return move(b, 100, x - 50, (1, 0), steps - 1)

        # 2 -> 4
        case (x, y) if 0 <= x <= 49 and y == 149 and d == (0, 1):
            if b[(149 - x, 99)] == '#':
                return x, y, d
            return move(b, 149 - x, 99, (0, -1), steps - 1)

        # 3 -> 2
        case (x, y) if 50 <= x <= 99 and y == 99 and d == (0, 1):
            if b[(49, x + 50)] == '#':
                return x, y, d
            return move(b, 49, x + 50, (-1, 0), steps - 1)

        # 5 -> 3
        case (x, y) if x == 100 and 0 <= y <= 49 and d == (-1, 0):
            if b[(y + 50, 50)] == '#':
                return x, y, d
            return move(b, y + 50, 50, (0, 1), steps - 1)

        # 5 -> 1
        case (x, y) if 100 <= x <= 149 and y == 0 and d == (0, -1):
            if b[(149 - x, 50)] == '#':
                return x, y, d
            return move(b, 149 - x, 50, (0, 1), steps - 1)

        # 6 -> 1
        case (x, y) if 150 <= x <= 199 and y == 0 and d == (0, -1):
            if b[(0, x - 100)] == '#':
                return x, y, d
            return move(b, 0, x - 100, (1, 0), steps - 1)

        # 4 -> 2
        case (x, y) if 100 <= x <= 149 and y == 99 and d == (0, 1):
            if b[(149 - x), 149] == '#':
                return x, y, d
            return move(b, 149 - x, 149, (0, -1), steps - 1)

        # 6 -> 4
        case (x, y) if 150 <= x <= 199 and y == 49 and d == (0, 1):
            if b[(149, x - 100)] == '#':
                return x, y, d
            return move(b, 149, x - 100, (-1, 0), steps - 1)

        # 2 -> 3
        case (x, y) if x == 49 and 100 <= y <= 149 and d == (1, 0):
            if b[(y - 50, 99)] == '#':
                return x, y, d
            return move(b, y - 50, 99, (0, -1), steps - 1)

        # 4 -> 6
        case (x, y) if x == 149 and 50 <= y <= 99 and d == (1, 0):
            if b[(y + 100, 49)] == '#':
                return x, y, d
            return move(b, y + 100, 49, (0, -1), steps - 1)

        # 6 -> 2
        case (x, y) if x == 199 and 0 <= y <= 49 and d == (1, 0):
            if b[(0, y + 100)] == '#':
                return x, y, d
            return move(b, 0, y + 100, (1, 0), steps - 1)
    # Wrap around for part 1
    # match d:
    # case (0, 1):
    #     col = 0
    #     while (x, col) not in b:
    #         col += 1
    #     if b[(x, col)] == '#':
    #         return x, y
    #     else:
    #         return move(b, x, col, d, steps - 1)
    # case (0, -1):
    #     col = max([f[1] for f in board])
    #     while (x, col) not in b:
    #         col -= 1
    #     if b[(x, col)] == '#':
    #         return x, y
    #     else:
    #         return move(b, x, col, d, steps - 1)
    # case (1, 0):
    #     li = 0
    #     while (li, y) not in b:
    #         li += 1
    #     if b[(li, y)] == '#':
    #         return x, y
    #     else:
    #         return move(b, li, y, d, steps - 1)
    # case (-1, 0):
    #     li = max([f[0] for f in board])
    #     while (li, y) not in b:
    #         li -= 1
    #     if b[(li, y)] == '#':
    #         return x, y
    #     else:
    #         return move(b, li, y, d, steps - 1)


def rotate(current_dir, new_dir):
    match new_dir:
        case 'R':
            dir_next = {
                (0, 1): (1, 0),
                (1, 0): (0, -1),
                (0, -1): (-1, 0),
                (-1, 0): (0, 1)
            }
            return dir_next[current_dir]
        case 'L':
            dir_prev = {
                (0, 1): (-1, 0),
                (1, 0): (0, 1),
                (0, -1): (1, 0),
                (-1, 0): (0, -1)
            }
            return dir_prev[current_dir]


board = {}
move_set = ""

with open("input.txt") as file:
    line_ind = -1
    for line in file.readlines():
        if '#' in line or '.' in line:
            line_ind += 1
            col_ind = 0
            for ch in line.strip('\n'):
                if ch == '.' or ch == '#':
                    board[(line_ind, col_ind)] = ch
                col_ind += 1
        if 'R' in line or 'L' in line:
            move_set = line.strip()

max_line, max_col = max([f[0] for f in board]), max([f[1] for f in board])

start_x, start_y = find_start(board, max_line, max_col)
current_x, current_y = start_x, start_y
mov_set_ind = 0
read_number = True
direction = (0, 1)
while mov_set_ind < len(move_set):
    if read_number:
        no_string = ""
        while mov_set_ind < len(move_set) and move_set[mov_set_ind] in '0123456789':
            no_string += move_set[mov_set_ind]
            mov_set_ind += 1
        read_number = False
        current_x, current_y, direction = move(board, current_x, current_y, direction, int(no_string))
    else:
        rl = move_set[mov_set_ind]
        mov_set_ind += 1
        read_number = True
        direction = rotate(direction, rl)

print(f"x={current_x + 1}, y={current_y + 1}, direction={direction}")
match direction:
    case (0, 1):
        d_no = 0
    case (1, 0):
        d_no = 1
    case (0, -1):
        d_no = 2
    case _:
        d_no = 3
print((current_x + 1) * 1000 + (current_y + 1) * 4 + d_no)
