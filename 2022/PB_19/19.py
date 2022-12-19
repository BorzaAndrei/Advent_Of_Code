from dataclasses import dataclass, replace
import re


@dataclass
class Robot:
    ore_cost: int
    clay_cost: int
    obsidian_cost: int


@dataclass
class Blueprint:
    id: int
    ore_robot: Robot
    clay_robot: Robot
    obsidian_robot: Robot
    geode_robot: Robot


@dataclass
class ResourceManager:
    blueprint: Blueprint
    no_ore_robots: int
    no_clay_robots: int
    no_obsidian_robots: int
    no_geode_robots: int
    ore: int
    clay: int
    obsidian: int
    geode: int
    current_no_ore_robots = 0
    current_no_clay_robots = 0
    current_no_obsidian_robots = 0
    current_no_geode_robots = 0
    depth_left = 6

    def start_building(self):
        self.current_no_ore_robots = self.no_ore_robots
        self.current_no_clay_robots = self.no_clay_robots
        self.current_no_obsidian_robots = self.no_obsidian_robots
        self.current_no_geode_robots = self.no_geode_robots

    def collect_resources(self):
        self.ore += self.current_no_ore_robots
        self.clay += self.current_no_clay_robots
        self.obsidian += self.current_no_obsidian_robots
        self.geode += self.current_no_geode_robots

    def build_robot(self, robot_type):
        match robot_type:
            case 'ore':
                if self.blueprint.ore_robot.ore_cost <= self.ore:
                    self.no_ore_robots += 1
                    self.ore -= self.blueprint.ore_robot.ore_cost
                    return True
                return False
            case 'clay':
                if self.blueprint.clay_robot.ore_cost <= self.ore:
                    self.no_clay_robots += 1
                    self.ore -= self.blueprint.clay_robot.ore_cost
                    return True
                return False
            case 'obsidian':
                if self.blueprint.obsidian_robot.ore_cost <= self.ore \
                        and self.blueprint.obsidian_robot.clay_cost <= self.clay:
                    self.no_obsidian_robots += 1
                    self.ore -= self.blueprint.obsidian_robot.ore_cost
                    self.clay -= self.blueprint.obsidian_robot.clay_cost
                    return True
                return False
            case 'geode':
                if self.blueprint.geode_robot.ore_cost <= self.ore \
                        and self.blueprint.geode_robot.obsidian_cost <= self.obsidian:
                    self.no_geode_robots += 1

                    self.ore -= self.blueprint.geode_robot.ore_cost
                    self.obsidian -= self.blueprint.geode_robot.obsidian_cost
                    return True
                return False

    def build_robots(self):
        new_rms = []
        built = self.build_robot('geode')
        if not built:
            built = self.build_robot('obsidian')
        if not built:
            if self.blueprint.clay_robot.ore_cost <= self.ore < self.blueprint.ore_robot.ore_cost and self.no_clay_robots <= self.blueprint.obsidian_robot.clay_cost:
                if self.depth_left - 1 > 0:
                    new_rm = replace(self)
                    new_rm.depth_left = self.depth_left - 1
                    new_rm.start_building()
                    new_rm.collect_resources()
                    new_rms.append(new_rm)
                self.build_robot('clay')
            elif self.blueprint.clay_robot.ore_cost <= self.ore and self.blueprint.ore_robot.ore_cost <= self.ore:
                if self.depth_left - 1 > 0:
                    if self.no_clay_robots <= self.blueprint.obsidian_robot.clay_cost:
                        new_rm = replace(self)
                        new_rm.depth_left = self.depth_left - 1
                        new_rm.start_building()
                        new_rm.build_robot('clay')
                        new_rm.collect_resources()
                        new_rms.append(new_rm)

                    if self.no_ore_robots <= max(self.blueprint.obsidian_robot.ore_cost,
                                                 self.blueprint.geode_robot.ore_cost):
                        new_rm = replace(self)
                        new_rm.depth_left = self.depth_left - 1
                        new_rm.start_building()
                        new_rm.build_robot('ore')
                        new_rm.collect_resources()
                        new_rms.append(new_rm)
                elif self.no_clay_robots <= self.blueprint.obsidian_robot.clay_cost:
                    self.build_robot('clay')

            elif self.blueprint.clay_robot.ore_cost > self.ore >= self.blueprint.ore_robot.ore_cost and self.no_ore_robots <= max(
                    self.blueprint.obsidian_robot.ore_cost, self.blueprint.geode_robot.ore_cost):
                if self.depth_left - 1 > 0:
                    new_rm = replace(self)
                    new_rm.depth_left = self.depth_left - 1
                    new_rm.start_building()
                    new_rm.collect_resources()
                    new_rms.append(new_rm)
                self.build_robot('ore')
        return new_rms


def read_blueprints():
    bpr = []
    with open("input.txt") as file:
        for line in file.readlines():
            blueprint_id = re.search("Blueprint ([0-9]+)", line).group(1)
            ore_costs = re.findall("costs ([0-9]+)", line)
            ore_robot = Robot(int(ore_costs[0]), 0, 0)
            clay_robot = Robot(int(ore_costs[1]), 0, 0)
            other_costs = re.findall("and ([0-9]+)", line)
            obsidian_robot = Robot(int(ore_costs[2]), int(other_costs[0]), 0)
            geode_robot = Robot(int(ore_costs[3]), 0, int(other_costs[1]))
            bp = Blueprint(int(blueprint_id), ore_robot, clay_robot, obsidian_robot, geode_robot)
            bpr.append(bp)
    return bpr


blueprints = read_blueprints()
s = 0
mul = 1
MAX_TIME = 32  # 24 for Part 1

# Only first 3 blueprints for part 2
for blueprint in blueprints[:3]:
    time = 1
    resource_managers = [ResourceManager(blueprint, 1, 0, 0, 0, 0, 0, 0, 0)]
    while time <= MAX_TIME:
        # print(f"Time: {time} - No rms: {len(resource_managers)}")
        new_resource_managers = []
        for rm in resource_managers:
            rm.start_building()
            list_new_rms = rm.build_robots()
            new_resource_managers.append(list_new_rms)
            rm.collect_resources()
        for lnrm in new_resource_managers:
            for nrm in lnrm:
                resource_managers.append(nrm)
        time += 1

    maxim = max(rm.geode for rm in resource_managers)
    print(f"{blueprint.id}: {maxim}")
    s += blueprint.id * maxim  # Used for part 1
    mul *= maxim

print(f"Sum of blueprint id * max_geodes: {s}")
print(f"Multiply the max no of geodes from the first 3 blueprints: {mul}")
