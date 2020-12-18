from functools import reduce  # Required in Python 3
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


# noinspection PyShadowingNames
def invalid_no_on_ticket(rules, ticket):
    invalid_nos = []
    for no in ticket:
        invalid = True
        for rule in rules:
            for lower_bound, higher_bound in rules[rule]:
                if lower_bound <= no <= higher_bound:
                    invalid = False
            if not invalid:
                break
        if invalid:
            invalid_nos.append(no)
    # return sum(invalid_nos)
    return len(invalid_nos) > 0


# noinspection PyShadowingNames
def matches_field(rules, rule, no):
    for lower_bound, higher_bound in rules[rule]:
        if lower_bound <= no <= higher_bound:
            return True
    return False


rules = {}
my_ticket = None
other_tickets = []

reading_my_ticket = False
reading_other_tickets = False
with open("input/16.txt") as r:
    for line in r.readlines():
        if "your ticket" in line:
            reading_my_ticket = True
        elif "nearby tickets" in line:
            reading_other_tickets = True

        elif reading_my_ticket:
            my_ticket = [int(no) for no in line.strip().split(',')]
            reading_my_ticket = False
        elif reading_other_tickets:
            other_tickets.append([int(no) for no in line.strip().split(',')])
        elif line != '\n':
            info = line.strip().split(':')
            rule_name = info[0].strip()
            ranges = info[1].split('or')
            rules[rule_name] = [(int(rang.strip().split('-')[0]), int(rang.strip().split('-')[1])) for rang in ranges]

# print(sum(invalid_no_on_ticket(rules, no) for no in other_tickets))
correct_tickets = [ticket for ticket in other_tickets if not invalid_no_on_ticket(rules, ticket)]

rule_position = {}
for rule in rules:
    for ind in range(len(my_ticket)):
        found_ind = True
        for ticket in correct_tickets:
            if not matches_field(rules, rule, ticket[ind]):
                found_ind = False
                break
        if found_ind:
            if rule not in rule_position:
                rule_position[rule] = []
            rule_position[rule].append(ind)

done = False
done_matches = []
while not done:
    perfect_match = [rule_position[rule][0] for rule in rule_position
                     if len(rule_position[rule]) == 1 and rule_position[rule][0] not in done_matches]
    if len(done_matches) == len(rule_position):
        done = True
        break
    for rule in rule_position:
        if len(rule_position[rule]) == 1:
            continue
        for match in perfect_match:
            if match in rule_position[rule]:
                rule_position[rule].remove(match)
    done_matches.extend(perfect_match)
for rule in rule_position:
    print(f"{rule}: {rule_position[rule]}")
print(prod(my_ticket[rule_position[rule][0]] for rule in rule_position if "departure" in rule))
