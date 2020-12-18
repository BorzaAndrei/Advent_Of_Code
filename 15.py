puzzle_input = [16, 12, 1, 0, 15, 7, 11]

last_saw = {}
for ind in range(len(puzzle_input)):
    last_saw[puzzle_input[ind]] = ind

last_number = 0
ind = len(puzzle_input)
while ind < 29999999:
    if last_number in last_saw:
        aux = last_number
        last_number = ind - last_saw[last_number]
        last_saw[aux] = ind
    else:
        last_saw[last_number] = ind
        last_number = 0
    ind += 1

print(last_number)
