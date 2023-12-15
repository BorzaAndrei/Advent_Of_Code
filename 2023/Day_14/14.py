from dataclasses import dataclass
from functools import cache


class Platform:

    def __init__(self, lines):
        self.max_h = len(lines)
        self.max_w = len(lines[0].strip('\n'))
        self.rocks = {}
        for x, line in enumerate(lines):
            for y, ch in enumerate(line.strip('\n')):
                if ch in ('O', '#'):
                    self.rocks[(x, y)] = ch
    
    def first_free_pos_in_direction(self, start, direction):
        x, y = 0, 0
        match direction:
            case 'N':
                x = -1
            case 'S':
                x = 1
            case 'E':
                y = 1
            case 'W':
                y = -1
        current_pos = start
        while 0 <= current_pos[0] + x < self.max_h and 0 <= current_pos[1] + y < self.max_w and (current_pos[0] + x, current_pos[1] + y) not in self.rocks.keys():
            current_pos = (current_pos[0] + x, current_pos[1] + y)
        return current_pos

    def order_rocks(self, direction):
        match direction:
            case 'N':
                first_arg, second_arg, rev = 0, 1, False
            case 'S':
                first_arg, second_arg, rev = 0, 1, True
            case 'E':
                first_arg, second_arg, rev = 1, 0, True
            case 'W':
                first_arg, second_arg, rev = 1, 0, False
        return list(filter(lambda rock: self.rocks[rock] == 'O', sorted(self.rocks.keys(), key=lambda rock: (rock[first_arg], rock[second_arg]), reverse=rev)))
    
    def tilt_direction(self, direction):
        ordered_rocks_keys = self.order_rocks(direction)
        for rock in ordered_rocks_keys:
            free_pos = self.first_free_pos_in_direction(rock, direction)
            if rock != free_pos:
                self.rocks[free_pos] = self.rocks[rock]
                del self.rocks[rock]
    
    def calculate_load(self, direction):
        # s = 0
        # for rockKey in self.order_rocks(direction):
        #     match direction:
        #         case 'N':
        #             h, p = self.max_h, rockKey[0]
        #         case 'S':
        #             h, p = self.max_h, -rockKey[0]
        #         case 'E':
        #             h, p = self.max_w, -rockKey[1]
        #         case 'W':
        #             h, p = self.max_w, rockKey[1]
        #     s += (h - p)
        # return s
        return sum([self.max_h - rockKey[0] for rockKey in self.order_rocks(direction)])
    
    def __str__(self) -> str:
        s = ""
        for l in range(self.max_h):
            for c in range(self.max_w):
                if (l, c) in self.rocks.keys():
                    s += self.rocks[(l, c)]
                else:
                    s += '.'
            s += '\n'
        return s


file = open("2023/Day_14/input.txt")

platform = Platform(file.readlines())
file.close()

past_iters = {}
no_cycles = 1000000000
for cycle in range(no_cycles):
    platform.tilt_direction('N')
    platform.tilt_direction('W')
    platform.tilt_direction('S')
    platform.tilt_direction('E')
    current_hash = hash(tuple(sorted(platform.rocks.items())))
    if current_hash in past_iters.keys():
        previous_cycles = past_iters[current_hash]
        cycles_length = cycle - previous_cycles

        remaining_cycles = no_cycles - cycle
        remaining_steps = remaining_cycles % cycles_length - 1

        for _ in range(remaining_steps):
            platform.tilt_direction('N')
            platform.tilt_direction('W')
            platform.tilt_direction('S')
            platform.tilt_direction('E')
        print(platform.calculate_load('N'))
        break
    else:
        past_iters[current_hash] = cycle
print(platform.calculate_load('N'))
