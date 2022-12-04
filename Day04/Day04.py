import re

def main(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        contains = overlaps = 0

        for line in lines:
            a1, a2, b1, b2 = map(int, re.split("-|,", line))
            if (b1 >= a1 and b2 <= a2) or (a1 >= b1 and a2 <= b2):
                contains += 1
            if a1 <= b2 and a2 >= b1:
                overlaps += 1
        print("part1: " + str(contains))
        print("part2: " + str(overlaps))

main('Day04/input/input.txt')

