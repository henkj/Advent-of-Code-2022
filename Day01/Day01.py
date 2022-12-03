def getCals(calList, amount):
    sums = sorted([sum(s) for s in calList])
    return sum(sums[-amount:])

def part(input):
    with open(input) as f:
        lines = f.readlines()
        l = [x.split(' ') for x in ' '.join([x.strip() for x in lines]).split('  ')]
        calories = [[int(s) for s in x] for x in l]

        print("part1: " + str(getCals(calories, 1)))
        print("part2: " + str(getCals(calories, 3)))


part('Day01/input/input.txt')