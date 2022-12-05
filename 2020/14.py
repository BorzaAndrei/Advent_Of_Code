def read_assign(assign_string):
    assign_string_split = assign_string.split('=')
    address_string = assign_string_split[0].strip()
    return int(address_string[address_string.find('[')+1:address_string.find(']')]), int(assign_string_split[1].strip())


def apply_mask(new_value, mask):
    value_binary = bin(new_value)[2:].rjust(36, '0')
    constructed_values = []
    constructed_value = ""
    for ind in range(len(mask)):
        # if mask[ind] == '1' or mask[ind] == '0':
        #     constructed_value = constructed_value + mask[ind]
        # else:
        #     constructed_value = constructed_value + value_binary[ind]
        if len(constructed_values) == 0:
            if mask[ind] == '1':
                constructed_value += '1'
            elif mask[ind] == '0':
                constructed_value += value_binary[ind]
            else:
                constructed_values.append(constructed_value)
        if len(constructed_values) > 0:
            if mask[ind] == '1':
                for value_index in range(len(constructed_values)):
                    constructed_values[value_index] = constructed_values[value_index] + '1'
            elif mask[ind] == '0':
                for value_index in range(len(constructed_values)):
                    constructed_values[value_index] = constructed_values[value_index] + value_binary[ind]
            else:
                for value_index in range(len(constructed_values)):
                    constructed_values.append(constructed_values[value_index] + '1')
                    constructed_values[value_index] = constructed_values[value_index] + '0'
    return constructed_values


def calculate_leftovers(memory):
    # return sum(int(memory[key], 2) for key in memory)
    return sum(memory[key] for key in memory)


mem = {}
current_mask = None

with open("input/14.txt") as r:
    for line in r.readlines():
        if "mask" in line:
            current_mask = line.split('=')[1].strip()
        else:
            address, value = read_assign(line)
            # mem[address] = apply_mask(value, current_mask)
            address_list = apply_mask(address, current_mask)
            for address in address_list:
                mem[int(address, 2)] = value

print(calculate_leftovers(mem))
