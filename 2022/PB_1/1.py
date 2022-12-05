# 1000
# 2000
# 3000
#
# 4000
#
# 5000
# 6000
#
# 7000
# 8000
# 9000
#
# 10000

# /\ Input: Calories held by each elf

# Part 1
# max_sum = 0
# with open("input.txt") as r_file:
#     current_sum = 0
#     for line in r_file.readlines():
#         stripped_line = line.strip('\n')
#         if len(stripped_line) > 0:
#             current_sum += int(stripped_line)
#         else:
#             max_sum = max(max_sum, current_sum)
#             current_sum = 0
# print(max_sum)

all_sums = []
with open("input.txt") as r_file:
    current_sum = 0
    for line in r_file.readlines():
        stripped_line = line.strip('\n')
        if len(stripped_line) > 0:
            current_sum += int(stripped_line)
        else:
            all_sums.append(current_sum)
            current_sum = 0
print(sum(sorted(all_sums, reverse=True)[:3]))
