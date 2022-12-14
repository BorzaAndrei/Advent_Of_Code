import math
from string import ascii_lowercase

mapping = {letter: ind for ind, letter in enumerate(ascii_lowercase)}
m = []
start_x, start_y = -1, -1
end_x, end_y = -1, -1
with open("input.txt") as file:
    line_no = 0
    for line in file.readlines():
        row = []
        for ch_ind, ch in enumerate(line.strip('\n')):
            if ch == 'S':
                start_x, start_y = line_no, ch_ind
                row.append(0)
            elif ch == 'E':
                end_x, end_y = line_no, ch_ind
                row.append(25)
            else:
                row.append(mapping[ch])
        m.append(row)
        line_no += 1

bfs_steps = [[-1 for _ in range(len(m[0]))] for _ in range(len(m))]


def bfs(matrix, steps, s_row, s_col, e_row, e_col):
    q = []
    steps[s_row][s_col] = 0
    q.append((s_row, s_col))
    dirs = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]
    while len(q) > 0:
        el_x, el_y = q.pop(0)
        if el_x == e_row and el_y == e_col:
            return steps[el_x][el_y]
        for direction in dirs:
            n_x, n_y = el_x + direction[0], el_y + direction[1]
            if n_x < 0 or n_x >= len(matrix) or n_y < 0 or n_y >= len(matrix[0]):
                continue
            if (steps[n_x][n_y] == -1 or steps[el_x][el_y] + 1 < steps[n_x][n_y]) \
                    and (matrix[n_x][n_y] == matrix[el_x][el_y]
                         or matrix[n_x][n_y] - 1 == matrix[el_x][el_y]
                         or matrix[n_x][n_y] < matrix[el_x][el_y]
            ):
                steps[n_x][n_y] = steps[el_x][el_y] + 1
                q.append((n_x, n_y))
    return math.inf


print(bfs(m, bfs_steps, start_x, start_y, end_x, end_y))
print(min([bfs(m, [[-1 for _ in range(len(m[0]))] for _ in range(len(m))], x_row, x_col, end_x, end_y) for x_row in range(len(m)) for x_col in range(len(m[x_row])) if m[x_row][x_col] == 0]))
