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


def fill(x, y , z, cubes):
    q = [(x, y, z)]
    visited = []
    while len(q) > 0:
        curr_x, curr_y, curr_z = q.pop(0)
        for add_x in range(-1, 2):
            for add_y in range(-1, 2):
                for add_z in range(-1, 2):
                    if (curr_x + add_x, curr_y + add_y, curr_z) not in cubes and (curr_x + add_x, curr_y + add_y, curr_z) not in visited:
                        q.append((curr_x + add_x, curr_y + add_y, curr_z))
                        visited.append((curr_x + add_x, curr_y + add_y, curr_z))

for x in range(30):
    for y in range(30):
        for z in range(30):
            if (x, y, z) not in cubes:
                cube = Cube(x, y, z)
                cube_sides = cube.construct_sides()
                all_in_common = True
                for side in cube_sides:
                    if tuple(sorted(side, key=lambda tup: (tup[0], tup[1], tup[2]))) not in common_sides:
                        all_in_common = False
                        break
                if all_in_common:
                    c -= 6
                    print((x, y, z))
print(c)
