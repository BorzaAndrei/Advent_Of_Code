from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
import operator
from functools import reduce


@dataclass
class Monkey:
    id: int
    items: List[int]
    op_sign: chr
    op_no: int
    test_no: int
    test_true: Optional[Monkey]
    test_false: Optional[Monkey]
    test_ids: List[int]
    inspections = 0

    def operation(self, old):
        other = self.op_no if self.op_no != -1 else old
        match self.op_sign:
            case '*':
                return old * other  # // 3
            case '+':
                return old + other  # // 3

    def test(self, item):
        if item % self.test_no == 0:
            self.test_true.items.append(item)
        else:
            self.test_false.items.append(item)

    def do_round(self, modulo):
        for _ in range(len(self.items)):
            self.inspections += 1
            item = self.items.pop(0)
            new_item = self.operation(item) % modulo
            self.test(new_item)

    def find_matching(self, other_monkeys: List[Monkey]):
        self.test_true = [m for m in other_monkeys if m.id == self.test_ids[0]][0]
        self.test_false = [m for m in other_monkeys if m.id == self.test_ids[1]][0]

    def __str__(self):
        return f"Monkey: {self.id} | M-True: {self.test_true.id} | M-False: {self.test_false.id}"


monkeys = []
with open("input.txt") as file:
    file.seek(0, 2)
    eof = file.tell()
    file.seek(0, 0)
    while file.tell() != eof:
        line_id = int(file.readline().split()[1].strip('\n').strip(':'))
        items_line = file.readline()
        starting_items = [int(x.strip().strip('\n')) for x in items_line[items_line.find(':') + 1:].split(', ')]
        operation_line = file.readline()
        operation = operation_line[operation_line.find('=') + 1:].split()
        op_sign = operation[1]
        op_no = int(operation[2]) if 'old' not in operation[2] else -1
        test_no = int(file.readline().split()[-1])
        test_true_id = int(file.readline().split()[-1])
        test_false_id = int(file.readline().split()[-1])
        file.readline()
        mo = Monkey(line_id, starting_items, op_sign, op_no, test_no, None, None, [test_true_id, test_false_id])
        monkeys.append(mo)

for monkey in monkeys:
    monkey.find_matching(monkeys)

modulo = reduce(operator.mul, [m.test_no for m in monkeys])  # Rahat
for round in range(10000):
    print(round)
    for mo in monkeys:
        mo.do_round(modulo)

monkeys.sort(key=lambda m: m.inspections, reverse=True)
print(monkeys[0].inspections * monkeys[1].inspections)
