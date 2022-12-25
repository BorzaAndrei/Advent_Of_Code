from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Direction:
    name: str
    positions: List[Tuple[int, int]]


direction_cycle = [
    Direction("N", [(-1, -1), (-1, 0), (-1, 1)]),
    Direction("S", [(1, -1), (1, 0), (1, 1)]),
    Direction("W", [(-1, -1), (0, -1), (1, -1)]),
    Direction("E", [(-1, 1), (0, 1), (1, 1)])
]

elf_positions = set()
ind_line = 10
with open("input.txt") as file:
    for line in file.readlines():
        ind_col = 10
        for ch in line.strip('\n'):
            if ch == '#':
                elf_positions.add((ind_line, ind_col))
            ind_col += 1
        ind_line += 1

all_stopped = False
r = 0
while not all_stopped:
    print(f"Still simulating... round={r}")
    all_stopped = True
    marked_to_move = {}
    for elf in elf_positions:
        # Check if he is alone
        alone = True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (elf[0] + x, elf[1] + y) in elf_positions:
                    if x == 0 and y == 0:
                        continue
                    alone = False
        if not alone:
            all_stopped = False
            # Find the direction to move
            for direction in direction_cycle:
                empty = True
                for d in direction.positions:
                    if (elf[0] + d[0], elf[1] + d[1]) in elf_positions:
                        empty = False
                        break

                if empty:
                    match direction.name:
                        case 'N':
                            if (elf[0] - 1, elf[1]) not in marked_to_move:
                                marked_to_move[(elf[0] - 1, elf[1])] = []
                            marked_to_move[(elf[0] - 1, elf[1])].append((elf[0], elf[1]))
                        case 'E':
                            if (elf[0], elf[1] + 1) not in marked_to_move:
                                marked_to_move[(elf[0], elf[1] + 1)] = []
                            marked_to_move[(elf[0], elf[1] + 1)].append((elf[0], elf[1]))
                        case 'S':
                            if (elf[0] + 1, elf[1]) not in marked_to_move:
                                marked_to_move[(elf[0] + 1, elf[1])] = []
                            marked_to_move[(elf[0] + 1, elf[1])].append((elf[0], elf[1]))
                        case 'W':
                            if (elf[0], elf[1] - 1) not in marked_to_move:
                                marked_to_move[(elf[0], elf[1] - 1)] = []
                            marked_to_move[(elf[0], elf[1] - 1)].append((elf[0], elf[1]))
                    break

    for new_pos in marked_to_move:
        if len(marked_to_move[new_pos]) > 1:
            continue
        elf_positions.remove(marked_to_move[new_pos][0])
        elf_positions.add(new_pos)
    d = direction_cycle.pop(0)
    direction_cycle.append(d)

    r += 1

    # min_x, min_y = min(e[0] for e in elf_positions), min(e[1] for e in elf_positions)
    # max_x, max_y = max(e[0] for e in elf_positions), max(e[1] for e in elf_positions)
    # for x in range(min_x, max_x + 1):
    #     for y in range(min_y, max_y + 1):
    #         if (x, y) in elf_positions:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # print()
print(r)
min_x, min_y = min(e[0] for e in elf_positions), min(e[1] for e in elf_positions)
max_x, max_y = max(e[0] for e in elf_positions), max(e[1] for e in elf_positions)
c = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if (x, y) in elf_positions:
            pass
        else:
            c += 1
print(c)
