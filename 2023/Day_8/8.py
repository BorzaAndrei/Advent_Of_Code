from dataclasses import dataclass
from functools import reduce
import math
from typing import ForwardRef, List, Tuple
import re


@dataclass
class Node:
    name: str
    left: ForwardRef('Node') = None
    right: ForwardRef('Node') = None

    def __str__(self) -> str:
        return f"{self.name} - {self.left.name}|{self.right.name}"
    

@dataclass
class Step:
    instruction_index: int
    node: str

    def __eq__(self, other) -> bool:
        return self.instruction_index == other.instruction_index and self.node == other.node
    
    def __str__(self) -> str:
        return f"({self.node}-{self.instruction_index})"

@dataclass
class Cycle:
    node: Node
    history_list: List[Step]
    steps_before: int

    def when_on_ending(self, ending_nodes):
        indexes = []
        for ind, step in enumerate(self.history_list):
            if step.node in ending_nodes:
                indexes.append(ind)
        return indexes



def steps_to(instructions: str, source: Node, destination: str):
    steps = 0
    ind_instruction = 0
    found = False
    current_node = source
    while not found:
        steps += 1

        current_instruction = instructions[ind_instruction]
        ind_instruction = ind_instruction + 1 if ind_instruction + 1 < len(instructions) else 0

        match current_instruction:
            case "R":
                current_node = current_node.right
            case "L":
                current_node = current_node.left
        
        if current_node.name == destination:
            found = True
    return steps

def detect_cycle(node: Node) -> Cycle:
    ind_instruction = 0
    found = False
    current_node = node
    history_list = [Step(ind_instruction, current_node.name)]
    steps_before = 0
    steps = 0
    while not found:
        steps += 1
        current_instruction = instructions[ind_instruction]
        ind_instruction = ind_instruction + 1 if ind_instruction + 1 < len(instructions) else 0

        match current_instruction:
            case "R":
                new_step = Step(ind_instruction, current_node.right.name)
                if new_step in history_list:
                    # history_list = history_list[history_list.index(new_step):]
                    # steps_before = len(history_list[:history_list.index(new_step)]) + 1
                    found = True
                else:
                    history_list.append(new_step)
                current_node = current_node.right
            case "L":
                new_step = Step(ind_instruction, current_node.left.name)
                if new_step in history_list:
                    # history_list = history_list[history_list.index(new_step):]
                    # steps_before = len(history_list[:history_list.index(new_step)]) + 1
                    found = True
                else:
                    history_list.append(new_step)
                current_node = current_node.left
        
    print(f"{node.name} - {steps_before}")
    return Cycle(node, history_list, steps_before)


def steps_to_multiple(instructions: str, starting_nodes: List[Node], ending_nodes: List[str]):
    steps = 0
    ind_instruction = 0
    found = False
    current_nodes = starting_nodes[:]
    while not found:
        if steps % 100 == 0:
            print(steps)
        steps += 1

        current_instruction = instructions[ind_instruction]
        ind_instruction = ind_instruction + 1 if ind_instruction + 1 < len(instructions) else 0

        match current_instruction:
            case "R":
                for ind in range(len(current_nodes)):
                    current_nodes[ind] = current_nodes[ind].right
            case "L":
                for ind in range(len(current_nodes)):
                    current_nodes[ind] = current_nodes[ind].left

        found = all([n.name in ending_nodes for n in current_nodes])

    return steps


nodes = []

def find_node(node_name, nodes):
    result = list(filter(lambda x: x.name == node_name, nodes))
    if len(result) == 0:
        return None
    return result[0]

with open("2023/Day_8/input.txt") as r:
    instructions = r.readline().strip('\n')
    r.readline()

    starting_nodes = []
    ending_nodes_names = []

    for line in r.readlines():
        mtch = re.findall("([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", line.strip('\n'))
        n, left, right = mtch[0][0], mtch[0][1], mtch[0][2]
        
        existing_left = find_node(left, nodes)
        if not existing_left:
            existing_left = Node(left)
            nodes.append(existing_left)
        existing_right = find_node(right, nodes)
        if not existing_right:
            existing_right = Node(right)
            nodes.append(existing_right)
        
        existing_node = find_node(n, nodes)
        if not existing_node:
            existing_node = Node(n, existing_left, existing_right)
        else:
            existing_node.left = existing_left
            existing_node.right = existing_right
        nodes.append(existing_node)

        if existing_node.name[-1] == 'A':
            starting_nodes.append(existing_node)
        elif existing_node.name[-1] == 'Z':
            ending_nodes_names.append(existing_node.name)

    # print(steps_to(instructions, find_node('AAA', nodes), 'ZZZ'))
    print([n.name for n in starting_nodes])

    # print(steps_to_multiple(instructions, starting_nodes, ending_nodes_names))
    # cycles = [detect_cycle(n) for n in starting_nodes]
    
    # for c in cycles:
    #     print(f"{c.node.name} - {c.steps_before} - {c.when_on_ending(ending_nodes_names)}")
    
    numbers = [17141, 16579, 18827, 12083, 13207, 22199]
    print(reduce(math.lcm, numbers))
    
