
def pair_in_pair(pair1, pair2):
    a, b = list(map(int, pair1.split('-')))
    x, y = list(map(int, pair2.split('-')))
    if a <= x <= b and a <= y <= b:
        return True
    elif x <= a <= y and x <= b <= y:
        return True
    return False


def count_overlap_pairs(pair1, pair2):
    a, b = list(map(int, pair1.split('-')))
    x, y = list(map(int, pair2.split('-')))
    if a <= x <= b or a <= y <= b:
        return True
    elif x <= a <= y or x <= b <= y:
        return True
    return False


with open("input.txt") as file:
    c = 0
    c2 = 0
    for line in file:
        pairs = line.strip('\n').split(',')
        if pair_in_pair(pairs[0], pairs[1]):
            c += 1
        if count_overlap_pairs(pairs[0], pairs[1]):
            c2 += 1

    print(f"{c} - {c2}")
