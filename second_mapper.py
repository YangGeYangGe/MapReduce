#!/usr/bin/python3

import sys


def second_mapper():
    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) != 3:
            continue

        print("{}\t{}\t{}".format(parts[0],parts[1], parts[2]))


if __name__ == "__main__":
    second_mapper()
