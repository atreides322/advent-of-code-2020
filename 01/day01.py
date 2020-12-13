#!/usr/bin/env python3

def main():
    with open('input.txt') as input:
        numbers = [ int(x) for x in input.readlines()]

    for number in numbers:
        find_number = 2020 - number

        if find_number in numbers:
            return number * find_number

if __name__ == "__main__":
    print(main())
