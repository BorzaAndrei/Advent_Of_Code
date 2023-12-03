# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
import math


with open("input.txt") as r:
    sum_idx = 0
    idx = 0
    max_color = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for line in r.readlines():
        game, rest = line.strip('\n').split(': ')
        # print(f"GAME: {game} | REST: {rest}")
        sets = rest.split('; ')
        # print(f"SETS: {sets}")
        stop = False
        min_color = {}
        for s in sets:
            # print(f"SET: {s}")
            pairs = s.split(', ')
            for no_color in pairs:
                # print(f"NO_COLOR: {no_color}")
                no_color = no_color.split(' ')
                number, color = no_color[0], no_color[1]
                if color not in min_color.keys():
                    min_color[color] = -math.inf
                if int(number) > min_color[color]:
                    min_color[color] = int(number)
        sum_idx += math.prod(min_color.values())
        #         if color in max_color.keys() and int(number) > max_color[color]:
        #             stop = True
        #             break
        #     if stop:
        #         break
        # if not stop:
        #     sum_idx += int(game.split(' ')[-1])
    print(sum_idx)
