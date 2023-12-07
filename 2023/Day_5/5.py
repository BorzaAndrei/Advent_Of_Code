from dataclasses import dataclass, field
from typing import List


def process_map(seed, map_name, textIO):
    pass

@dataclass
class Map:
    source_start: int
    destination_start: int
    range_length: int

    def __str__(self) -> str:
        return f"Source: {self.source_start} - Dest: {self.destination_start} - Range: {self.range_length}"

@dataclass
class TopLevelMap:
    maps: List[Map] = field(default_factory=list)

    def addMap(self, toAdd: Map):
        self.maps.append(toAdd)
    
    def __str__(self) -> str:
        return f"{[m for m in self.maps]}"

@dataclass
class RepoTopLevelMaps:
    topLevelMaps: List[TopLevelMap] = field(default_factory=list)

    def addTopLevelMap(self, toAdd: TopLevelMap):
        self.topLevelMaps.append(toAdd)

    def mapSeed(self, seed):
        print
        current_value = seed
        for tlm in self.topLevelMaps:
            for m in tlm.maps:
                if m.source_start <= current_value < m.source_start + m.range_length:
                    current_value = m.destination_start + (current_value - m.source_start)
                    break
        return current_value
                
    
    def __str__(self) -> str:
        rt = ""
        for tp in self.topLevelMaps:
            rt += str(tp) + '\n'
        return rt


with open("2023/Day_5/input.txt") as r:
    lines = r.readlines()
    seeds = list(map(int, lines[0].strip('\n').split(':')[1].strip(' ').split()))

    repo = RepoTopLevelMaps()
    
    topLevelMap = TopLevelMap()
    for ind in range(3, len(lines)):
        line = lines[ind].strip('\n')
        if len(line) > 0 and "to" not in line:
            dest, source, rng = line.split()
            topLevelMap.addMap(Map(int(source), int(dest), int(rng)))
        else:
            if len(topLevelMap.maps) > 0:
                repo.addTopLevelMap(topLevelMap)
                topLevelMap = TopLevelMap()
            r.readline()
    repo.addTopLevelMap(topLevelMap)

    print(min([repo.mapSeed(seed) for seed in seeds]))
    results = []
    for start, rng in zip(seeds[0::2], seeds[1::2]):
        print(f"{start}-{rng}")
        for x in range(start, start + rng, 16):
            results.append(repo.mapSeed(x))
    print(min(results))
