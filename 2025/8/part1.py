import math

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.replace("\n", "") for line in lines]
print(lines)
distance_dict = {}

while lines:
    line = lines.pop(0)
    x = tuple([int(i) for i in line.split(",")])
    for l in lines:
        y = tuple([int(i) for i in l.split(",")])
        distance_dict[line].append((l, math.dist(x, y)))
    break

print(distance_dict)

for key, values in distance_dict.items():
    coord = values[0][0]
    dist = values[0][1]

    for val in values:
        if val[1] < dist:
            coord = val[0]

    print(f"The shortest route from {key} is to {coord} with a distance of {dist}")


