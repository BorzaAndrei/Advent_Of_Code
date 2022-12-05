jolts = None
effective_rating = 0
jolt_1_differences = 0
jolt_3_differences = 0
with open("input/10.txt") as r:
    jolts = [int(jolt.strip()) for jolt in r.readlines()]

jolts.append(max(jolts) + 3)
jolts.insert(0, 0)

jolts = sorted(jolts)

for jolt in jolts:
    if jolt - effective_rating == 1:
        jolt_1_differences += 1
    elif jolt - effective_rating == 3:
        jolt_3_differences += 1
    effective_rating = jolt

    diff_current_jolt = 0
    for jolt_diff in range(1, 4):
        if jolt + jolt_diff in jolts:
            diff_current_jolt += 1

power = {}
for jolt in jolts:
    power[jolt] = 0

power[jolts[-1]] = 1

for c_jolt in jolts[-2::-1]:
    for next_jolt in range(c_jolt + 1, c_jolt + 4):
        if power.get(next_jolt):
            power[c_jolt] += power.get(next_jolt)

print(power[0])
