from __future__ import annotations
from dataclasses import dataclass
import re


@dataclass
class ValveRoom:
    name: str
    flow: int
    leads_to = []
    leads_to_names = []
    current_flow = 0

    def paths_available(self, visited):
        for vr in self.leads_to:
            if (self.name, vr.name) not in visited and (vr.name, self.name) not in visited:
                return True
        return False

    def calculate_max_score(self, score, time, visited, skipped, all_valves, came_from=None):
        any_open = False
        for v in all_valves:
            if v.current_flow == v.flow:
                any_open = True

        changed_here = False
        if self.current_flow > 0 or not any_open and time > 0:
            changed_here = True
            time -= 1
            score += self.flow * time
            self.current_flow = 0

        max_score = 0
        max_path = []
        no_path_available = True
        if time != 0:
            for vr in self.leads_to:
                if (came_from is None or came_from != vr.name or not vr.paths_available(visited)) and (
                        (self.name, vr.name) not in visited or vr.paths_available(visited)):
                    no_path_available = False
                    s, path, skipped = vr.calculate_max_score(score, time - 1, visited + [(self.name, vr.name)],
                                                              skipped, all_valves, self.name)
                    if changed_here:
                        score_without_opening_this, path_without_opening_this, skipped = vr.calculate_max_score(
                            score - self.flow * time, time, visited + [(self.name, vr.name)], skipped, all_valves,
                            self.name)
                        if score_without_opening_this > s:
                            skipped.add(self.name)
                            s, path = score_without_opening_this, path_without_opening_this
                    if s > max_score:
                        max_score = s
                        max_path = path
        if time == 0 or no_path_available:
            max_path = visited
            max_score = score
        if changed_here:
            self.current_flow = self.flow

        # any_open = False
        # for v in all_valves:
        #     if v.current_flow == v.flow:
        #         any_open = True
        # 
        # # Pickup stragglers
        # if any_open and len(skipped) > 0:
        #     for v in self.leads_to:

        return max_score, max_path, skipped

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

for v in valves:
    for vlt in v.leads_to_names:
        v.leads_to.append([valve for valve in valves if valve.name == vlt][0])

print(valves[0].calculate_max_score(0, 30, [], set(), valves))
