from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SystemItem:
    name: str

    def calculate_size(self):
        pass


@dataclass
class File(SystemItem):
    size: int

    def calculate_size(self):
        return self.size


@dataclass
class Dir(SystemItem):
    parent: Optional[Dir]
    files: List[File]
    child_dirs: List[Dir]

    def calculate_size(self):
        size = 0
        for f in self.files:
            size += f.calculate_size()
        for child_d in self.child_dirs:
            size += child_d.calculate_size()
        return size


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
            for c in self.current_dir.child_dirs:
                if c.name == dir_name:
                    self.current_dir = c


home = Dir("/", None, [], [])
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
                dirManagement.current_dir.files.append(file)
            else:
                new_dir = Dir(stripped_line.split()[1], dirManagement.current_dir, [], [])
                dirManagement.current_dir.child_dirs.append(new_dir)

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
    for f in base_dir.files:
        print(f"{'🍔' * (depth + 1)}{f.name} - {f.calculate_size()}".replace("🍔", "\t"))
    for child_d in base_dir.child_dirs:
        pretty_print_dirs_check_sizes(child_d, depth + 1)


pretty_print_dirs_check_sizes(home, 0)

print(s)  # total sizes of files under 100000
print(sorted(bigger)[0])  # smallest file size needed to delete
