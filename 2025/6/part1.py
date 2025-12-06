import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [item.replace("\n", "").split(" ") for item in lines]
lines = [[num for num in row if num] for row in lines]

array = np.array(lines)
array = array.transpose()

results = []
for row in array:
    operator = row[-1]
    expression = f"{operator}".join(row[:-1])
    results.append(eval(expression))

print(sum(results))

