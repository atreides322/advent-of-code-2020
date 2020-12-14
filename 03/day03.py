#!/usr/bin/env python3

import sys
from functools import reduce

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        topography = [ [char for char in line.strip()] for line in input.readlines()]

    slopes = [(1,1), (1,3), (1,5), (1,7), (2, 1)]
    solution = [count_trees(topography, dy, dx) for dy, dx in slopes]

    print( solution, "=", reduce((lambda x, y: x * y), solution ) )

def count_trees(topography, dy, dx):
    max_x = len(topography[0])
    x = 0
    trees = 0
    for y in range(0, len(topography), dy):
        if topography[y][x] == '#':
            trees += 1

        x = (x + dx) % max_x

    return trees

if __name__ == "__main__":
    main()
