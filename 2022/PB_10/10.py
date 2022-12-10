op_queue = []
cycle = 1
reg_x = 1
with open("input.txt") as file:
    for line in file.readlines():
        if 'noop' in line:
            op_queue.append(0)
        else:
            op_queue.append(0)
            op_queue.append(int(line.strip('\n').split()[1]))

# s = 0
while len(op_queue) > 0:
    el = op_queue.pop(0)
    if (cycle - 1) % 40 in [reg_x - 1, reg_x, reg_x + 1]:
        print('#', end='')
    else:
        print('.', end='')
    cycle += 1
    reg_x += el
    if cycle - 1 in [40, 80, 120, 160, 200, 240]:
        print()
        # s += reg_x * cycle

# print(s)
