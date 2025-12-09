import math
import uuid

class Grid:
    def __init__(self):
        self.id = str(uuid.uuid4())[:4]
        self.circuits = []

    def __repr__(self):
        return self.id

    def __len__(self):
        return len(self.circuits)

    def add_circuit(self, circuit: "Circuit"):
        self.circuits.append(circuit)

    def new_circuit(self, junction1: "Junction", junction2: "Junction"):
        circuit = Circuit(grid=self)
        circuit.add_junction(junction1)
        circuit.add_junction(junction2)
        self.circuits.append(circuit)
        return circuit

    def query_circuits(self, junction: "Junction"):
        for c in self.circuits:
            if c.query_junctions(junction):
                return c
        return None

class Circuit:
    def __init__(self, grid: "Grid"):
        self.id = str(uuid.uuid4())[:4]
        self.grid = grid
        self.junctions = []

    def __repr__(self):
        return self.id

    def __len__(self):
        return len(self.junctions)

    def add_junction(self, junction: "Junction"):
        self.junctions.append(junction)

    def query_junctions(self, junction: "Junction"):
        for j in self.junctions:
            if junction == j:
                return True
        return False

class Junction:
    def __init__(self, x, y, z):
        self.id = str(uuid.uuid4())[:4]
        self.coord = (int(x), int(y), int(z))
        self.connection = None
        self.connection_distance = None
        self.circuit = None
        self.grid = None

    def check_other_coordinate_distance(self, other: "Junction") -> float:
        return math.dist(self.coord, other.coord)

    def set_connection(self, other: "Junction", connection_distance: float, circuit: "Circuit", grid: "Grid"):
        self.connection = other
        self.connection_distance = connection_distance
        self.circuit = circuit
        self.grid = grid

    def __eq__(self, other):
        return self.coord == other.coord

    def __repr__(self):
        return f"Junction(ID: {self.coord}, CXN: {self.id})"

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]
    junctions = [Junction(*line.split(",")) for line in lines]

    grid = Grid()

    for junction in junctions:
        print(f"Looking at Junction: {junction.coord}.")
        if not junction.connection:
            print(f"Junction {junction.coord} has no connection.")
            distances = [junction.check_other_coordinate_distance(j) for j in junctions if j != junction]
            shortest_dist: float = min(distances)
            shortest_dist_index: int = distances.index(shortest_dist) + 1
            closest_junc: Junction = junctions[shortest_dist_index]
            print(f"The closest junction to {junction.coord} is {closest_junc.coord}.")

            if closest_junc.circuit:
                print(f"Closest Junction {closest_junc.coord} is already connected on circuit {closest_junc.circuit}. Adding Junction to Closest Junction circuit.")
                junction.set_connection(other=closest_junc, connection_distance=shortest_dist, circuit=closest_junc.circuit, grid=grid)
                closest_junc.circuit.add_junction(junction)
            else:
                print(f"Closest Junction {closest_junc.id} has no connected circuit, building new circuit and joining junctions.")
                circuit = grid.new_circuit(junction, closest_junc)
                junction.set_connection(other=closest_junc, connection_distance=shortest_dist, circuit=circuit, grid=grid)
                closest_junc.set_connection(other=junction, connection_distance=shortest_dist, circuit=circuit, grid=grid)
        else:
            print(f"Junction: {junction.coord} is already connected.")

    return grid


if __name__ == "__main__":
    g = main()
    #note






