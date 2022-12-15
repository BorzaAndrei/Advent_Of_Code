import re

from dataclasses import dataclass


@dataclass
class Beacon:
    x: int
    y: int


@dataclass
class Sensor:
    x: int
    y: int
    closest_beacon: Beacon
    md = 0

    def calculate_md(self):
        self.md = abs(self.closest_beacon.x - self.x) + abs(self.closest_beacon.y - self.y)

    def is_point_in_area(self, x, y):
        return abs(self.x - x) + abs(self.y - y) <= self.md

    def __str__(self):
        return f"x={self.x}, y={self.y}, md={self.md}, beacon: x={self.closest_beacon.x}, y={self.closest_beacon.y}"


sensors = []
beacons = []
with open("input.txt") as file:
    regex_x = "x=(-*[0-9]+)"
    regex_y = "y=(-*[0-9]+)"
    for line in file.readlines():
        beacon = Beacon(int(re.findall(regex_x, line)[1]), int(re.findall(regex_y, line)[1]))
        beacons.append(beacon)
        sensor = Sensor(int(re.findall(regex_x, line)[0]), int(re.findall(regex_y, line)[0]), beacon)
        sensor.calculate_md()
        sensors.append(sensor)

max_md = (max(s.md for s in sensors))
min_x = min(s.x for s in sensors)
min_x = min(min_x, min(b.x for b in beacons)) - 1 - max_md
max_x = max(s.x for s in sensors)
max_x = max(max_x, max(b.x for b in beacons)) + 1 + max_md


# Part 1
# y = 2000000
# found_points = set()
# print(f"min: {min_x} - max: {max_x}")
# for x in range(min_x, max_x + 1):
#     for s in sensors:
#         if s.is_point_in_area(x, y):
#             found_points.add((x, y))
#             break
# for b in beacons:
#     if (b.x, b.y) in found_points:
#         found_points.remove((b.x, b.y))
# 
# print(f"c={len(found_points)}")

# Part 2

def check(x, y, limit):
    if y >= limit:
        return x + 1, 0
    return x, y


MAX = 4000000

x_found = 0
y_found = 0
c = 0
found = False
while not found:
    in_area = False
    for s in sensors:
        if s.is_point_in_area(x_found, y_found):
            in_area = True
            y_found = s.y + s.md - abs(x_found - s.x) + 1
            x_found, y_found = check(x_found, y_found, MAX)
            c += 1
            break
    if not in_area:
        found = True
    if c % 100000 == 0:
        print(f"{x_found} - {y_found}")
print(f"VICTORY: {x_found} - {y_found} - {x_found * MAX + y_found}")
