from functools import cache, reduce

@cache
def hash_alg(text):
    return reduce(lambda acc, ch: (acc + ord(ch)) * 17 % 256, text, 0)

boxes = {ind: [] for ind in range(256)}
focal = {}
with open("2023/Day_15/input.txt") as r:
    init_seq = r.readline().strip('\n').split(',')
    print(sum(map(hash_alg, init_seq)))

    for instruction in init_seq:
        if '=' in instruction:
            focal_length = int(instruction[-1])
            box = int(hash_alg(instruction[:-2]))
            if instruction[:-2] in boxes[box]:
                focal[instruction[:-2]] = focal_length
            else:
                boxes[box].append(instruction[:-2])
                focal[instruction[:-2]] = focal_length
        else:
            box = int(hash_alg(instruction[:-1]))
            if instruction[:-1] in boxes[box]:
                boxes[box].remove(instruction[:-1])
                del focal[instruction[:-1]]

    print(sum([(1 + hash_alg(label)) * (1 + boxes[hash_alg(label)].index(label)) * focal[label] for label in focal.keys()]))
