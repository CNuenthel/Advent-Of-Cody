
with open("input.txt", "r") as f:
    data = f.readlines()
lines = [[char for char in line.replace("\n", "")] for line in data]

count = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            lines[i+1][j] = "|"
        elif char == "^":
            if lines[i-1][j] == "|":
                lines[i][j-1] = "|"
                lines[i][j+1] = "|"
                count += 1
        elif char == ".":
            if lines[i-1][j] == "|":
                lines[i][j] = "|"

print(count)

