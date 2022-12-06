with open("input.txt") as file:
    for line in file.readlines():
        # P1 0 and 4
        start, end = 0, 14
        while len(set(line[start:end])) != 14:
            start += 1
            end += 1
        print(end)
