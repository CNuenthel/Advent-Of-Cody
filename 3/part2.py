

def extract_max_joltage(battery: str) -> int:
    ls_battery = [int(char) for char in battery]
    max_joltage = []

    i = -11
    while True:
        selectable_slice = ls_battery[0:i]

        if len(max_joltage) == 11:
            max_joltage.append(max(ls_battery))
            break
        elif not selectable_slice:
            max_joltage.extend(ls_battery)
            break

        num = max(selectable_slice)
        num_index = ls_battery.index(num)
        max_joltage.append(num)
        ls_battery = ls_battery[num_index + 1:]
        i += 1
    return int("".join([str(i) for i in max_joltage]))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()

    data = [line.replace("\n", "") for line in data]

    total = [extract_max_joltage(row) for row in data]
    print(total)
    print(sum(total))