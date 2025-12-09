import math
import uuid
from itertools import combinations

class Grid:
    def __init__(self):
        self.id = str(uuid.uuid4())[:4]
        self.circuits = []  # list of Circuit

    def add_circuit(self, c: "Circuit"):
        self.circuits.append(c)

    def merge_circuits(self, c1: "Circuit", c2: "Circuit"):
        for j in c2.junctions:
            j.circuit = c1
            c1.junctions.append(j)
        self.circuits.remove(c2)


class Circuit:
    def __init__(self, grid: Grid):
        self.id = str(uuid.uuid4())[:4]
        self.grid = grid
        self.junctions = []

    def __len__(self):
        return len(self.junctions)

    def __repr__(self):
        return f"Circuit({self.id}, size={len(self.junctions)})"


class Junction:
    def __init__(self, x, y, z):
        self.coord = (int(x), int(y), int(z))
        self.circuit: Circuit | None = None

    def dist(self, other: "Junction") -> float:
        return math.dist(self.coord, other.coord)

    def __repr__(self):
        return f"J({self.coord})"


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip().split(",") for line in f if line.strip()]

    junctions = [Junction(*xyz) for xyz in lines]
    n = len(junctions)

    grid = Grid()
    for j in junctions:
        c = Circuit(grid)
        c.junctions.append(j)
        j.circuit = c
        grid.add_circuit(c)

    edges = []
    for a, b in combinations(range(n), 2):
        d = junctions[a].dist(junctions[b])
        edges.append((d, a, b))

    edges.sort(key=lambda x: x[0])
    last_merge_pair = None
    connection_count = 0

    for dist, a, b in edges:
        ja = junctions[a]
        jb = junctions[b]

        connection_count += 1

        if ja.circuit is not jb.circuit:
            c1 = ja.circuit
            c2 = jb.circuit

            if len(c1) < len(c2):
                c1, c2 = c2, c1

            grid.merge_circuits(c1, c2)
            last_merge_pair = (a, b)

        if len(grid.circuits) == 1:
            break

    a, b = last_merge_pair
    x1 = junctions[a].coord[0]
    x2 = junctions[b].coord[0]
    part2_answer = x1 * x2

    print(part2_answer)


if __name__ == "__main__":
    main()
