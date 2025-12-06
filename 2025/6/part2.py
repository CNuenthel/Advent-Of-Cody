import pandas as pd

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.replace("\n", "") for line in lines]
biggly_boi = max([len(line) for line in lines])

normalized_lines = []
for line in lines:
    if len(line) < biggly_boi:
        spaces = " "*(biggly_boi - len(line))
        normalized_lines.append(line + spaces)
    else:
        normalized_lines.append(line)

lines = [line.replace(" ", ".") for line in normalized_lines]
lines = [[char for char in line][::-1] for line in lines]

operators = [char for char in lines.pop(-1) if char in "*+"]

df = pd.DataFrame(lines)

indexes = []
for col in df.columns:
    col_num = col
    column_values = df[col].tolist()
    if all([val == "." for val in column_values]):
        indexes.append(col_num)

slices = []
start = 0
for index in indexes:
    slices.append(df.iloc[:, start: index+1])
    start = index + 1
slices.append(df.iloc[:, start:])  # indexes just takes you to last op, need to manually add remaining slice

equation_data = []
for slice in slices:
    operator = operators.pop(0)
    equation_data.append({
        "slice": slice,
        "operator": operator
    })

equations = []
for equation_datum in equation_data:
    operator = equation_datum["operator"]
    slice = equation_datum["slice"]

    nums = []
    for col in slice.columns:
        col_values = [num for num in df[col].tolist() if num != "."]
        if col_values:  # end of slice is just col of dots
            nums.append("".join(col_values))

    equations.append(operator.join(nums))

answer = sum([eval(equation) for equation in equations])
print(answer)