
with open("input.txt", "r") as f:
    lines = f.readlines()

cords = [line.replace("\n", "").split(",") for line in lines]

sums = []
for cord in cords:
    sums.append(int(cord[0]) + int(cord[1]))

minimum_cord = cords[sums.index(min(sums))]
maximum_cord = cords[sums.index(max(sums))]

area = (int(maximum_cord[0]) - int(minimum_cord[0])) * (int(maximum_cord[1]) - int(minimum_cord[1]))

print(area)