#!/usr/bin/env python3

def main():
    with open('input.txt') as input:
        passwords = [ {"rule": rule, "password": password } for rule, password in
                        [ x.split(":") for x in input.readlines()]]

    valid = 0
    for entry in passwords:
        rule_parts = entry['rule'].split(' ')
        character = rule_parts[1]
        min, max = (int(x) for x in rule_parts[0].split('-',2))

        count = len([ x for x in entry['password'] if x == character])

        if( count >= min and count <= max ):
            valid+=1

    print(valid)

if __name__ == "__main__":
    main()
