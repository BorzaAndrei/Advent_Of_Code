cardinal_points = ['E', 'S', 'W', 'N']


def rotate(current_direction, rotation_direction, degrees):
    no_rotations = degrees // 90
    way = 1 if rotation_direction == 'R' else -1
    current_index = cardinal_points.index(current_direction)
    while no_rotations:
        current_index += way
        current_index = current_index % len(cardinal_points)
        no_rotations -= 1
    return cardinal_points[current_index]


def move(start_coordinates, direction, next_move):
    move_direction = next_move[0]
    number_moves = int(next_move.strip()[1:])
    if move_direction == 'F':
        move_direction = direction
    elif move_direction == 'R' or move_direction == 'L':
        return rotate(direction, move_direction, number_moves)

    if move_direction == 'N':
        start_coordinates["y"] += number_moves
    elif move_direction == 'S':
        start_coordinates["y"] -= number_moves
    elif move_direction == 'E':
        start_coordinates["x"] += number_moves
    elif move_direction == 'W':
        start_coordinates["x"] -= number_moves
    return direction


def rotate_waypoint(start_waypoint_coordinates, rotation_direction, degrees):
    no_rotations = degrees // 90
    way = 1 if rotation_direction == 'R' else -1
    while no_rotations:
        if way == -1:
            start_waypoint_coordinates["x"], start_waypoint_coordinates["y"] = -start_waypoint_coordinates["y"],\
                                                                               start_waypoint_coordinates["x"]
        else:
            start_waypoint_coordinates["x"], start_waypoint_coordinates["y"] = start_waypoint_coordinates["y"], \
                                                                               -start_waypoint_coordinates["x"]
        no_rotations -= 1


def move_with_waypoint(start_coordinates, start_waypoint_coordinates, next_move):
    move_direction = next_move[0]
    number_moves = int(next_move.strip()[1:])
    if move_direction == 'F':
        start_coordinates["x"] += start_waypoint_coordinates["x"] * number_moves
        start_coordinates["y"] += start_waypoint_coordinates["y"] * number_moves
    elif move_direction == 'R' or move_direction == 'L':
        rotate_waypoint(start_waypoint_coordinates, move_direction, number_moves)
    elif move_direction == 'N':
        start_waypoint_coordinates["y"] += number_moves
    elif move_direction == 'S':
        start_waypoint_coordinates["y"] -= number_moves
    elif move_direction == 'E':
        start_waypoint_coordinates["x"] += number_moves
    elif move_direction == 'W':
        start_waypoint_coordinates["x"] -= number_moves


s_coordinates = {"x": 0, "y": 0}
waypoint_coordinates = {"x": 10, "y": 1}
s_direction = 'E'
with open("input/12.txt") as r:
    for line in r.readlines():
        # s_direction = move(s_coordinates, s_direction, line)
        move_with_waypoint(s_coordinates, waypoint_coordinates, line)
print(abs(s_coordinates["x"]) + abs(s_coordinates["y"]))
