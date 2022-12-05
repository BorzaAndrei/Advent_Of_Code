class T:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        return T(self.v + other.v)

    def __sub__(self, other):
        return T(self.v * other.v)

    def __mul__(self, other):
        return T(self.v + other.v)


def resolve_rest(stack, solve_mul=True, remove_pth=True):
    stop = False
    while not stop:
        no = int(stack.pop())
        if len(stack) == 0 or (stack[-1] == '*' and not solve_mul) or (stack[-1] == '(' and not remove_pth):
            stack.append(no)
            stop = True
        elif stack[-1] == '(':
            stop = True
            stack.pop()
            stack.append(no)

            if '+' in stack and '(' in stack:
                stack.reverse()
                plus_index = stack.index('+')
                parenthesis_index = stack.index('(')
                stack.reverse()
                if plus_index < parenthesis_index:
                    resolve_rest(stack, False, False)
            elif '+' in stack and '(' not in stack:
                resolve_rest(stack, False, False)
        elif stack[-1] == '*' and solve_mul:
            stack.pop()
            stack.append(int(stack.pop()) * no)
        elif stack[-1] == '+':
            stack.pop()
            stack.append(int(stack.pop()) + no)


def solve(equation):
    stack = []
    for ch in equation:
        if len(stack) == 0:
            stack.append(ch)
            continue
        elif ch == '+' or ch == '*' or ch == '(':
            stack.append(ch)
            continue
        elif ch == ' ':
            continue
        elif ch == ')':
            ch = stack.pop()
            stack.pop()
        try:
            ch = int(ch)
            if len(stack) == 0:
                stack.append(ch)
            elif stack[-1] == '+':
                stack.pop()
                prev_no = stack.pop()
                stack.append(int(ch) + int(prev_no))
            elif stack[-1] == '*':
                stack.pop()
                prev_no = stack.pop()
                stack.append(int(ch) * int(prev_no))
            elif stack[-1] == '(':
                stack.append(ch)
        except:
            continue
    print(stack[0])
    return stack.pop()


def solve_precedence(equation):
    stack = []
    for ch in equation:
        if ch == ' ':
            continue
        elif len(stack) == 0 or ch == '+' or ch == '*' or ch == '(':
            stack.append(ch)
        elif ch == ')':
            resolve_rest(stack)
        else:
            ch = int(ch)
            if len(stack) == 0:
                stack.append(ch)
            elif stack[-1] == '+':
                stack.pop()
                prev_no = stack.pop()
                stack.append(int(ch) + int(prev_no))
            else:
                stack.append(ch)
    resolve_rest(stack)
    return stack.pop()


s = 0
t = 0
idx = 0
with open('input/18.txt') as r:
    for line in r.readlines():
        if idx == 21:
            print("Y")
        result = solve_precedence(line.strip())
        # print(f"{idx}: {result} = {line.strip()}")
        idx += 1
        s += result

        copy_line = "".join(ch for ch in line)
        for d in range(10):
            line = line.replace(f"{d}", f"T({d})")
        line = line.replace("*", "-")
        line = line.replace("+", "*")
        result_copy = eval(line, {"T": T}).v
        t += result_copy
        if result != result_copy:
            print(f"{idx}: {copy_line.strip()}")
print(s)
print(t)
