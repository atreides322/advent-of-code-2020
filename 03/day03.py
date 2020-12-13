#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    with open(sys.argv[1]) as input:
        topography = [ [char for char in line.strip()] for line in input.readlines()]

    dy = 1
    dx = 3

    max_x = len(topography[0])
    x = 0
    trees = 0
    for y in range(0, len(topography), dy):
        if topography[y][x] == '#':
            trees += 1

        x = (x + dx) % max_x

    print(trees)

if __name__ == "__main__":
    main()
