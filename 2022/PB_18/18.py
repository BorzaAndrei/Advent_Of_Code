from dataclasses import dataclass


@dataclass
class Cube:
    x: int
    y: int
    z: int

    def construct_sides(self):
        return [
            [(self.x, self.y, self.z), (self.x + 1, self.y, self.z), (self.x, self.y + 1, self.z),
             (self.x + 1, self.y + 1, self.z)],
            [(self.x, self.y, self.z), (self.x + 1, self.y, self.z), (self.x, self.y, self.z + 1),
             (self.x + 1, self.y, self.z + 1)],
            [(self.x, self.y, self.z), (self.x, self.y + 1, self.z), (self.x, self.y, self.z + 1),
             (self.x, self.y + 1, self.z + 1)],
            [(self.x, self.y, self.z + 1), (self.x + 1, self.y, self.z + 1), (self.x, self.y + 1, self.z + 1),
             (self.x + 1, self.y + 1, self.z + 1)],
            [(self.x + 1, self.y, self.z), (self.x + 1, self.y, self.z + 1), (self.x + 1, self.y + 1, self.z),
             (self.x + 1, self.y + 1, self.z + 1)],
            [(self.x + 1, self.y + 1, self.z), (self.x, self.y + 1, self.z), (self.x, self.y + 1, self.z + 1),
             (self.x + 1, self.y + 1, self.z + 1)],
        ]


common_sides = set()
cubes = []
c = 0
with open("input.txt") as file:
    for line in file.readlines():
        cube_x, cube_y, cube_z = [int(t) for t in line.strip('\n').split(',')]
        cubes.append((cube_x, cube_y, cube_z))
        sides = [
            [(cube_x, cube_y, cube_z), (cube_x + 1, cube_y, cube_z), (cube_x, cube_y + 1, cube_z),
             (cube_x + 1, cube_y + 1, cube_z)],
            [(cube_x, cube_y, cube_z), (cube_x + 1, cube_y, cube_z), (cube_x, cube_y, cube_z + 1),
             (cube_x + 1, cube_y, cube_z + 1)],
            [(cube_x, cube_y, cube_z), (cube_x, cube_y + 1, cube_z), (cube_x, cube_y, cube_z + 1),
             (cube_x, cube_y + 1, cube_z + 1)],
            [(cube_x, cube_y, cube_z + 1), (cube_x + 1, cube_y, cube_z + 1), (cube_x, cube_y + 1, cube_z + 1),
             (cube_x + 1, cube_y + 1, cube_z + 1)],
            [(cube_x + 1, cube_y, cube_z), (cube_x + 1, cube_y, cube_z + 1), (cube_x + 1, cube_y + 1, cube_z),
             (cube_x + 1, cube_y + 1, cube_z + 1)],
            [(cube_x + 1, cube_y + 1, cube_z), (cube_x, cube_y + 1, cube_z), (cube_x, cube_y + 1, cube_z + 1),
             (cube_x + 1, cube_y + 1, cube_z + 1)],
        ]
        for side in sides:
            sorted_side = sorted(side, key=lambda tup: (tup[0], tup[1], tup[2]))
            if tuple(sorted_side) in common_sides:
                c -= 1
            else:
                c += 1
                common_sides.add(tuple(sorted_side))


def fill(x, y, z, cubes, MAXIM=8):
    q = [(x, y, z)]
    visited = []
    while len(q) > 0:
        curr_x, curr_y, curr_z = q.pop(0)
        for add_x in range(-1, 2):
            if -1 <= curr_x + add_x <= MAXIM:
                for add_y in range(-1, 2):
                    if -1 <= curr_y + add_y <= MAXIM:
                        for add_z in range(-1, 2):
                            if (add_x, add_y, add_z) in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                                if -1 <= curr_z + add_z <= MAXIM and (
                                        curr_x + add_x, curr_y + add_y, curr_z + add_z) not in cubes and (
                                        curr_x + add_x, curr_y + add_y, curr_z + add_z) not in visited:
                                    q.append((curr_x + add_x, curr_y + add_y, curr_z + add_z))
                                    visited.append((curr_x + add_x, curr_y + add_y, curr_z + add_z))
    return visited


MAXIM = 30
exterior_air = fill(-1, -1, -1, cubes, MAXIM)
for x in range(-1, MAXIM):
    for y in range(-1, MAXIM):
        for z in range(-1, MAXIM):
            if (x, y, z) not in cubes and (x, y, z) not in exterior_air:
                cube = Cube(x, y, z)
                cube_sides = cube.construct_sides()
                for side in cube_sides:
                    if tuple(sorted(side, key=lambda tup: (tup[0], tup[1], tup[2]))) in common_sides:
                        c -= 1

print(c)
