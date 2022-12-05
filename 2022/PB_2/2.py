# A Y
# B X
# C Z

# play_dict = {
#     "A": "R",
#     "B": "P",
#     "C": "S",
#     "X": "R",
#     "Y": "P",
#     "Z": "S"
# }

beats_dict = {
    "R": "S",
    "P": "R",
    "S": "P"
}

points = {
    "R": 1,
    "P": 2,
    "S": 3
}

score = 0
# Part 1
# with open("input.txt") as file:
#     for line in file.readlines():
#         opponent_play, my_play = line.split()
#
#         opponent_play_t = play_dict[opponent_play]
#         my_play_t = play_dict[my_play]
#
#         # Draw
#         if my_play_t == opponent_play_t:
#             score += 3
#         # Win
#         elif beats_dict[my_play_t] == opponent_play_t:
#             score += 6
#         # Lose
#         else:
#             score += 0
#         score += points[my_play_t]

play_dict = {
    "A": "R",
    "B": "P",
    "C": "S",
}


def determine_my_play(opp_play, expected_outcome):
    # Draw
    if expected_outcome == 'Y':
        return opp_play
    # Win
    elif expected_outcome == 'Z':
        return [key for key in beats_dict.keys() if beats_dict[key] == opp_play][0]
    # Lose
    else:
        return beats_dict[opp_play]

# Part 2
with open("input.txt") as file:
    for line in file.readlines():
        opponent_play, outcome = line.split()

        opponent_play_t = play_dict[opponent_play]
        my_play_t = determine_my_play(opponent_play_t, outcome)

        # Draw
        if my_play_t == opponent_play_t:
            score += 3
        # Win
        elif beats_dict[my_play_t] == opponent_play_t:
            score += 6
        # Lose
        else:
            score += 0
        score += points[my_play_t]

print(score)
