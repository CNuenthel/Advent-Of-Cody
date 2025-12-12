import itertools


def press_buttons(panel_len: int, buttons: tuple) -> list:
    panel = [0 for i in range(panel_len)]
    for button in buttons:
        btn_ind = [int(num) for num in button if num.isdigit()]
        for num in btn_ind:
            panel[int(num)] += 1
    return panel

def solve(line: str):
    line_items = line.split(" ")
    _ = line_items.pop(0)
    panel = [int(num.strip()) for num in line_items.pop(-1)[1:-1].split(",")]
    buttons = line_items

    panel_result = []
    k = 0
    while panel != panel_result:
        perms = list(itertools.permutations(buttons, k))
        for perm in perms:
            panel_result = press_buttons(len(panel), perm)
            if panel_result == panel:
                return k
        k += 1

    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    results = [solve(line) for line in [line.replace("\n", "") for line in lines]]
    print(results)
    print(sum(results))
