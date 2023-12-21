from dataclasses import dataclass, field
from typing import Dict
import copy

slashMirror = {
    "E": "S",
    "W": "N",
    "N": "W",
    "S": "E"
}

backspaceMirror = {
    "E": "N",
    "W": "S",
    "N": "E",
    "S": "W"
}

@dataclass
class Position:
    x: int
    y: int
    type: str
    visitedFromDirection: Dict[str, bool] = field(default_factory=lambda :{
        "S": False,
        "N": False,
        "W": False,
        "E": False
    })

    def anyVisited(self) -> bool:
        return any(self.visitedFromDirection[direction] for direction in self.visitedFromDirection)


@dataclass
class Beam:
    x: int
    y: int
    direction: str
    max_x: int = 0
    max_y: int = 0
    stopped: bool = False

    def get_next_pos(self, positions):
        match self.direction:
            case "S":
                if 0 <= self.x + 1 < self.max_x and not positions[(self.x + 1, self.y)].visitedFromDirection['N']:
                    positions[(self.x + 1, self.y)].visitedFromDirection['N'] = True
                    return positions[(self.x + 1, self.y)]
                else:
                    return None
            case "N":
                if 0 <= self.x - 1 < self.max_x and not positions[(self.x - 1, self.y)].visitedFromDirection['S']:
                    positions[(self.x - 1, self.y)].visitedFromDirection['S'] = True
                    return positions[(self.x - 1, self.y)]
                else:
                    return None
            case "E":
                if 0 <= self.y + 1 < self.max_y and not positions[(self.x, self.y + 1)].visitedFromDirection['W']:
                    positions[(self.x, self.y + 1)].visitedFromDirection['W'] = True
                    return positions[(self.x, self.y + 1)]
                else:
                    return None
            case "W":
                if 0 <= self.y - 1 < self.max_y and not positions[(self.x, self.y - 1)].visitedFromDirection['E']:
                    positions[(self.x, self.y - 1)].visitedFromDirection['E'] = True
                    return positions[(self.x, self.y - 1)]
                else:
                    return None


class BeamRepo:

    def __init__(self, positions, starting_beam):
        self.beams = [starting_beam]
        self.positions = positions
    
    def update(self):
        for beam in self.beams:
            if not beam.stopped:
                next_pos = beam.get_next_pos(self.positions)
                if next_pos:
                    beam.x, beam.y = next_pos.x, next_pos.y
                    match next_pos.type:
                        case ".":
                            pass # Good
                        case "|":
                            if beam.direction in ('E', 'W'):
                                beam.direction = 'S'
                                self.beams.append(Beam(next_pos.x, next_pos.y, 'N', beam.max_x, beam.max_y))
                        case "-":
                            if beam.direction in ('N', 'S'):
                                beam.direction = 'E'
                                self.beams.append(Beam(next_pos.x, next_pos.y, 'W', beam.max_x, beam.max_y))
                        case "\\":
                            beam.direction = slashMirror[beam.direction]
                        case "/":
                            beam.direction = backspaceMirror[beam.direction]
                else:
                    beam.stopped = True


    def solve(self):
        while not all([beam.stopped for beam in self.beams]):
            self.update()
            self.beams = list(filter(lambda x: not x.stopped, self.beams))



positions = {}
with open("2023/Day_16/input.txt") as r:
    lines = r.readlines()
    max_x, max_y  = len(lines), len(lines[0].strip('\n'))
    for ind_l, line in enumerate(lines):
        for ind_c, ch in enumerate(line.strip('\n')):
            positions[(ind_l, ind_c)] = Position(ind_l, ind_c, ch)

m = -1
for l in range(max_x):
    print(f"Line: {l}")
    beamRepo = BeamRepo(copy.deepcopy(positions), Beam(l, -1, 'E', max_x, max_y))
    beamRepo.solve()
    count = sum([1 if beamRepo.positions[pos].anyVisited() == True else 0 for pos in beamRepo.positions])
    if count > m:
        m = count

    beamRepo = BeamRepo(copy.deepcopy(positions), Beam(l, max_y, 'W', max_x, max_y))
    beamRepo.solve()
    count = sum([1 if beamRepo.positions[pos].anyVisited() == True else 0 for pos in beamRepo.positions])
    if count > m:
        m = count

for c in range(max_y):
    print(f"Col: {c}")
    beamRepo = BeamRepo(copy.deepcopy(positions), Beam(-1, c, 'S', max_x, max_y))
    beamRepo.solve()
    count = sum([1 if beamRepo.positions[pos].anyVisited() == True else 0 for pos in beamRepo.positions])
    if count > m:
        m = count

    beamRepo = BeamRepo(copy.deepcopy(positions), Beam(max_x, c, 'N', max_x, max_y))
    beamRepo.solve()
    count = sum([1 if beamRepo.positions[pos].anyVisited() == True else 0 for pos in beamRepo.positions])
    if count > m:
        m = count
print(m)
# for l in range(max_x):
#     for c in range(max_y):
#         print('#' if beamRepo.positions[(l, c)].anyVisited() else '.', end='')
#     print()
