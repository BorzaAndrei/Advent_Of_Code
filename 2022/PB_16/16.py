from __future__ import annotations

import math
from dataclasses import dataclass
import re
import itertools


@dataclass
class ValveRoom:
    name: str
    flow: int
    leads_to = []
    leads_to_names = []

    def __str__(self):
        return f"Valve {self.name} - Rate={self.flow} - Leads To: {','.join([v.name for v in self.leads_to])}"


valves = []
with open("input.txt") as file:
    for line in file.readlines():
        v_name = re.search('Valve ([A-Z]{2})', line).group(1)
        v_rate = re.search('rate=([0-9]+)', line).group(1)
        v_leads_to = line[line.find('valve') + len('valves'):].strip().strip('\n').split(', ')
        v = ValveRoom(v_name, int(v_rate))
        v.leads_to_names = v_leads_to
        v.leads_to = []
        v.current_flow = v.flow
        valves.append(v)

non_empty_valves = set()
for v in valves:
    for vlt in v.leads_to_names:
        v.leads_to.append([valve for valve in valves if valve.name == vlt][0])
    if v.flow > 0:
        non_empty_valves.add(v.name)

dist = {v.name: {vlt.name: math.inf for vlt in valves} for v in valves}
nxt = {v.name: {vlt.name: None for vlt in valves} for v in valves}
for v in valves:
    dist[v.name][v.name] = 0
    nxt[v.name][v.name] = v
    for vlt in v.leads_to:
        dist[v.name][vlt.name] = 1
        nxt[v.name][vlt.name] = vlt
for k in range(len(valves)):
    for i in range(len(valves)):
        for j in range(len(valves)):
            vlv_i = valves[i].name
            vlv_j = valves[j].name
            vlv_k = valves[k].name
            if dist[vlv_i][vlv_j] > dist[vlv_i][vlv_k] + dist[vlv_k][vlv_j]:
                dist[vlv_i][vlv_j] = dist[vlv_i][vlv_k] + dist[vlv_k][vlv_j]
                nxt[vlv_i][vlv_j] = nxt[vlv_i][vlv_k]


def calculate_score(all_valves, distances, start, score, time_left, opened, non_empty):
    if len(non_empty - opened) == 0 or time_left == 0:
        return score
    max_score = 0
    for v_name in non_empty - opened:
        if time_left - distances[start.name][v_name] - 1 >= 0:
            opened.add(v_name)
            v = [x for x in all_valves if x.name == v_name][0]
            s = calculate_score(all_valves, distances, v,
                                score + (time_left - distances[start.name][v_name] - 1) * v.flow,
                                time_left - distances[start.name][v_name] - 1, opened, non_empty)
            opened.remove(v_name)
            if s > max_score:
                max_score = s
    return max(score, max_score)


max_global = 0
for comb in itertools.combinations(non_empty_valves, len(non_empty_valves) // 2):
    combinations = set(comb)
    rest = non_empty_valves - combinations
    score_me = calculate_score(valves, dist, [x for x in valves if x.name == "AA"][0], 0, 26, set(), combinations)
    score_elephant = calculate_score(valves, dist, [x for x in valves if x.name == "AA"][0], 0, 26, set(), rest)
    if score_me + score_elephant > max_global:
        max_global = score_me + score_elephant
print(max_global)
