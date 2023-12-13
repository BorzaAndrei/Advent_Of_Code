# .....
# .F-7.
# .|.|.
# .L-J.
# .....

from dataclasses import dataclass
import queue
from typing import ForwardRef, List

@dataclass
class Pipe:
    x: int
    y: int
    type: str
    n1: ForwardRef("Pipe") = None
    n2: ForwardRef("Pipe") = None
    step: int = 0

    def __str__(self) -> str:
        if self.n1 and self.n2:
            return f"Pipe({self.x}, {self.y}), Type: {self.type}, Step: {self.step}, n1:{self.n1.x}/{self.n1.y}, n2:{self.n2.x}/{self.n2.y}"
        elif self.n1:
            return f"({self.x}, {self.y}) - {self.type} - n1:{self.n1.x}/{self.n1.y}"
        elif self.n2:
            return f"({self.x}, {self.y}) - {self.type} - n2:{self.n2.x}/{self.n2.y}"
        else:
            return f"({self.x}, {self.y}) - {self.type}"
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


def how_many_wall_in_direction(matrix, element, direction):
    current_x, current_y = element[0], element[1]
    s = 0
    while 0 <= current_x < len(matrix) and 0 <= current_y < len(matrix[0]):
        if matrix[current_x][current_y] == 2:
            s += 1
        current_x += direction[0]
        current_y += direction[1]
    return s


pipes: List[Pipe] = []
matrix = []
with open("2023/Day_10/input.txt") as r:

    for ind_x, line in enumerate(r.readlines()):
        row = []
        for ind_y, ch in enumerate(line.strip('\n')):
            if ch != '.':
                pipes.append(Pipe(ind_x, ind_y, ch))
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)


    start_pipe = None
    
    for p in pipes:
        
        n1_x, n1_y, n2_x, n2_y = -1, -1, -1, -1
        match p.type:
            case '|':
                n1_x, n1_y, n2_x, n2_y = p.x - 1, p.y, p.x + 1, p.y
            case '-':
                n1_x, n1_y, n2_x, n2_y = p.x, p.y + 1, p.x, p.y - 1
            case 'L':
                n1_x, n1_y, n2_x, n2_y = p.x - 1, p.y, p.x, p.y + 1
            case 'F':
                n1_x, n1_y, n2_x, n2_y = p.x, p.y + 1, p.x + 1, p.y
            case 'J':
                n1_x, n1_y, n2_x, n2_y = p.x, p.y - 1, p.x - 1, p.y
            case '7':
                n1_x, n1_y, n2_x, n2_y = p.x, p.y - 1, p.x + 1, p.y
            case 'S':
                start_pipe = p

        for n in pipes:
            if n.x == n1_x and n.y == n1_y:
                p.n1 = n
                if n.type == 'S':
                    if n.n1 is None:
                        n.n1 = p
                    else:
                        n.n2 = p
            elif n.x == n2_x and n.y == n2_y:
                p.n2 = n
                if n.type == 'S':
                    if n.n1 is None:
                        n.n1 = p
                    else:
                        n.n2 = p
    
    dif1 = (start_pipe.n1.x - start_pipe.x, start_pipe.n1.y - start_pipe.y)
    dif2 = (start_pipe.n2.x - start_pipe.x, start_pipe.n2.y - start_pipe.y)
    match (dif1, dif2):
        case ((0, 1), (1, 0)):
            start_pipe.type = 'F'
        case ((1, 0), (0, 1)):
            start_pipe.type = 'F'
        case ((0, -1), (-1, 0)):
            start_pipe.type = 'J'
        case ((-1, 0), (0, -1)):
            start_pipe.type = 'J'
    
    print("Finished reading")
    visited_pipes: List[Pipe] = [start_pipe]
    q = queue.Queue()
    q.put(start_pipe)
    while not q.empty():
        current_pipe = q.get()
        if current_pipe.type not in ('F', 'J'):
            matrix[current_pipe.x][current_pipe.y] = 2
        else:
            matrix[current_pipe.x][current_pipe.y] = 3
        if current_pipe.n1 not in visited_pipes:
            visited_pipes.append(current_pipe.n1)
            current_pipe.n1.step = current_pipe.step + 1
            q.put(current_pipe.n1)
        if current_pipe.n2 not in visited_pipes:
            visited_pipes.append(current_pipe.n2)
            current_pipe.n2.step = current_pipe.step + 1
            q.put(current_pipe.n2)
    
    print(max([p.step for p in pipes]))

    for r in matrix:
        print(r)

    s = 0
    for ind_r in range(len(matrix)):
        for ind_c in range(len(matrix[ind_r])):
            if matrix[ind_r][ind_c] in (0, 1):
                s += how_many_wall_in_direction(matrix, (ind_r, ind_c), (-1, 1)) % 2
    
    print(s)
