from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Number:
    index: int
    value: int


original_list = []
ind = 0
with open("input.txt") as file:
    for line in file.readlines():
        number = Number(index=ind, value=int(line.strip('\n')))
        number.value *= 811589153
        original_list.append(number)
        ind += 1


cpy_list = original_list[:]
for r in range(10):
    for current_number in original_list:
        current_index = [ind for ind in range(len(cpy_list)) if cpy_list[ind].index == current_number.index][0]
        cpy_list.pop(current_index)
        if current_number.value == -current_index:
            cpy_list.append(current_number)
        else:
            cpy_list.insert((current_index + current_number.value) % (len(original_list) - 1), current_number)

number_0_ind = [ind for ind in range(len(cpy_list)) if cpy_list[ind].value == 0][0]
n_1000 = cpy_list[(number_0_ind + 1000) % len(original_list)].value
n_2000 = cpy_list[(number_0_ind + 2000) % len(original_list)].value
n_3000 = cpy_list[(number_0_ind + 3000) % len(original_list)].value
print(f"{n_1000} + {n_2000} + {n_3000} = {n_1000 + n_2000 + n_3000}")
