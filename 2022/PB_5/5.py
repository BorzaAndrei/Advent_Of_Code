stacks = {}

with open("input.txt") as file:
    last_line = False
    no_stacks = -1
    for line in file.readlines():
        line_iter = iter(line)
        finished = False
        ind = 0
        while not finished and not last_line:
            try:
                next(line_iter)  # possible bracket 1
            except StopIteration:
                # Reached EoL
                finished = True
                no_stacks = ind
                continue
            possible_letter = next(line_iter)
            next(line_iter)  # possible bracket 2
            next(line_iter)  # space
            ind += 1
            try:
                a = int(possible_letter)
                last_line = True
                # Reverse stacks
                for key in stacks.keys():
                    stacks[key].reverse()
            except ValueError:
                # Letter
                if possible_letter == ' ':
                    continue
                else:
                    if str(ind) not in stacks.keys():
                        stacks[str(ind)] = []
                    stacks[str(ind)].append(possible_letter)

        # Read moves P1
        # if last_line and 'move' in line:
        #     split_line = line.split()
        #     amount = int(split_line[1])
        #     source = split_line[3]
        #     destination = split_line[-1]
        #     for _ in range(amount):
        #         element = stacks[source].pop()
        #         stacks[destination].append(element)
        # Read Moves P2
        if last_line and 'move' in line:
            split_line = line.split()
            amount = int(split_line[1])
            source = split_line[3]
            destination = split_line[-1]
            stack = []
            for _ in range(amount):
                element = stacks[source].pop()
                stack.append(element)
            for _ in range(amount):
                stacks[destination].append(stack.pop())

print(stacks)
for ind in range(1, no_stacks + 1):
    print(stacks[str(ind)][-1], end='')
