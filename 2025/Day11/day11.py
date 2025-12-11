print("2025 - Day 11")
from functools import cache

with open("./2025/Day11/input.txt") as file:
    lines = [line.rstrip() for line in file]

graph = {}
for line in lines:
    parts = line.split(":")
    graph[parts[0]] = parts[1].split()


def search1(source):
    if source == "out":
        return 1
    return sum([search1(next) for next in graph[source]])


@cache
def search2(source, dac, fft):
    if source == "out":
        if dac and fft:
            return 1
        else:
            return 0
    if source == "dac":
        dac = True
    if source == "fft":
        fft = True
    return sum([search2(next, dac, fft) for next in graph[source]])


p1 = search1("you")
p2 = search2("svr", False, False)

print("------------------------")
print("Part 1:", p1)
print("------------------------")
print("Part 2:", p2)
print("------------------------")
