import math
import uuid
from itertools import combinations

class Grid:
    def __init__(self):
        self.id = str(uuid.uuid4())[:4]
        self.circuits = []

    def add_circuit(self, c):
        self.circuits.append(c)

    def merge_circuits(self, c1, c2):
        for j in c2.junctions:
            j.circuit = c1
            c1.junctions.append(j)
        self.circuits.remove(c2)

class Circuit:
    def __init__(self, grid):
        self.id = str(uuid.uuid4())[:4]
        self.grid = grid
        self.junctions = []

class Junction:
    def __init__(self, x, y, z):
        self.coord = (int(x), int(y), int(z))
        self.circuit = None

    def dist(self, other):
        return math.dist(self.coord, other.coord)


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip().split(",") for line in f]

    junctions = [Junction(*xyz) for xyz in lines]
    grid = Grid()

    for j in junctions:
        c = Circuit(grid)
        c.junctions.append(j)
        j.circuit = c
        grid.add_circuit(c)

    edges = []
    for a, b in combinations(range(len(junctions)), 2):
        edges.append((junctions[a].dist(junctions[b]), a, b))

    edges.sort(key=lambda x: x[0])

    for i in range(1000):
        dist, a, b = edges[i]

        ja = junctions[a]
        jb = junctions[b]

        if ja.circuit is jb.circuit:
            continue

        c1 = ja.circuit
        c2 = jb.circuit

        if len(c1.junctions) < len(c2.junctions):
            c1, c2 = c2, c1

        grid.merge_circuits(c1, c2)

    sizes = sorted((len(c.junctions) for c in grid.circuits), reverse=True)
    print("Answer", sizes[0] * sizes[1] * sizes[2])


if __name__ == "__main__":
    main()
