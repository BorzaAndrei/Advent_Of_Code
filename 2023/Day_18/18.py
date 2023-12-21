# # 1st implementation
# import sys
# sys.setrecursionlimit(50000)

# from collections import Counter


# def flood_fill(matrix, start_point, new_color):
#     """
#     Perform flood fill on a matrix starting from a given point.

#     Parameters:
#     - matrix: 2D matrix to be filled
#     - start_point: Tuple (row, column) representing the starting point
#     - new_color: New color to fill the area with

#     Note: Assumes that the matrix is represented as a list of lists.
#     """
#     rows, cols = len(matrix), len(matrix[0])
#     original_color = matrix[start_point[0]][start_point[1]]
    
#     # Check if the start point is already of the new color
#     if original_color == new_color:
#         return

#     def valid_point(row, col):
#         return 0 <= row < rows and 0 <= col < cols

#     def fill(row, col):
#         if not valid_point(row, col) or matrix[row][col] != original_color:
#             return
#         matrix[row][col] = new_color
#         fill(row - 1, col)
#         fill(row + 1, col)
#         fill(row, col - 1)
#         fill(row, col + 1)

#     fill(start_point[0], start_point[1])



# current_x, current_y = 0, 0
# points = set((current_x, current_y))
# max_x, max_y = -1, -1
# with open("2023/Day_18/input.txt") as r:
    
#     for l in r.readlines():
#         direction, depth, color = l.strip('\n').split()
#         for _ in range(int(depth)):
#             match direction:
#                 case 'R':
#                     current_y += 1
#                 case 'L':
#                     current_y -= 1
#                 case 'U':
#                     current_x -= 1
#                 case 'D':
#                     current_x += 1
#             if current_x > max_x:
#                 max_x = current_x
#             if current_y > max_y:
#                 max_y = current_y
#             points.add((current_x, current_y))

# with open("2023/Day_18/output.txt", 'w') as w:
#     matrix = []
#     for l in range(-30, max_x + 2):
#         line = []
#         for c in range(-30, max_y + 2):
#             if (l, c) in points:
#                 line.append('#')
#                 w.write('#')
#             else:
#                 line.append('.')
#                 w.write('.')
#         matrix.append(line)
#         w.write('\n')

# print()
# flood_fill(matrix, (329, 42), '#')

# # for l in matrix:
# #     print("".join(l))


# print(Counter([item for l in matrix for item in l])['#'])

# 2nd implementation
from collections import Counter
import math
from shapely.geometry import Polygon, Point

current_x, current_y = 0, 0
vertices = [(current_x, current_y)]
perimeter = 0
pob = 0
with open("2023/Day_18/input.txt") as r:
    for line in r.readlines():
        # hexx = line.strip('\n').split(' ')[2].strip('()')[1:]
        # depth, direction = int(hexx[:5], 16), int(hexx[-1])
        direction, depth, _ = line.strip('\n').split()
        depth = int(depth)
        # match direction:
        #     case 0:
        #         current_y += depth
        #     case 1:
        #         current_x += depth
        #     case 2:
        #         current_y -= depth
        #     case 3:
        #         current_x -= depth
        perimeter += depth - 1
        match direction:
            case 'R':
                current_y += depth
            case 'D':
                current_x += depth
            case 'L':
                current_y -= depth
            case 'U':
                current_x -= depth
        # if current_x != 0 or current_y != 0:
        if current_x == 0:
            pob += current_y + 1
        elif current_y == 0:
            pob += current_x + 1
        else:
            pob += math.gcd(current_x, current_y) + 1
        vertices.append((current_x, current_y))

# B: 38
# I: 24
polygon = Polygon(vertices)
print(f"Possible B: {pob} | Actual B: 38")
print(f"Possible I: {polygon.area - pob // 2 - 1} | Actual I: 24")
print(f"Possible result: {pob + polygon.area - pob // 2 - 1} | Actual result: 62")

# From reddit
import math

S='data'
f=open("2023/Day_18/input.txt",'r')
R=f.read()
L=R.split("\n")
Block=R.split("\n\n")
f.close()

steps=[]
#direcmap={"R":(0,1), "D":(1,0), "L":(0,-1), "U":(-1,0)}
direcmap={"0":(0,1), "1":(1,0), "2":(0,-1), "3":(-1,0)}

for line in L[:-1]:
    direc, length, col = line.split(" ")
    direc = line.split(" ")[-1][-2]     #comment out for part 1
    length = line.split(" ")[-1][-7:-2] #comment out for part 1
    length = int(length, 16)            #just do int(length) for part 1
    steps.append((direc,length))

x=0
y=0
perimeter=0
area=0
for step in steps:
    direc, length = step
    dy, dx = direcmap[direc]
    dy, dx = dy*length, dx*length
    y, x = y+dy, x+dx
    perimeter+=length
    area+=x*dy
print('Inner area:',area)
print('Perimeter: ',perimeter)
print("Total area:",area+perimeter//2+1)
