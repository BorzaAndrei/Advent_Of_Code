from dataclasses import dataclass
from typing import Tuple, List
from copy import deepcopy


@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x}, {self.y})"


@dataclass
class Wind:
    position: Point
    direction: Tuple[int, int]

    def update(self, max_x, max_y):
        new_x, new_y = self.position.x + self.direction[0], self.position.y + self.direction[1]
        if new_x >= max_x - 1:
            new_x = 1
        elif new_x <= 0:
            new_x = max_x - 2

        if new_y >= max_y - 1:
            new_y = 1
        elif new_y <= 0:
            new_y = max_y - 2
        self.position.x, self.position.y = new_x, new_y

        return self.position.x, self.position.y


@dataclass
class Valley:
    map: List[List[int]]
    winds: List[Wind]

    def update_winds(self):
        max_x, max_y = len(self.map), len(self.map[0])
        for w in self.winds:
            self.map[w.position.x][w.position.y] -= 1
            x, y = w.update(max_x, max_y)
            self.map[x][y] += 1

    def print_valley(self):
        for l in self.map:
            print(l)
        print()


def generate_x_valleys(start_valley: Valley, x):
    valleys = [deepcopy(start_valley)]
    for _ in range(x):
        start_valley.update_winds()
        valleys.append(deepcopy(start_valley))
    return valleys


def bfs(valley: Valley, start_pos, start_time: int, end_pos):
    q = {start_pos}
    max_x = len(valley.map)
    max_y = len(valley.map[0])
    for minute in range(1000):
        valley.update_winds()
        next_q = set()
        for p in q:
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                new_x, new_y = p[0] + d[0], p[1] + d[1]
                if 0 <= new_x < max_x and 0 <= new_y < max_y and valley.map[new_x][new_y] == 0:
                    new_point = (new_x, new_y)
                    next_q.add(new_point)
        if (end_pos[0], end_pos[1]) in next_q:
            return minute + 1
        q = next_q


new_map = []
winds = []
with open("input.txt") as file:
    for line_ind, line in enumerate(file.readlines()):
        new_line = []
        for col_ind, ch in enumerate(line.strip('\n')):
            if ch == '#':
                new_line.append(1)
            elif ch == '.':
                new_line.append(0)
            else:
                if ch == '>':
                    direction = (0, 1)
                elif ch == '<':
                    direction = (0, -1)
                elif ch == 'v':
                    direction = (1, 0)
                else:
                    direction = (-1, 0)
                wind = Wind(Point(line_ind, col_ind), direction)
                winds.append(wind)
                new_line.append(1)
        new_map.append(new_line)

valley = Valley(new_map, winds)
start_pos = (0, valley.map[0].index(0))
end_pos = (len(valley.map) - 1, valley.map[-1].index(0))

print(f"Trip 1 in {bfs(valley, start_pos, 0, end_pos)} minutes")
print(f"Trip 2 in {bfs(valley, end_pos, 0, start_pos)} minutes")
print(f"Trip 3 in {bfs(valley, start_pos, 0, end_pos)} minutes")
