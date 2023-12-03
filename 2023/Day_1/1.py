import re
import functools

first_regex = "\d"
second_regex = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"


match_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

compare = []

with open("input.txt") as r:
    print(functools.reduce(lambda x, y: x + y, (map(lambda lst: int(f"{lst[0] if len(lst[0]) == 1 else match_dict[lst[0]]}{lst[-1] if len(lst[-1]) == 1 else match_dict[lst[-1]]}"),[[match.group(1) for match in re.finditer(second_regex, line.strip('\n'))] for line in r.readlines()]))))
