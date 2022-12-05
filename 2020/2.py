with(open("input/2.txt")) as r:

    count = 0

    for line in r.readlines():
        line = line.split(':')
        policy = line[0].strip().split()
        password = line[1].strip()

        bounds = policy[0].split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        letter = policy[1]

        # print(str(bounds) + " | " + letter + " | " + str(password.count(letter)) + " | " + password)
        # if lower_bound <= password.count(letter) <= upper_bound:
        #     print("Correct!")
        #     count += 1

        pos_1 = letter == password[lower_bound - 1]
        pos_2 = letter == password[upper_bound - 1]

        print(str(bounds) + " | " + letter + " | " + str([pos_1, pos_2]) + " | " + str(pos_1 ^ pos_2) + " | " + password)
        count += int(pos_1 ^ pos_2)

    print(count)
