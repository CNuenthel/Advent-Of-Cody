import math
import uuid

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.replace("\n", "") for line in lines]

class Coordinate:
    def __init__(self, x, y, z):
        self.coord = (int(x),int(y),int(z))
        self.connection = None
        self.connection_distance = None
        self.circuit_id = None

    def check_other_coordinate_distance(self, other: "Coordinate"):
        return math.dist(self.coord, other.coord)

    def set_connection(self, other: "Coordinate"):
        if not other.circuit_id and not self.circuit_id:
            self.circuit_id = uuid.uuid4()

        self.circuit_id = connection_id

    def __eq__(self, other):
        return self.coord == other.coord

    def __repr__(self):
        return str(self.coord)

points = [Coordinate(*line.split(",")) for line in lines]

for point in points:
    for p in points:
        if p == point:
            continue

        shortest_coord = p
        shortest_dist = 999999999

        dist = point.check_other_coordinate_distance(p)
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_coord = p

    point.set_connection








