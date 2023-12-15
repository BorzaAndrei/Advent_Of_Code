from functools import cache
from itertools import product
import re
from typing import List
import time


class Record:
    row: List[str]
    springs: List[int]

    def __init__(self, row, springs) -> None:
        # Part 1
        # self.row = [ch for ch in row]
        # self.springs = list(map(int, springs.split(',')))

        # Part 2
        self.row = [ch for ch in row + '?'] * 5
        self.row.pop()
        self.springs = list(map(int, springs.split(','))) * 5

    def __str__(self) -> str:
        r = "".join(self.row)
        s = ",".join(list(map(str, self.springs)))
        return f"{r} - {s}"
    
    def valid(self, row):
        text = "".join(row)
        matches = re.findall(r'#+', text)
        if row.count('#') != sum(self.springs) or len(matches) != len(self.springs):
            return False
        for ind, match in enumerate(matches):
            if len(match) != self.springs[ind]:
                return False
        return True
    
    @staticmethod
    def count_groups_of_hashes(s):
        # Use regular expression to find all consecutive groups of "#"
        text = "".join(s)
        matches = re.findall(r'#+', text)

        # Count the number of matches
        return len(matches)
    
    def count_valid_possibilities(self):
        # Find indices of "?" characters
        question_mark_indices = [i for i, c in enumerate(self.row) if c == '?']

        # Generate all combinations of replacement values
        replacement_values = product(".#", repeat=len(question_mark_indices))

        # Replace "?" characters with generated values
        count = 0
        for values in replacement_values:
            possibility = list(self.row)
            for i, value in zip(question_mark_indices, values):
                possibility[i] = value
            if self.valid(possibility):
                count += 1

        return count

records: List[Record] = []

with open("2023/Day_12/input.txt") as r:

    for line in r.readlines():
        if len(line) > 0:
            split = line.strip('\n').split(' ')
            records.append(Record(split[0], split[1]))

start_time = time.time()

s = 0
for ind, r in enumerate(records):
    # if ind % 10 == 0:
    print(ind)
    s += r.count_valid_possibilities()

# print(sum([r.count_valid_possibilities() for r in records]))

end_time = time.time()

print(end_time - start_time)
