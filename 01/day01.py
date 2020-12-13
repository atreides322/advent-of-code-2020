#!/usr/bin/env python3

from functools import reduce

def main():
    with open('input.txt') as input:
        numbers = [ int(x) for x in input.readlines()]

    print_answer( find(numbers, 2020, 2) )
    print_answer( find(numbers, 2020, 3) )

def find(numbers, target, factors):
    for number in numbers:
        find_number = target - number

        if factors == 2:
            if find_number in numbers:
                return [number, find_number]

        else:
            result = find(numbers, find_number, factors - 1)
            if result:
                return [number] + result

def print_answer( solution ):
    print( " + ".join(str(x) for x in solution), "=", sum(solution) )
    print( " * ".join(str(x) for x in solution), "=", reduce((lambda x, y: x * y), solution ) )

if __name__ == "__main__":
    main()
