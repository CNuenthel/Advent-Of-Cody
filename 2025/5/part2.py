
def merge_range(ranges: list, target_range: tuple):
    """
    Takes a range, and continuously merges ranges in a list if those ranges overlap with target range. Once
    an overlap is not detected, returns the merged range, and the remaining ranges for follow-up merging. Ranges
    must be sorted by range[0]
    """
    while True:
        if not ranges:
            break
        ingredient_range = ranges.pop(0)
        if (target_range[0] <= ingredient_range[0] <= target_range[1]
                or target_range[0] <= ingredient_range[1] <= target_range[1]
                or ingredient_range[0] <= target_range[0] <= ingredient_range[1]
                or ingredient_range[0] <= target_range[1] <= ingredient_range[1]):
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

    merged_ranges = []
    while ranges:
        t = ranges.pop(0)
        if not ranges:
            merged_ranges.append(t)
            break
        mr, ranges = merge_range(ranges, t)
        merged_ranges.append(mr)

    fresh_ingredients = sum([r[1] - r[0] + 1 for r in merged_ranges])
    print(f"Fresh Ingredients: {fresh_ingredients}")

if __name__ == "__main__":
    main()