#!/usr/bin/env python3

import sys
import re

rules = {
    'byr': (lambda x: validate_num_range(x, 1920, 2002)),
    'iyr': (lambda x: validate_num_range(x, 2010, 2020)),
    'eyr': (lambda x: validate_num_range(x, 2020, 2030)),
    'hgt': (lambda x: validate_height(x)),
    'hcl': (lambda x: bool(re.fullmatch(r'#[0-9a-f]{6}', x))),
    'ecl': (lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': (lambda x: bool(re.fullmatch(r'\d{9}', x))),
    'cid': (lambda x: True)
}

# cid "optional"
required = [x for x in sorted(list(rules.keys())) if x != 'cid']

def validate_num_range( value, min, max):
    return value.isdigit() and int(value) >= min and int(value) <= max

def validate_height( height ):
    if height.endswith('cm'):
        return validate_num_range( height[0:-2], 150, 193)

    if height.endswith('in'):
        return validate_num_range( height[0:-2], 59, 76)

    return False

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

    return keys == required and all([ rules[key](value) for key, value in data.items() ])

if __name__ == "__main__":
    main()
