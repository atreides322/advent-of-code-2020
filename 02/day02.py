#!/usr/bin/env python3

def main():
    with open('input.txt') as input:
        passwords = [ {"rule": rule, "password": password } for rule, password in
                        [ x.split(":") for x in input.readlines()]]

    valid_old = 0
    valid_new = 0

    for entry in passwords:
        password = entry['password'].strip()
        rule_parts = entry['rule'].split(' ')
        character = rule_parts[1]
        min, max = (int(x) for x in rule_parts[0].split('-',2))

        count = len([ x for x in password if x == character])

        if( count >= min and count <= max ):
            valid_old+=1

        pos1 = min - 1
        pos2 = max - 1

        if password[ pos1 ] != password[ pos2 ] and \
            ( password[ pos1 ] == character or password[ pos2 ] == character ):
            valid_new+=1

    print(f"Old Rule: {valid_old}")
    print(f"New Rule: {valid_new}")

if __name__ == "__main__":
    main()
