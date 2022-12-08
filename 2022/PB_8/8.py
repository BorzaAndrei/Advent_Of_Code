matrix = []
with open("input.txt") as file:
    for line in file.readlines():
        matrix.append([int(x) for x in line.strip('\n')])


def check_direction(matrix, start, end, step, other, el, row):
    if row:
        for row_ind in range(start, end, step):
            if matrix[row_ind][other] >= el:
                return False
        return True
    else:
        for col_ind in range(start, end, step):
            if matrix[other][col_ind] >= el:
                return False
        return True


def count_direction(matrix, start, end, step, other, el, row):
    c = 0
    if row:
        for row_ind in range(start, end, step):
            if matrix[row_ind][other] >= el:
                c += 1
                return c
            c += 1
        return c
    else:
        for col_ind in range(start, end, step):
            if matrix[other][col_ind] >= el:
                c += 1
                return c
            c += 1
        return c


def count(matrix, el_row, el_col, el):
    c = 1
    c *= count_direction(matrix, el_row + 1, len(matrix), 1, el_col, el, True)
    c *= count_direction(matrix, el_row - 1, -1, -1, el_col, el, True)
    c *= count_direction(matrix, el_col + 1, len(matrix[0]), 1, el_row, el, False)
    c *= count_direction(matrix, el_col - 1, -1, -1, el_row, el, False)
    return c


def is_visible(matrix, el_row, el_col, el):
    if el_row == 0 or el_row == len(matrix) - 1 or el_col == 0 or el_col == len(matrix[0]) - 1:
        return True
    else:

        visible = check_direction(matrix, el_row + 1, len(matrix), 1, el_col, el, True)
        if visible:
            return True
        visible = check_direction(matrix, el_row - 1, -1, -1, el_col, el, True)
        if visible:
            return True
        visible = check_direction(matrix, el_col + 1, len(matrix[0]), 1, el_row, el, False)
        if visible:
            return True
        visible = check_direction(matrix, el_col - 1, -1, -1, el_row, el, False)
        if visible:
            return True
        return False


print(sum(1
          for row_ind in range(len(matrix))
          for col_ind in range(len(matrix[row_ind]))
          if is_visible(matrix, row_ind, col_ind, matrix[row_ind][col_ind])
          ))

print(max(count(matrix, row_ind, col_ind, matrix[row_ind][col_ind])
          for row_ind in range(len(matrix))
          for col_ind in range(len(matrix[row_ind]))
          )
      )
