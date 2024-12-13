print("2024 - Day 13")

with open("./2024/Day13/input.txt") as file:
    lines = [line.rstrip() for line in file]

machines = [{}]

for line in lines:
    if line == "\n":
        continue
    if "Button" in line:
        parts = line.split(":")
        button = parts[0].split(" ")[-1]
        moves = parts[1].split(",")
        moves[0] = int(moves[0].split("+")[-1])
        moves[1] = int(moves[1].split("+")[-1])
        machines[-1][button] = moves
    elif "Prize" in line:
        parts = line.split(":")[-1].split(", ")
        prize = [0, 0]
        prize[0] = int(parts[0].split("=")[-1])
        prize[1] = int(parts[1].split("=")[-1])
        machines[-1]["prize"] = prize
    else:
        machines.append({})


def get_cost(machines, part2=False):
    for machine in machines:
        prize = machine["prize"]
        amoves = machine["A"]
        bmoves = machine["B"]

        xa = amoves[0]
        xb = bmoves[0]
        ya = amoves[1]
        yb = bmoves[1]
        if part2:
            xp = prize[0] + 10000000000000
            yp = prize[1] + 10000000000000
        else:
            xp = prize[0]
            yp = prize[1]

        a = (xb * yp - yb * xp) / (ya * xb - xa * yb)
        b = (ya * xp - xa * yp) / (ya * xb - xa * yb)

        if int(a) == a and int(b) == b:
            machine["cost"] = int(a) * 3 + int(b)
        else:
            machine["cost"] = 0

    return sum([m["cost"] for m in machines])


print("------------------------")
print("Part 1:", get_cost(machines))
print("------------------------")
print("Part 2:", get_cost(machines, part2=True))
print("------------------------")
