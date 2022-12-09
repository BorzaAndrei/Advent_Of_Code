from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Snake:
    x: int
    y: int
    next: Optional[Snake]

    def move_direction(self, matrix, direction):
        dirs = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        self.x, self.y = self.x + dirs[direction][0], self.y + dirs[direction][1]
        prev = self
        current = self.next
        while current is not None:
            if current.next is None:
                current.follow_other(matrix, prev, True)
            else:
                current.follow_other(matrix, prev, False)
            prev = current
            current = current.next

    def follow_other(self, matrix, head: Snake, do_update):
        if self.should_move_after(head):
            x = self.x - head.x
            if x < 0:
                self.x += 1
            elif x > 0:
                self.x -= 1
            y = self.y - head.y
            if y < 0:
                self.y += 1
            elif y > 0:
                self.y -= 1
            if do_update:
                matrix[self.x][self.y] = 1

    def should_move_after(self, head: Snake):
        for row_ind in range(-1, 2):
            for col_ind in range(-1, 2):
                if head.x + row_ind == self.x and head.y + col_ind == self.y:
                    return False
        return True


DIMENSION = 1000
m = [[0 for _ in range(DIMENSION)] for _ in range(DIMENSION)]

count = 0

h = Snake(DIMENSION // 2, DIMENSION // 2, None)
parent = h
for _ in range(9):
    t = Snake(DIMENSION // 2, DIMENSION // 2, None)
    parent.next = t
    parent = t
m[h.x][h.y] = 1
with open("input.txt") as file:
    for line in file.readlines():
        way, steps = line.strip('\n').split()
        for _ in range(int(steps)):
            h.move_direction(m, way)

print(sum(1 for row in m for el in row if el == 1))
