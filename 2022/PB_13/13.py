from __future__ import annotations

from dataclasses import dataclass
from functools import cmp_to_key
from typing import List, Optional

import regex_spm


@dataclass
class ListStack:
    elements: List[int | ListStack]
    parent: Optional[ListStack]


def build(pair):
    current_stack = ListStack([], None)

    no = []
    for ch in pair:
        match regex_spm.fullmatch_in(ch):
            case r'\[':
                new_stack = ListStack([], current_stack)
                current_stack.elements.append(new_stack)
                current_stack = new_stack
            case r'^[-+]?[0-9]+$':
                no.append(ch)
            case r'\]':
                if len(no):
                    current_stack.elements.append(int(''.join(no)))
                    no = []
                current_stack = current_stack.parent
            case r',':
                if len(no):
                    current_stack.elements.append(int(''.join(no)))
                    no = []
    return current_stack


def in_order(left, right):
    if isinstance(left, ListStack) and isinstance(right, ListStack):
        return compare_lists(left.elements, right.elements)
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 'T'
        elif left == right:
            return 'C'
        else:
            return 'F'
    elif isinstance(left, ListStack) and isinstance(right, int):
        return compare_lists(left.elements, ListStack([right], None).elements)
    elif isinstance(left, int) and isinstance(right, ListStack):
        return compare_lists(ListStack([left], None).elements, right.elements)


def compare_lists(left, right):
    ind_l = 0
    ind_r = 0
    order = True
    while ind_l < len(left) and ind_r < len(right) and order:
        result = in_order(left[ind_l], right[ind_r])
        match result:
            case 'T':
                return 'T'
            case 'F':
                return 'F'
            case 'C':
                ind_l += 1
                ind_r += 1
    if ind_l == len(left) and ind_r == len(right):
        return 'C'
    elif ind_l == len(left):
        return 'T'
    else:
        return 'F'


def compare_pairs_str(pair_left, pair_right):
    stack_l = build(pair_left)
    stack_r = build(pair_right)

    match compare_lists(stack_l.elements, stack_r.elements):
        case 'T':
            return 1
        case 'C':
            return 0
        case _:
            return -1


def part1():
    with open("input.txt") as file:
        fp = None
        pair = 1
        s = 0
        for line in file.readlines():
            if len(line.strip('\n')) > 0:
                if fp is None:
                    fp = line.strip('\n')
                else:
                    r = compare_pairs_str(fp, line.strip('\n'))
                    match r:
                        case 'T':
                            s += pair
                        case _:
                            pass
                    fp = None
                    pair += 1
        print(s)


def part2():
    pairs = ['[[2]]', '[[6]]']
    with open("input.txt") as file:
        for line in file.readlines():
            if len(line.strip('\n')) > 0:
                pairs.append(line.strip('\n'))
    pairs = sorted(pairs, key=cmp_to_key(compare_pairs_str), reverse=True)
    print((pairs.index('[[2]]') + 1) * (pairs.index('[[6]]') + 1))

part2()
