solved = {}
unsolved = {}


def read_part_1():
    with open("input.txt") as file:
        for line in file.readlines():
            splitted_line = line.strip('\n').split()
            monkey = splitted_line[0][:-1]
            # if monkey == 'root':
            #     unsolved[monkey] = (splitted_line[1], '=', splitted_line[3])
            # elif monkey == 'humn':
            #     unsolved[monkey] = monkey
            # else:
            if len(splitted_line) > 2:
                unsolved[monkey] = (splitted_line[1], splitted_line[2], splitted_line[3])
            else:
                solved[monkey] = int(splitted_line[1])


def read_part_2():
    with open("input.txt") as file:
        for line in file.readlines():
            splitted_line = line.strip('\n').split()
            monkey = splitted_line[0][:-1]
            if monkey == 'root':
                unsolved[monkey] = (splitted_line[1], '=', splitted_line[3])
            elif monkey == 'humn':
                unsolved[monkey] = monkey
            else:
                if len(splitted_line) > 2:
                    unsolved[monkey] = (splitted_line[1], splitted_line[2], splitted_line[3])
                else:
                    solved[monkey] = int(splitted_line[1])


def solve_part_1():
    while 'root' in unsolved:
        print(f"Solved: {len(solved)} - Unsolved: {len(unsolved)}")
        to_pop = []
        for el in unsolved.keys():
            if unsolved[el][0] in solved and unsolved[el][2] in solved:
                el1 = solved[unsolved[el][0]]
                el2 = solved[unsolved[el][2]]
                match unsolved[el][1]:
                    case '+':
                        sol = el1 + el2
                    case '-':
                        sol = el1 - el2
                    case '*':
                        sol = el1 * el2
                    case _:
                        sol = el1 // el2
                solved[el] = sol
                to_pop.append(el)
        for pop in to_pop:
            unsolved.pop(pop)


def solve_part_2():
    while unsolved['root'][0] in unsolved and unsolved['root'][2] in unsolved:
        to_pop = []
        for el in unsolved.keys():
            if unsolved[el][0] in solved and unsolved[el][2] in solved:
                el1 = solved[unsolved[el][0]]
                el2 = solved[unsolved[el][2]]
                match unsolved[el][1]:
                    case '+':
                        sol = el1 + el2
                    case '-':
                        sol = el1 - el2
                    case '*':
                        sol = el1 * el2
                    case _:
                        sol = el1 // el2
                solved[el] = sol
                to_pop.append(el)
        for pop in to_pop:
            unsolved.pop(pop)

    part_solved = unsolved['root'][0] if unsolved['root'][0] in solved else unsolved['root'][2]
    current_total = solved[part_solved]
    current_monkey = unsolved['root'][0] if unsolved['root'][0] in unsolved else unsolved['root'][2]

    while True:
        print(f"{current_monkey} - {current_total}")
        equation = unsolved[current_monkey]
        if current_monkey == 'humn':
            print(current_total)
            break
        if equation[0] in solved:
            other = equation[2]
            the_solved_one = equation[0]
        else:
            other = equation[0]
            the_solved_one = equation[2]
        match equation[1]:
            case '+':
                sol = current_total - solved[the_solved_one]
            case '-':
                sol = current_total + solved[the_solved_one]
            case '*':
                sol = current_total // solved[the_solved_one]
            case _:
                sol = current_total * solved[the_solved_one]
        current_monkey = other
        current_total = sol


read_part_2()
solve_part_2()
