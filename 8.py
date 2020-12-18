instructions = []
flippable = []

with open("input/8.txt") as r:
    ind = 0
    for line in r.readlines():
        if "jmp" in line:
            flippable.append(ind)
        instructions.append(line.strip('\n'))
        ind += 1

found = False
for flippy in flippable:
    current_index = 0
    completed_instruction_indexes = set()
    put_before = False
    accumulator = 0

    while not put_before:
        if current_index >= len(instructions):
            found = True
            break

        instruction = instructions[current_index].split()

        before_len = len(completed_instruction_indexes)
        completed_instruction_indexes.add(current_index)
        if len(completed_instruction_indexes) == before_len:
            put_before = True
            continue

        command = instruction[0]
        sign = instruction[1][0]
        number = int(instruction[1][1:])
        if current_index == flippy:
            if command == "jmp":
                command = "nop"
        if command == "acc":
            if sign == "+":
                accumulator += number
            else:
                accumulator -= number
            current_index += 1
        elif command == "jmp":
            if sign == "+":
                current_index += number
            else:
                current_index -= number
        elif command == "nop":
            current_index += 1
    if found:
        print(accumulator)
        break
