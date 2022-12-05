dependency_dict = {}
can_reach_solution = set()


def add_recursively(top):
    for c_color, _ in dependency_dict[top]:
        if c_color == "shiny gold":
            can_reach_solution.add(top)
            return True
        elif c_color in can_reach_solution:
            return True
        else:
            if add_recursively(c_color):
                can_reach_solution.add(c_color)
                can_reach_solution.add(top)
                return True
    return False


def count_recursively(top):
    partial_sum = 0
    for c_color, q in dependency_dict[top]:
        partial_sum += q + q * count_recursively(c_color)
    return partial_sum


with open("input/7.txt") as r:
    for line in r.readlines():
        info = line.split("contain")
        parent = " ".join(info[0].split()[0:2])
        dependency_dict[parent] = []
        if "no other bags" in info[1]:
            pass
        else:
            children = info[1].split(',')
            for child in children:
                correct_child = child.strip().strip('\n').strip('bag').strip('bags').strip('bags.').strip('bag.').strip()
                split_correct_child = correct_child.split()
                quantity = int(split_correct_child[0])
                name = " ".join(split_correct_child[1:])
                if name == "shiny gold":
                    can_reach_solution.add(parent)
                dependency_dict[parent].append((name, quantity))

for color in dependency_dict:
    if color not in can_reach_solution:
        for child_color, _ in dependency_dict[color]:
            if child_color == "shiny gold":
                can_reach_solution.add(color)
                break
            elif add_recursively(child_color):
                can_reach_solution.add(color)
                break

# print(can_reach_solution)
print(len(can_reach_solution))

print(count_recursively("shiny gold"))
