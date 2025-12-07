
with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [lines.replace("\n", "") for lines in lines]
lines = [[char for char in line] for line in lines]

count = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            lines[i+1][j] = "|"
        if char == "^":
            if lines[i-1][j] == "|":
                lines[i][j-1] = "|"
                lines[i][j+1] = "|"
                count += 1
        else:
            if lines[i-1][j] == "|":
                lines[i][j] = "|"

for line in lines:
    print(line)

print("")
print(count)