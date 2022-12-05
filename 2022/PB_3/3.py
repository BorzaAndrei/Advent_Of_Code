from string import ascii_lowercase, ascii_uppercase

points = {letter: ind + 1 for ind, letter in enumerate(ascii_lowercase)}
for ind, letter in enumerate(ascii_uppercase):
    points[letter] = ind + 27

with open("input.txt") as file:
    s = 0
    for line in file.readlines():
        stripped_line = line.strip('\n')
        common = set(stripped_line[:len(stripped_line) // 2]).intersection(stripped_line[len(stripped_line) // 2:])
        for c in common:
            s += points[c]
    print(s)

with open("input.txt") as file:
    file_iter = iter(file)
    s = 0
    for rucksack in file_iter:
        rucksack_1 = rucksack.strip('\n')
        rucksack_2 = next(file_iter).strip('\n')
        rucksack_3 = next(file_iter).strip('\n')
        common = set(rucksack_1).intersection(set(rucksack_2)).intersection(set(rucksack_3))
        for c in common:
            s += points[c]
    print(s)
