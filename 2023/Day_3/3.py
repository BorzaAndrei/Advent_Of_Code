from dataclasses import dataclass, field
import re
from typing import List, Set, ForwardRef
from functools import reduce


@dataclass
class Position:
    x: int
    y: int
    symbol: ForwardRef('Symbol') = None

    def __str__(self) -> str:
        return f"Pos({self.x}, {self.y})"
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


@dataclass
class Number:
    value: int
    positions: List[Position]
    used: bool = False

    def __str__(self) -> str:
        return f"{self.value} - {self.used}: {self.positions}"
    
    def __bool__(self):
        return self.used
    
    def __hash__(self):
        return hash((self.value, str(self.positions)))
    

@dataclass
class Symbol:
    value: str
    position: Position
    neighbourCount: int = 0
    neighbours: Set[Number] = field(default_factory=set)

    def __str__(self) -> str:
        return f"{self.value} - {self.position} - {self.neighbourCount} - {self.neighbours}"
    
    def __bool__(self):
        return self.neighbourCount == 2

symbols_re = r'[@\/\$&\+\-#%\*=]'
symbols: List[Symbol] = []
numbers: List[Number] = []

with open("input.txt") as r:

    for ind, line in enumerate(r.readlines()):
        for mtch in re.finditer(symbols_re, line.strip('\n')):
            symbols.append(Symbol(mtch.group(0), Position(ind, mtch.start())))
        for mtch in re.finditer('\d+', line.strip('\n')):
            positions = [Position(ind, y) for y in range(mtch.start(), mtch.end())]
            numbers.append(Number(value=int(mtch.group(0)), positions=positions))

neighbour_positions = []
for symbol in symbols:
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x != 0 or y != 0:
                neighbour_positions.append(Position(symbol.position.x + x, symbol.position.y + y, symbol))

# Part 1
for number in numbers:
    for pos in number.positions:
        try:
            ind = neighbour_positions.index(pos)
            if neighbour_positions[ind].symbol.value == '*' and number.used is False:
                neighbour_positions[ind].symbol.neighbourCount += 1
                neighbour_positions[ind].symbol.neighbours.add(number)
            number.used = True
        except ValueError:
            pass


print(sum(map(lambda n: n.value, filter(None, numbers))))

print(sum(map(lambda symbol: reduce(lambda x, y: x * y, [n.value for n in symbol.neighbours]), filter(None, symbols))))
