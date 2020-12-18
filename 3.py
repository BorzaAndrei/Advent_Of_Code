tree_map = []

with(open("input/3.txt")) as r:
    for line in r.readlines():
        row = []
        for ch in line.strip():
            if ch == '.':
                row.append(0)
            else:
                row.append(1)
        tree_map.append(row)


slopes = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2}
]
product = 1
for slope in slopes:
    count = 0
    row_ind = 0
    col_ind = 0
    while row_ind < len(tree_map) - 1:
        row_ind += slope["down"]
        col_ind += slope["right"]
        if col_ind >= len(tree_map[row_ind]):
            col_ind = col_ind - len(tree_map[row_ind])
        if tree_map[row_ind][col_ind] == 1:
            count += 1
    product *= count

print(product)
