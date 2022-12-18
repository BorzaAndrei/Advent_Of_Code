from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ShapeStack:
    stack = [[1 for _ in range(7)]]
    current_shape: Optional[Shape]
    w = 0
    pos_x_shape: Optional[int]
    pos_y_shape: Optional[int]
    movement = 'h'
    direction: Optional[str]

    def add_empty(self, h=3):
        for _ in range(h):
            self.stack.append([0 for _ in range(7)])

    def clean_empty_top(self):
        for line_ind in range(len(self.stack) - 1, -1, -1):
            if len([x for x in self.stack[line_ind] if x > 0]) == 0:
                self.stack.pop()
            else:
                break

    def place_shape_beginning(self):
        self.add_empty(3)
        self.add_empty(self.current_shape.get_height())
        self.pos_x_shape = (len(self.stack)) - 1
        self.pos_y_shape = 2

    def change_movement(self):
        match self.movement:
            case 'h':
                self.movement = 'v'
            case 'v':
                self.movement = 'h'

    def can_shape_move(self):
        bottom_line_x, bottom_line_y = self.current_shape.get_bottom_right_corner()
        actual_blx, actual_bly = self.pos_x_shape - bottom_line_x + 1, self.pos_y_shape + bottom_line_y - 1
        if self.movement == 'v':
            for shape_line_ind in range(len(self.current_shape.actual_shape)):
                for shape_col_ind in range(len(self.current_shape.actual_shape[0])):
                    if self.stack[self.pos_x_shape - shape_line_ind - 1][self.pos_y_shape + shape_col_ind] >= 1 \
                            and self.current_shape.actual_shape[shape_line_ind][shape_col_ind] == 1:
                        return False
            return True
        else:
            check_col = -1
            shape_col_ind = -1
            match self.direction:
                case '>':
                    check_col = actual_bly + 1
                    shape_col_ind = len(self.current_shape.actual_shape[0]) - 1
                    stop_col = check_col - len(self.current_shape.actual_shape[0])

                    if check_col < 0 or check_col >= 7:
                        return False

                    for col in range(check_col, stop_col, -1):
                        shape_line_ind = 0
                        for line_ind in range(self.pos_x_shape, actual_blx - 1, -1):
                            if self.stack[line_ind][col] >= 1 \
                                    and self.current_shape.actual_shape[shape_line_ind][shape_col_ind] == 1:
                                return False
                            shape_line_ind += 1
                        shape_col_ind -= 1
                    return True

                case '<':
                    check_col = self.pos_y_shape - 1
                    stop_col = check_col + len(self.current_shape.actual_shape[0])
                    shape_col_ind = len(self.current_shape.actual_shape[0]) - 1

                    if check_col < 0 or check_col >= 7:
                        return False

                    for col in range(stop_col - 1, check_col - 1, - 1):
                        shape_line_ind = 0
                        for line_ind in range(self.pos_x_shape, actual_blx - 1, -1):
                            if self.stack[line_ind][col] >= 1 \
                                    and self.current_shape.actual_shape[shape_line_ind][shape_col_ind] == 1:
                                return False
                            shape_line_ind += 1
                        shape_col_ind -= 1
                    return True

    def move_shape(self):
        if self.movement == 'v':
            self.pos_x_shape -= 1
        else:
            match self.direction:
                case '>':
                    self.pos_y_shape += 1
                case '<':
                    self.pos_y_shape -= 1

    def store_shape(self):
        actual_line = self.pos_x_shape
        actual_col = self.pos_y_shape
        for line_ind in range(len(self.current_shape.actual_shape)):
            for col_ind in range(len(self.current_shape.actual_shape[line_ind])):
                if self.current_shape.actual_shape[line_ind][col_ind] == 1:
                    if self.stack[actual_line][actual_col + col_ind] > 0:
                        pass
                    self.stack[actual_line][actual_col + col_ind] = w
            actual_line -= 1


@dataclass
class Shape:
    name: str
    actual_shape: List[List[int]]

    def get_bottom_right_corner(self):
        return len(self.actual_shape), len(self.actual_shape[-1])

    def get_height(self):
        return len(self.actual_shape)


@dataclass
class ShapeManager:
    shapes = {
        "line": Shape('line', [[1, 1, 1, 1]]),
        "plus": Shape('plus', [[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
        "l": Shape('l', [[0, 0, 1], [0, 0, 1], [1, 1, 1]]),
        "v-line": Shape('v-line', [[1], [1], [1], [1]]),
        "square": Shape('square', [[1, 1], [1, 1]])
    }
    count = 0
    next_shape = 'line'
    shapes_name = ['line', 'plus', 'l', 'v-line', 'square']

    def generate_next_shape(self):
        new_shape = self.shapes[self.next_shape]
        self.count += 1
        self.next_shape = self.shapes_name[(self.shapes_name.index(self.next_shape) + 1) % len(self.shapes_name)]
        return new_shape, self.shapes_name.index(self.next_shape) + 1


file = open("input.txt")
wind = file.readline().strip('\n')
file.close()

shape_manager = ShapeManager()
shape_stack = ShapeStack(None, None, None, None)
wind_ind = 0
c = 0
cycle_stack = []
while shape_manager.count < 2022:
    shape, w = shape_manager.generate_next_shape()
    shape_stack.current_shape = shape
    shape_stack.w = w
    shape_stack.place_shape_beginning()
    shape_stack.movement = 'h'
    shape_stack.direction = wind[wind_ind % len(wind)]
    movement_stack = []
    wind_ind += 1
    cant_move_down = False
    if shape_stack.current_shape.name == 'l':
        pass
    while not cant_move_down:
        can_move = shape_stack.can_shape_move()
        if can_move:
            shape_stack.move_shape()
        elif not can_move and shape_stack.movement == 'v':
            cant_move_down = True
            shape_stack.store_shape()
            # 
            # print(movement_stack)
            # for l in list(reversed(shape_stack.stack)):
            #     print(l)
            # print("-----------------------------------------\n")
            if movement_stack in cycle_stack:
                for c in cycle_stack:
                    print(c)
                pass
            cycle_stack.append(movement_stack)

            shape_stack.clean_empty_top()

            break
        movement_stack.append(
            (shape_stack.current_shape.name, shape_stack.movement, shape_stack.direction if shape_stack.movement == 'h' else "", can_move))
        shape_stack.change_movement()
        if shape_stack.movement == 'h':
            shape_stack.direction = wind[wind_ind % len(wind)]
            wind_ind += 1
print(c + len(shape_stack.stack) - 1)
