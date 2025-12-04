
class MatrixMapper:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.neighbor_map = {}

    def find_neighbors(self, y: int, x: int):
        if self.matrix[y][x] != "@":
            return
        neighbors = 0
        for coord in [
            (y,x-1), (y,x+1), (y-1,x), (y+1,x),
            (y-1,x+1), (y+1,x+1), (y-1,x-1), (y+1,x-1)
        ]:
            if coord[0] < 0 or coord[1] < 0:
                continue
            try:
                if self.matrix[coord[0]][coord[1]] == "@":
                    neighbors += 1
            except IndexError:
                continue
        self.neighbor_map[(y,x)] = neighbors

    def get_accessible_rolls(self):
        return sum([1 for val in self.neighbor_map.values() if val < 4])

    def map_neighbors(self):
        for row_i in range(0, len(self.matrix)):
            for col_i in range(0, len(self.matrix[row_i])):
                self.find_neighbors(row_i, col_i)

    def remove_accessible_rolls(self):
        total_removed = 0
        for coord, neigh_ct in self.neighbor_map.items():
            if neigh_ct < 4:
                self.matrix[coord[0]][coord[1]] = "."
                total_removed += 1
        self.neighbor_map = {}
        print(f"Removed {total_removed} Rolls")
        return total_removed

def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    matrix = [[char for char in row.replace("\n", "")] for row in data]
    mapper = MatrixMapper(matrix)

    total_removed = 0
    rolls = 1
    while rolls > 0:
        mapper.map_neighbors()
        rolls = mapper.remove_accessible_rolls()
        total_removed += rolls

    print(f"Total Rolls Removed: {total_removed}")

if __name__ == "__main__":
    main()