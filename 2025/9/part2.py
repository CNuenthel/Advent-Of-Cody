"""
KEYWORD FOR SOLUTION:
COORDINATE COMPRESSION

This challenge was $%!!@#$ hard.
Study:
    Coordinate Compression
    Flood Fill
    Prefix Sum
"""
from collections import deque

points = [list(map(int, line.split(","))) for line in open("input.txt")]

xs = sorted({x for x, _ in points})
ys = sorted({y for _, y in points})

""" 
I'm pulling from the entire list of points, sorting them and creating a deduplicated list
of X coordinates (rows) and Y coordinates (columns)

Why this matters:
Instead of worrying about all useless points between our red tiles, I am recording each
specific row/column where a red tile, or corner, exists. Those rows/columns are retained 
with a value of 1, while all internal rows/columns are compressed and their compression value
is stored. 

A column where a # is at index 0, and the next # is at index 5 would look like this:
[ #=1, .=5, #=1]
"""
# print(xs)
# print(" ")
#
# print(ys)
# print(" ")

"""
Build base compressed grid, a row for each x, a column for each y, and a row for each
compressed space between x and a column for each compressed spaced between y


2d grid example: 
indexes: [0   1   2   3   4  5   6 ]
grid:    [2  gap  7  gap  9 gap  11] or [point gap point gap point gap point]

so when we do len(ys) * 2 - 1, we are saying we need a point for each Y (or x) and a point for
each space between.
"""
grid = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]

"""
We need all pairs of points, here I'm just iterating over the points including the last
paired with the first.
"""
for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
    # For each point, get the compressed index
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])

    """
    print(x1, y1, x2, y2, cx1, cy1, cx2, cy2)

    Remember from the sample input, our X order is 2 -> 7 -> 9 -> 11 (always remember)
    2 is at compressed index 0 (keep in mind we cannot compress our red tiles, it must be 1)
    compressed index 1 is the space between 2 and 7 (this is 4, non-inclusive)
    7 is at compressed index 1 (yada, yada)

    7 1 11 1 2 0 6 0     7,1 is first point, 11,1 is second point
    11 1 11 7 6 0 6 6    
    11 7 9 7 4 6 6 6
    9 7 9 5 4 4 4 6
    9 5 2 5 0 4 4 4
    2 5 2 3 0 2 0 4
    2 3 7 3 0 2 2 2
    7 3 7 1 2 0 2 2
    """

    # Modify the grid to show 1 for each uncompressed red tile point
    for cx in range(cx1, cx2 + 1):
        for cy in range(cy1, cy2 + 1):
            grid[cx][cy] = 1
    # We now have a grid (grid) displaying the polygon formed by our input points

# for row in grid:
#     print(*row)
# print("")

"""
Run a flood fill on the outside to identify all the coords on the outside,
this allows me to determine if any rectangle coord is found outside the polygon

1. Fill in the shape of the polygon
2. Loop through each pair of red tiles, for each rectangle containing only r/g tiles record area if max
"""
outside = {(-1, -1)}  # start from a position outside the grid
queue = deque(outside)

""" [1] """
while len(queue) > 0:  # queue currently initially has one item, (-1, -1)
    tx, ty = queue.popleft()

    """ 
    For each cell, try to move up, down, left, right
    Skip out of bounds cells (lt 0, gt len(row), gt len(grid[0]))
    Skip cells where the char is already 1
    Skip cells that were already visited

    the point is either outside our polygon, a wall piece, or inside. If it is inside
    we add that point to the queue and do the same on that point until finished.
    """
    for nx, ny in [(tx - 1, ty), (tx + 1, ty), (tx, ty - 1), (tx, ty + 1)]:
        if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid[0]):  # outside the grid including the buffer
            continue
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:  # the wall is already 1
            continue
        if (nx, ny) in outside: continue  # already seen
        outside.add((nx, ny))
        queue.append((nx, ny))

"""
For all the points in our compressed grid, if it is not an outside point, change the value to 1
to indicate it is a green fill tile
"""
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x, y) not in outside:
            grid[x][y] = 1

# for row in grid:
#     print(*row)
# print(" ")


""" [2] """
"""
We need to repeatedly determine the sum of all values in a rectangle without loops.

Prefix Summary Data Structure

Take a list:
[ 1 5 2 3 ]

Create a new list that stores a sum of values up to a point
[ 1 6 8 11 ] or [ 1, 5+1=6, 2+6=8, 3+8=11 ]

[ 1 5 2 3 ] 
    ^ ^ The sum of range between ls[1] to ls[2] 

take sum of all elements before the last in the list then subtract
the sum of items in the list just before the start of the range

so the range from ls[1] to ls[2] here is 8-1 (from prefix summary list) or 7, 
which if we look at our origin list:
    [ 1 5 2 3 ], the sum (ls[1]+ls[2]) is indeed 7

Same for say this range:
[ 1 5 2 3 ]             V here V here
    ^   ^  (this is [ 1 |6 8 11| ] which would be 11 - 1, or 10
                      ^ sub   ^ from this

            5+2+3 == 10 is True. Sick. 
"""
psa = [[0] * len(row) for row in grid]
for x in range(len(psa)):
    for y in range(len(psa[0])):
        left = psa[x - 1][y] if x > 0 else 0
        top = psa[x][y - 1] if y > 0 else 0
        topleft = psa[x - 1][y - 1] if x > 0 < y else 0
        psa[x][y] = left + top - topleft + grid[x][y]


def valid(x1, y1, x2, y2):
    cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
    cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
    left = psa[cx1 - 1][cy2] if cx1 > 0 else 0
    top = psa[cx2][cy1 - 1] if cy1 > 0 else 0
    topleft = psa[cx1 - 1][cy1 - 1] if cx1 > 0 < cy1 else 0
    count = psa[cx2][cy2] - left - top + topleft
    return count == (cx2 - cx1 + 1) * (cy2 - cy1 + 1)


# print("Valid Rectangles\nInvalid Rectangles")
# print([(x1,y1,x2,y2) for i, (x1, y1) in enumerate(points) for x2, y2 in points[:i] if valid(x1, y1, x2, y2)])
# print([(x1,y1,x2,y2) for i, (x1, y1) in enumerate(points) for x2, y2 in points[:i] if not valid(x1, y1, x2, y2)])

print(max([(abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) for i, (x1, y1) in enumerate(points) for x2, y2 in points[:i] if
           valid(x1, y1, x2, y2)]))