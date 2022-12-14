m = set()

with open("input.txt") as file:
    for line in file.readlines():
        rocks = line.strip('\n').split(' -> ')
        # noinspection PyRedeclaration
        rock_y, rock_x = (int(x) for x in rocks[0].split(','))
        for rock in rocks[1:]:
            m.add((rock_x, rock_y))
            dest_rock_y, dest_rock_x = (int(x) for x in rock.split(','))
            for row_ind in range(rock_x, dest_rock_x):
                m.add((row_ind, rock_y))
            for row_ind in range(dest_rock_x, rock_x):
                m.add((row_ind, rock_y))
            for col_ind in range(rock_y, dest_rock_y):
                m.add((rock_x, col_ind))
            for col_ind in range(dest_rock_y, rock_y):
                m.add((rock_x, col_ind))
            m.add((dest_rock_x, dest_rock_y))
            rock_x, rock_y = dest_rock_x, dest_rock_y

still_generating_grains = True
start_x, start_y = 0, 500
c = 0
MAX_DEPTH = max(x for (x, _) in m) + 2
for col in range(1000):
    m.add((MAX_DEPTH, col))
while still_generating_grains:
    current_x, current_y = start_x, start_y
    still_falling = True
    while still_falling:
        # if current_x > MAX_DEPTH:
        #     still_generating_grains = False
        #     still_falling = False
        if (current_x + 1, current_y) not in m:
            current_x += 1
        elif (current_x + 1, current_y - 1) not in m:
            current_x += 1
            current_y -= 1
        elif (current_x + 1, current_y + 1) not in m:
            current_x += 1
            current_y += 1
        else:
            m.add((current_x, current_y))
            c += 1
            still_falling = False
            if (current_x, current_y) == (0, 500):
                still_generating_grains = False

print(c)
