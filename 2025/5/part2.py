

def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    data = [item.replace("\n", "") for item in data]

    split_index = data.index("")
    ranges, ingredients = data[:split_index], data[split_index+1:]

    ranges = [(int(num.split("-")[0]), int(num.split("-")[1])) for num in ranges]
    ingredients = [int(num) for num in ingredients]



if __name__ == "__main__":
    main()