
class RedTile:
    def __init__(self, x: str, y: str):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"RTile({self.x}, {self.y})"

    def find_area(self, other_rt: "RedTile"):
        return abs(self.x + 1 - other_rt.x) * abs(self.y + 1 - other_rt.y)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    tiles = [RedTile(*line.replace("\n", "").split(",")) for line in lines]

    max_dist_tiles = []
    max_area = 0

    for tile in tiles:
        for t in tiles:
            if tile == t:
                continue
            else:
                area = tile.find_area(t)
                if area > max_area:
                    max_dist_tiles = [tile, t]
                    max_area = area

    print(max_dist_tiles)
    print(max_area)

if __name__ == "__main__":
    main()