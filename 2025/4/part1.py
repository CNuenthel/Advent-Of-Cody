from numpy.ma.extras import row_stack


class MatrixMapper:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.neighbor_map = {}

    def get_accessible_rolls(self):
        return sum([1 for val in self.neighbor_map.values() if val < 4])

    def find_neighbors(self, row: int, col: int):
        if self.matrix[row][col] != "@":
            return

        y = row
        x = col
        left_neighbor = (y, x - 1)
        right_neighbor = (y, x + 1)
        up_neighbor = (y - 1, x)
        down_neighbor = (y + 1, x)
        ne_neighbor = (y - 1, x + 1)
        se_neighbor = (y + 1, x + 1)
        nw_neighbor = (y - 1, x - 1)
        sw_neighbor = (y + 1, x - 1)

        neighbors = 0
        for coord in [
            left_neighbor, right_neighbor, up_neighbor, down_neighbor,
            ne_neighbor, se_neighbor, nw_neighbor, sw_neighbor
        ]:
            if coord[0] < 0 or coord[1] < 0:
                continue

            try:
                if self.matrix[coord[0]][coord[1]] == "@":
                    neighbors += 1
            except IndexError:
                continue

        self.neighbor_map[(row, col)] = neighbors


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    matrix = [[char for char in row.replace("\n", "")] for row in data]
    mapper = MatrixMapper(matrix)

    for row_i in range(0, len(matrix)):
        for col_i in range(0, len(matrix[row_i])):
            mapper.find_neighbors(row_i, col_i)

    print(f"Accessible Rolls: {mapper.get_accessible_rolls()}")


if __name__ == "__main__":
    main()