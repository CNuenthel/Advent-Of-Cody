class Tile:
    def __init__(self, x, y, tile_color = None):
        self.x = int(x)
        self.y = int(y)
        self.tile_color = tile_color

    def __repr__(self):
        return self.tile_color

    def find_area(self, other: "Tile"):
        return abs(self.x + 1 - other.x) * abs(self.y + 1 - other.y)

    def set_type(self, tile_color: str):
        self.tile_color = tile_color
        return self

    def reduce_cord(self, red_x: int, red_y: int):
        self.x -= red_x
        self.y -= red_y
        return self

    def return_bounds(self, other: "Tile") -> tuple:
        return (self.x, self.y), (other.x, self.y), (other.x, other.y), (self.x, other.y)


def build_tile_map(tiles: list) -> list:
    print("[+] Building Tile Map")
    max_x = max([tile.x+1 for tile in tiles])
    max_y = max([tile.y+1 for tile in tiles])
    tile_map = [[Tile(j, i, ".") for j in range(max_x)] for i in range(max_y)]
    for i in range(0, len(tiles)):
        if i == len(tiles) - 1:
            tile1 = tiles[i]
            tile2 = tiles[0]
        else:
            tile1 = tiles[i]
            tile2 = tiles[i+1]
        tile_map[tile1.y][tile1.x] = tile1
        traversal_x = tile1.x - tile2.x
        traversal_y = tile1.y - tile2.y
        x_operator = "-" if traversal_x < 0 else "+"
        y_operator = "-" if traversal_y < 0 else "+"
        for j in range(1, abs(traversal_x)):
            green_tile_x_index = tile1.x + j if x_operator == "-" else tile1.x - j
            tile_map[tile1.y][green_tile_x_index].set_type("G")
        for j in range(1, abs(traversal_y)):
            green_tile_y_index = tile1.y + j if y_operator == "-" else tile1.y - j
            tile_map[green_tile_y_index][tile1.x].set_type("G")
    return tile_map

def compress_tiles(tiles: list) -> list:
    print("[+] Compressing Tiles")
    min_x = min([tile.x for tile in tiles])
    min_y = min([tile.y for tile in tiles])
    return [tile.reduce_cord(min_x, min_y) for tile in tiles]

def verify_rectangle(tile_map_slice: list) -> bool:
    print("[!] Valid Rectangle Found!")
    for row in tile_map_slice:
        if any(slice_tile.tile_color not in "%RG" for slice_tile in row):
            return False
    return True

def draw_and_measure_rectangles(tiles: list[Tile]):
    print("[+] Drawing Rectangles")
    tile_map = build_tile_map(tiles)

    for i, row in enumerate(tile_map):  # fill
        if any(tile.tile_color in "RG" for tile in row):
            row_tile_group = [t for t in row if t.tile_color in "RG"]
            start_tile = row.index(row_tile_group[0])
            end_tile = row.index(row_tile_group[-1])
            for j in range(start_tile + 1, end_tile):
                tile = tile_map[i][j]
                if tile.tile_color in "RG":
                    continue
                else:
                    tile.set_type("%")

    print("[+] Checking Slices")
    max_area = 0
    for tile in tiles:
        for t in tiles:
            if t == tile:
                continue

            tile_map_slice = [
                row[tile.x: t.x + 1]
                for row in tile_map[tile.y: t.y + 1]
            ]

            if not tile_map_slice:
                continue

            area = len(tile_map_slice[0]) * len(tile_map_slice)

            if area < max_area:
                continue

            valid_rectangle = verify_rectangle(tile_map_slice)

            if valid_rectangle:
                max_area = area

    return max_area


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    tiles = [Tile(*line.replace("\n", "").split(",")).set_type("R") for line in lines]
    compressed_tiles = compress_tiles(tiles)
    result = draw_and_measure_rectangles(compressed_tiles)
    print(f"[&] Largest Area: {result}")




if __name__ == "__main__":
    main()