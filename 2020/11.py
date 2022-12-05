def count_adjacent(seats, center_row, center_col):
    count = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if 0 <= center_row + i < len(seats) and 0 <= center_col + j < len(seats[i]) and not (i == 0 and j == 0):
                if seats[center_row + i][center_col + j] == '#':
                    count += 1
    return count


def count_adjacent_directions(seats, center_row, center_col):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for direction in directions:
        interaction = False
        x = center_row + direction[0]
        y = center_col + direction[1]
        while 0 <= x < len(seats) and 0 <= y < len(seats[x]) and seats[x][y] == '.':
            x += direction[0]
            y += direction[1]
        if 0 <= x < len(seats) and 0 <= y < len(seats[x]):
            if seats[x][y] == '#':
                count += 1
    return count


def execute_round(seats):
    changes = 0
    copy_seats = [[char for char in row] for row in seats]
    for row_index in range(len(copy_seats)):
        for col_index in range(len(copy_seats[row_index])):
            if copy_seats[row_index][col_index] == 'L' and count_adjacent_directions(copy_seats, row_index, col_index) == 0:
                seats[row_index][col_index] = '#'
                changes += 1
            elif copy_seats[row_index][col_index] == '#' and count_adjacent_directions(copy_seats, row_index, col_index) >= 5:
                seats[row_index][col_index] = 'L'
                changes += 1
    return changes


def print_map(seats):
    for row in seats:
        print(row)
    print()


def count_occupied(seats):
    count = 0
    for row in seats:
        for char in row:
            if char == '#':
                count += 1
    return count


seat_map = []
with open("input/11.txt") as r:
    for line in r.readlines():
        r = []
        for ch in line.strip():
            r.append(ch)
        seat_map.append(r)

while execute_round(seat_map) != 0:
    pass

# print_map(seat_map)
print(count_occupied(seat_map))
