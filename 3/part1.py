



def determine_max_joltage(battery: str) -> int:
    battery_jolts = [int(char) for char in battery]
    max_joltage = 0
    for jolt in range(0, len(battery_jolts)):
        joltage = battery_jolts.pop(0)
        for j in battery_jolts:
            if int(str(joltage) + str(j)) > max_joltage:
                max_joltage = int(str(joltage)+str(j))
    return max_joltage

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = [row.replace("\n", "") for row in lines]

    joltages = []

    for line in lines:
        joltages.append(determine_max_joltage(line))

    print(joltages)
    print(sum(joltages))

if __name__ == "__main__":
    main()
