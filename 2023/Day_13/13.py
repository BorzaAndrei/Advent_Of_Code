from dataclasses import field, dataclass
from functools import reduce
from typing import Set, Tuple


@dataclass
class Matrix:
    max_h: int
    max_w: int
    rocks: Set[Tuple[(int, int)]] = field(default_factory=set)

    def __str__(self) -> str:
        s = ""
        ordered_rocks = list(sorted(self.rocks, key=lambda rock: (rock[0], rock[1])))
        for ind_l in range(self.max_h):
            for ind_c in range(self.max_w):
                if (ind_l, ind_c) in ordered_rocks:
                    s += "#"
                else:
                    s += "."
            s += "\n"
        return s
    
    def all_rocks_on_column_or_line(self, ind, isLine=True):
        if isLine:
            return list(filter(lambda rock: rock[0] == ind, self.rocks))
        else:
            return list(filter(lambda rock: rock[1] == ind, self.rocks))
    
    @staticmethod
    def hash_rocks(rocks, isLine=True):
        if isLine:
            return sum([rock[1] + 1 for rock in rocks])
        else:
            return sum([rock[0] + 1 for rock in rocks])
    
    def find_mirror(self):
        for ind1, ind2 in ((self.max_h // 2 - 1, self.max_h // 2), (self.max_h // 2, self.max_h // 2 + 1)):
            mirror = True
            cp_ind1, cp_ind2 = ind1, ind2
            for _ in range(self.max_h // 2):
                if self.hash_rocks(self.all_rocks_on_column_or_line(cp_ind1)) != self.hash_rocks(self.all_rocks_on_column_or_line(cp_ind2)):
                    mirror = False
                    break
                cp_ind1 -= 1
                cp_ind2 += 1
            if mirror:
                return 100 * (ind1 + 1)
        
        for ind1, ind2 in ((self.max_w // 2 - 1, self.max_w // 2), (self.max_w // 2, self.max_w // 2 + 1)):
            mirror = True
            cp_ind1, cp_ind2 = ind1, ind2
            for _ in range(self.max_w // 2):
                if self.hash_rocks(self.all_rocks_on_column_or_line(cp_ind1, False), False) != self.hash_rocks(self.all_rocks_on_column_or_line(cp_ind2, False), False):
                    mirror = False
                    break
                cp_ind1 -= 1
                cp_ind2 += 1
            if mirror:
                return ind2
        return 0


matrixes = []
with open("2023/Day_13/input.txt") as r:
    lines = r.readlines()
    lines.extend(["\n"])
    ind_l = 0
    max_w = 0
    rocks = set()
    for line in lines:
        if len(line.strip('\n')) == 0:
            matrixes.append(Matrix(max_h=ind_l, max_w=max_w + 1, rocks=rocks.copy()))
            ind_l = 0
            max_w = 0
            rocks = set()
            continue
        for ind_c, ch in enumerate(line.strip("\n")):
            if ind_c > max_w:
                max_w = ind_c
            if ch == "#":
                rocks.add((ind_l, ind_c))
        ind_l += 1

print(sum([matrix.find_mirror() for matrix in matrixes]))
