from copy import deepcopy


def change_state(matrix, cube):
    x, y, z, w = cube
    count = 0
    active = matrix[z][x][y] == '#'
    for index_w in range(-1, 2):
        for index_z in range(-1, 2):
            for index_x in range(-1, 2):
                for index_y in range(-1, 2):
                    if index_x == index_y == index_z == 0:
                        continue
                    if matrix[w + index_w][z + index_z][x + index_x][y + index_y] == '#':
                        count += 1
    if (active and count == 2 or count == 3) or (not active and count == 3):
        return '#'
    else:
        return '.'


MATRIX_BOUND = 100


matrix3d = []
for ind_w in range(MATRIX_BOUND):
    dim = []
    for ind in range(MATRIX_BOUND):
        slc = []
        for index_l_y in range(MATRIX_BOUND):
            slc.append(['.'] * MATRIX_BOUND)
        dim.append(slc)
    matrix3d.append(dim)


with open("input/17.txt") as r:
    matrix_slice = []
    for line in r.readlines():
        matrix_slice.append([ch for ch in line.strip()])

# matrix3d access: z, x, y
slice_row_ind = 0
MATR = MATRIX_BOUND // 2
for ind in range(len(matrix3d[MATR]) // 2 - len(matrix_slice) // 2, len(matrix3d[MATR]) // 2 + len(matrix_slice) // 2 + 1):
    slice_col_ind = 0
    for index_l_y in range(len(matrix3d[MATR][ind]) // 2 - len(matrix_slice[0]) // 2, len(matrix3d[MATR][ind]) // 2 + len(matrix_slice[0]) // 2):
        try:
            matrix3d[MATR][MATR][ind][index_l_y] = matrix_slice[slice_row_ind][slice_col_ind]
        except IndexError:
            print(MATR)
            print(ind)
            print(index_l_y)
            print(slice_row_ind)
            print(slice_col_ind)
            exit(-1)
        slice_col_ind += 1
    slice_row_ind += 1
    if slice_row_ind >= len(matrix_slice):
        break

print('PULA')
for cycle in range(6):
    print(f"Cycle: {cycle}")
    copy_matrix3d = []
    for ind_w in range(MATRIX_BOUND):
        dim = []
        for ind_z in range(MATRIX_BOUND):
            slc = []
            for index_x in range(MATRIX_BOUND):
                line = []
                for index_y in range(MATRIX_BOUND):
                    line.append(matrix3d[ind_w][ind_z][index_x][index_y])
                slc.append(line)
            dim.append(slc)
        copy_matrix3d.append(dim)
    for ind_w in range(1, len(matrix3d) - 1):
        print(ind_w)
        for ind_z in range(1, len(matrix3d[ind_w]) - 1):
            for ind_x in range(1, len(matrix3d[ind_w][ind_z]) - 1):
                for ind_y in range(1, len(matrix3d[ind_w][ind_z][ind_x]) - 1):
                    matrix3d[ind_w][ind_z][ind_x][ind_y] = change_state(copy_matrix3d, (ind_x, ind_y, ind_z, ind_w))


print(sum(x.count('#') for w in matrix3d for z in w for x in z))
