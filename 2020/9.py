def is_valid(no, preamble):
    for a_number in preamble:
        if no - a_number in preamble:
            return True
    return False


current_numbers = []
preamble_no = 25
invalid_number = None
all_numbers = []
with open("input/9.txt") as r:
    for line in r.readlines():
        number = int(line.strip('\n'))
        all_numbers.append(number)
        if preamble_no > 0:
            current_numbers.append(number)
            preamble_no -= 1
        else:
            if not is_valid(number, current_numbers):
                print(number)
                invalid_number = number
                break
            else:
                current_numbers.pop(0)
                current_numbers.append(number)

current_set = []
current_sum = 0
for number in all_numbers:
    if current_sum + number < invalid_number:
        current_sum += number
        current_set.append(number)
    else:
        while current_sum + number > invalid_number:
            current_sum -= current_set.pop(0)
        current_sum += number
        current_set.append(number)
    if current_sum == invalid_number:
        print(min(current_set) + max(current_set))
        break
