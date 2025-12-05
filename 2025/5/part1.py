
def check_freshness(ranges: list, ingredient: int) -> bool:
    for range_set in ranges:
        if ingredient < range_set[0] or ingredient > range_set[1]:
            continue
        else:
            if range_set[0] <= ingredient <= range_set[1]:
                print(f"Ingredient {ingredient} was found in the range {range_set[0]} to {range_set[1]}. Fresh.")
                return True
    return False

def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    data = [item.replace("\n", "") for item in data]

    split_index = data.index("")
    ranges, ingredients = data[:split_index], data[split_index+1:]

    ranges = [(int(num.split("-")[0]), int(num.split("-")[1])) for num in ranges]
    ingredients = [int(num) for num in ingredients]

    fresh_ingredients = []
    for ingredient in ingredients:
        if check_freshness(ranges, ingredient):
            fresh_ingredients.append(ingredient)

    print(f"Fresh Ingredients: {len(fresh_ingredients)}")


if __name__ == "__main__":
    main()