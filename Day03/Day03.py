def findCommonChar(a, b):
    for c in a:
        for c2 in b:
            if c == c2:
                return c
    return None

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        priorities = []

        for line in lines:
            index = int(len(line)/2)
            a = line[0:index]
            b = line[index:]
            c = findCommonChar(a, b)
            if c.isupper():
                priorities.append(ord(c)-38)
            else:
                priorities.append(ord(c)-96)
        print("part1: " + str(sum(priorities)))

def findCommonChar2(a, b, c):
    for c1 in a:
        for c2 in b:
            if c1 == c2:
                for c3 in c:
                    if c2 == c3:
                        return c3
    return None

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        i = 0
        priorities = []

        while i < len(lines):
            c = findCommonChar2(lines[i],lines[i+1],lines[i+2])
            if c.isupper():
                priorities.append(ord(c)-38)
            else:
                priorities.append(ord(c)-96)
            i += 3
        print("part2: " + str(sum(priorities)))

        


part1('Day03/input/input.txt')
part2('Day03/input/input.txt')