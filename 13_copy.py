# import math
# import time
#
# with open("input/13.txt") as r:
#     depart_time = int(r.readline().strip())
#     bus_schedule = r.readline().strip().split(',')
#
#
# # minimum = math.inf
# # minimum_bus_id = None
# # for bus in bus_schedule:
# #     try:
# #         bus_id = int(bus)
# #         closest_multiple = depart_time // bus_id + 1
# #         difference = closest_multiple * bus_id - depart_time
# #         if difference < minimum:
# #             minimum = difference
# #             minimum_bus_id = bus_id
# #     except ValueError:
# #         pass
# #
# # print(minimum * minimum_bus_id)
#
# # Construct list
# new_bus_schedule = []
# free_space = 0
# last_bus_id = int(bus_schedule[0])
# max_id = -1
# max_ind = -1
# for bus in bus_schedule[1:]:
#     if bus == 'x' and free_space > 0:
#         free_space += 1
#     elif bus == 'x' and free_space == 0:
#         free_space = 1
#     else:
#         new_bus_schedule.append((last_bus_id, free_space + 1))
#         if last_bus_id > max_id:
#             max_id = last_bus_id
#             max_ind = len(new_bus_schedule) - 1
#         free_space = 0
#         last_bus_id = int(bus)
# new_bus_schedule.append((int(bus_schedule[-1]), 1))
#
# print(new_bus_schedule)
# print(max_id)
# print(max_ind)
#
# start_time = time.time()
#
# found = False
# current_multiple = (100000000000000 // max_id + 1) * max_id
# while not found:
#     if time.time() - start_time > 300:
#         print(current_multiple)
#     found = True
#     aux_multiple = current_multiple
#     for small_id in range(max_ind - 1, -1, -1):
#         if (aux_multiple - new_bus_schedule[small_id][1]) % new_bus_schedule[small_id][0] != 0:
#             found = False
#             break
#         else:
#             aux_multiple -= new_bus_schedule[small_id][1]
#     if found:
#         aux_multiple = current_multiple
#         for big_id in range(max_ind + 1, len(new_bus_schedule)):
#             if (aux_multiple + new_bus_schedule[big_id - 1][1]) % new_bus_schedule[big_id][0] != 0:
#                 found = False
#                 break
#             else:
#                 aux_multiple += new_bus_schedule[big_id - 1][1]
#     if not found:
#         current_multiple += max_id
#
# end_time = start_time - time.time()
# print(end_time)
# print(current_multiple)
# for small_id in range(max_ind - 1, -1, -1):
#     current_multiple -= new_bus_schedule[small_id][1]
# print(current_multiple)
x = 0
T, D = map(eval, open("input/13.txt"))
n = p = 1
s = T,
for b in D:
    if b:
        while (n + x) % b: n += p
        p *= b
        w, v = s = min(s, (-T % b, b))
    x += 1
print(w * v, n)
