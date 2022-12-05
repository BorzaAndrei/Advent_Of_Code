numbers = []

with(open("input/1.txt")) as r:
    for number in r.readlines():
        numbers.append(int(number))

numbers = sorted(numbers)
# for ind in range(len(numbers)):
#     current_no = numbers[ind]
#     for ind_o in range(len(numbers) - 1, ind, -1):
#         if current_no + numbers[ind_o] == 2020:
#             print(current_no * numbers[ind_o])
#         if current_no + numbers[ind_o] < 2020:
#             break

for ind in range(len(numbers)):
    for ind_o in range(ind + 1, len(numbers)):
        other_no = 2020 - numbers[ind_o] - numbers[ind]
        if other_no in numbers:
            print(numbers[ind] * numbers[ind_o] * other_no)
            break
