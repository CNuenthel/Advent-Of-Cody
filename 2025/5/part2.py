
def merge_range(ranges: list, target_range: tuple):
    while True:
        if not ranges:
            break
        ingredient_range = ranges.pop(0)
        if target_range[0] <= ingredient_range[0] <= target_range[1] or target_range[0] <= ingredient_range[1] <= target_range[1]:
            target_range = (min(ingredient_range+target_range), max(ingredient_range+target_range))
        else:
            ranges.insert(0, ingredient_range)
            break

    return target_range, ranges

def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    data = [item.replace("\n", "") for item in data]
    split_index = data.index("")
    ranges, ingredients = data[:split_index], data[split_index + 1:]
    ranges = sorted([(int(num.split("-")[0]), int(num.split("-")[1])) for num in ranges])

    range_count = len(ranges)

    while True:
        merged_ranges = []

        while ranges:
            t = ranges.pop(0)

            if not ranges:
                merged_ranges.append(t)
                break

            mr, ranges = merge_range(ranges, t)
            merged_ranges.append(mr)

        ranges = merged_ranges

        if len(merged_ranges) == range_count:
            break
        else:
            range_count = len(merged_ranges)

    fresh_ingredients = sum([r[1] - r[0] + 1 for r in ranges])
    print(f"Fresh Ingredients: {fresh_ingredients}")

if __name__ == "__main__":
    main()