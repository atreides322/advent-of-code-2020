#!/usr/bin/env python3

import sys

# cid "optional"
required = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def main():

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} input_file")

    valid = 0
    data = {}

    with open(sys.argv[1]) as input:
        for line in input:
            line = line.strip()
            if len(line) == 0:
                if validate(data):
                    valid += 1

                data = {}
            else:
                fields = { key: value for key, value in [part.split(':') for part in line.split(' ')]}
                data = {**data, **fields}
        if validate(data):
            valid += 1

    print(valid)

def validate(data):
    keys = [ key for key in sorted(data.keys()) if key != 'cid']
    return keys == required

if __name__ == "__main__":
    main()
