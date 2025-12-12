
with open("input.txt", "r") as f:
    data = f.readlines()
lines = [[char for char in line.replace("\n", "")] for line in data]

rows = len(lines)
cols = len(lines[0])
ways = [[0]*cols for _ in range(rows)]

for x, ch in enumerate(lines[0]):
    if ch == 'S':
        ways[0][x] = 1

for y in range(rows):
    for x in range(cols):
        w = ways[y][x]
        if w == 0:
            continue

        cell = lines[y][x]

        if cell == '|' or cell == 'S' or cell == '.':
            if y+1 < rows:
                ways[y+1][x] += w

        if cell == '^':
            if y+1 < rows and x-1 >= 0:
                ways[y+1][x-1] += w
            if y+1 < rows and x+1 < cols:
                ways[y+1][x+1] += w

def display_ways(ways):
    for row in ways:
        formatted = [
            f"{val:4d}" if val != 0 else "   ."
            for val in row
        ]
        print(" ".join(formatted))

# display_ways(ways)
total_paths = sum(ways[rows-1])
# print(total_paths)
