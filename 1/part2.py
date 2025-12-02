import time

class SafeCracker:
    def __init__(self):
        self.pos = 50
        self.pass_count = 0

    def rotate(self, val):
        if "R" in val:
            val = int(val.replace("R", ""))
            for i in range(val):
                self.pos += 1
                self.pos = self.pos % 100
                if self.pos == 0:
                    self.pass_count += 1

        elif "L" in val:
            val = int(val.replace("L", ""))

            for i in range(val):
                self.pos -= 1
                self.pos = self.pos % 100
                if self.pos == 0:
                    self.pass_count += 1

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    inputs = [line.replace("\n", "") for line in lines]
    cracker = SafeCracker()
    for input in inputs:
        cracker.rotate(input)
    print(cracker.pass_count)

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Completed in {end - start:.6f} seconds")


