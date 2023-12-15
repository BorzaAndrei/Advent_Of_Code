from itertools import combinations

galaxies = []

def dist(galaxy1, galaxy2):
    distance = abs(galaxy2[0] - galaxy1[0]) + abs(galaxy2[1] - galaxy1[1])
    return distance

with open("2023/Day_11/input.txt") as r:
    lines = r.readlines()
    max_x, max_y = len(lines), len(lines[0].strip('\n'))
    for line_ind, line in enumerate(lines):
        for ind, ch in enumerate(line.strip('\n')):
            if ch == '#':
                galaxies.append((line_ind, ind))
    
    empty_rows = [x for x in range(max_x)]
    empty_cols = [y for y in range(max_y)]
    for galaxy in galaxies:
        if galaxy[0] in empty_rows:
            empty_rows.remove(galaxy[0])
        if galaxy[1] in empty_cols:
            empty_cols.remove(galaxy[1])

    updated_galaxies = []
    for galaxy in galaxies:
        new_x = galaxy[0]
        new_y = galaxy[1]
        for er in empty_rows:
            if galaxy[0] > er:
                new_x += 999999
        for ec in empty_cols:
            if galaxy[1] > ec:
                new_y += 999999
        updated_galaxies.append((new_x, new_y))
    
    print(sum([dist(pair[0], pair[1]) for pair in list(combinations(updated_galaxies, 2))]))
