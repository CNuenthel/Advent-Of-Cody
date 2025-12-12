import itertools


def press_buttons(panel_len: int, buttons: tuple) -> list:
    panel = ["." for i in range(panel_len)]
    for button in buttons:
        btn_ind = [int(num) for num in button if num.isdigit()]
        for num in btn_ind:
            panel[int(num)] = "#" if panel[int(num)] == "." else "."
    return panel

def solve(line: str):
    line_items = line.split(" ")
    panel = [char for char in line_items.pop(0)[1:-1]]
    _ = line_items.pop(-1)
    buttons = line_items

    for k in range(1, 10):  # pick sizes 1 through 6
        perms = list(itertools.permutations(buttons, k))

        for perm in perms:
            panel_result = press_buttons(len(panel), perm)
            if panel_result == panel:
                return k
    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    results = [solve(line) for line in [line.replace("\n", "") for line in lines]]
    print(results)
    print(sum(results))
