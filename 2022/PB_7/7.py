from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SystemItem:
    name: str

    def calculate_size(self):
        pass

    def is_dir(self) -> bool:
        pass


@dataclass
class File(SystemItem):
    size: int

    def calculate_size(self):
        return self.size

    def is_dir(self):
        return False


@dataclass
class Dir(SystemItem):
    parent: Optional[Dir]
    content: List[SystemItem]

    def calculate_size(self):
        size = 0
        for item in self.content:
            size += item.calculate_size()
        return size

    def is_dir(self):
        return True


@dataclass
class DirManagement:
    current_dir: Optional[Dir]
    home_dir: Dir

    def prev(self):
        self.current_dir = self.current_dir.parent

    def cd(self, dir_name):
        if dir_name == '..':
            self.prev()
        else:
            if dir_name == '/':
                self.current_dir = self.home_dir
            for c in self.current_dir.content:
                if c.name == dir_name and c.is_dir():
                    self.current_dir = c


home = Dir("/", None, [])
dirManagement = DirManagement(None, home)
with open("input.txt") as file:
    for line in file.readlines():
        stripped_line = line.strip('\n')
        if '$' in stripped_line:
            split_line = stripped_line.split()
            if split_line[1] == 'cd':
                dirManagement.cd(split_line[2])
        else:
            if 'dir' not in stripped_line:
                file_length, file_name = stripped_line.split()
                file = File(file_name, int(file_length))
                dirManagement.current_dir.content.append(file)
            else:
                new_dir = Dir(stripped_line.split()[1], dirManagement.current_dir, [])
                dirManagement.current_dir.content.append(new_dir)

s = 0
to_delete = 30000000 - (70000000 - dirManagement.home_dir.calculate_size())  # need - (total - currently_occupied)
bigger = []


def pretty_print_dirs_check_sizes(base_dir: Dir, depth):
    global s
    size = base_dir.calculate_size()
    if size <= 100000:
        s += size
    if size >= to_delete:
        bigger.append(size)
    print(f"{'🍔' * depth}{base_dir.name} - {size}".replace("🍔", "\t"))
    for f in base_dir.content:
        if f.is_dir():
            pretty_print_dirs_check_sizes(f, depth + 1)
        else:
            print(f"{'🍔' * (depth + 1)}{f.name} - {f.calculate_size()}".replace("🍔", "\t"))


pretty_print_dirs_check_sizes(home, 0)

print(s)  # total sizes of files under 100000
print(sorted(bigger)[0])  # smallest file size needed to delete
