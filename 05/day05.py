#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    max_found = -1

    with open(sys.argv[1]) as input:
        for line in input:
            line = line.strip()
            id = decode(line)
            if id > max_found:
                max_found = id

    print(max_found)


def decode(line):
    row = bin_search(line[0:-3], 'F')
    column = bin_search(line[-3:], 'L')

    return row * 8 + column


def bin_search(directions, high):
    left = 0
    right = pow(2, len(directions)) - 1

    for character in directions:
        if character is high:
            right = int((right - left) / 2) + left
        else:
            left = right - int((right - left) / 2)

    return left


if __name__ == "__main__":
    main()
