from functools import reduce
import re

def beats_record(speed, total_time, record):
    return speed * (total_time - speed) > record

with open("2023/Day_6/input.txt") as r:
    # Part 1
    time_line = r.readline().strip('\n')
    dist_line = r.readline().strip('\n')
    time = [int(m) for m in re.findall("\d+", time_line)]
    dist = [int(m) for m in re.findall("\d+", dist_line)]

    print(reduce(lambda x, y: x * y, [sum(filter(None, [beats_record(s, time[ind], dist[ind]) for s in range(time[ind])])) for ind in range(len(time))]))

    # Part 2
    time = int(time_line.split(':')[1].replace(' ', ''))
    dist = int(dist_line.split(':')[1].replace(' ', ''))    

    print(sum(filter(None, [beats_record(s, time, dist) for s in range(time)]))) 
