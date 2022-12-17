def add(aSet, value):
    if value not in aSet:
        aSet.add(value)


def processSandPt1(stones, maxDepth):
    x = 500
    y = 0

    while True:
        if y > maxDepth:
            break
        if (x, y+1) not in stones:
            y += 1
        elif (x-1, y+1) not in stones:
            x -= 1
            y += 1
        elif (x+1, y+1) not in stones:
            x += 1
            y += 1
        elif (x, y+1) in stones and (x-1, y+1) in stones and (x+1, y+1) in stones:
            stones.add((x, y))
            x = 500
            y = 0


def processSandPt2(stones, maxDepth):
    x = 500
    y = 0

    while True:
        if y == maxDepth:
            stones.add((x, y))
            x = 500
            y = 0

        if (x, y+1) not in stones:
            y += 1
        elif (x-1, y+1) not in stones:
            x -= 1
            y += 1
        elif (x+1, y+1) not in stones:
            x += 1
            y += 1

        elif (x, y+1) in stones and (x-1, y+1) in stones and (x+1, y+1) in stones:
            stones.add((x, y))
            if x == 500 and y == 0:
                return
            x = 500
            y = 0


def parseStones(lines):
    stones = set()
    for line in lines:
        old = None
        asd = line.split(" -> ")
        for val in asd:
            val = eval(val)
            val = (int(val[0]), int(val[1]))
            if old == None:
                stones.add(val)
            else:
                valX = int(val[0])
                valY = int(val[1])
                if old[0] > valX:
                    for i in range(old[0] - valX):
                        add(stones, (old[0]-(i+1), old[1]))
                elif old[0] < valX:
                    for i in range(valX - old[0]):
                        add(stones, (old[0]+(i+1), old[1]))
                elif old[1] > valY:
                    for i in range(old[1] - valY):
                        add(stones, (old[0], old[1]-(i+1)))
                elif old[1] < valY:
                    for i in range(valY - old[1]):
                        add(stones, (old[0], old[1]+(i+1)))
            old = val
    return stones


def main(input):

    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        # Part 1
        stones = parseStones(lines)
        stoneCount = len(stones)
        maxDepth = -1
        for stone in stones:
            maxDepth = max(maxDepth, stone[1])

        processSandPt1(stones, maxDepth)
        print("part1: " + str(len(stones) - stoneCount))

        # Part 2
        stones = parseStones(lines)
        maxDepth += 1
        processSandPt2(stones, maxDepth)
        print("part2: " + str(len(stones) - stoneCount))


main('Day14/input/input.txt')
