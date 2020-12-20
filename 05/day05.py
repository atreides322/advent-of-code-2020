#!/usr/bin/env python3

import sys

found = []


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

            found.append(id)

    print("Max: ", max_found)
    print("My Seet ID: ", find_missing())


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


def find_missing():
    found_sorted = sorted(found)

    previous = found_sorted[0]
    for current in found_sorted[1:]:
        if current - previous > 1:
            return current - 1
        previous = current


if __name__ == "__main__":
    main()
