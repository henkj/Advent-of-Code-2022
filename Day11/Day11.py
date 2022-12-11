class Monkey:
    def __init__(self, items, op, val, divTest, trueIndex, falseIndex):
        self.items = items
        self.op = op
        self.val = val
        self.divTest = divTest
        self.trueIndex = trueIndex
        self.falseIndex = falseIndex
        self.inspections = 0
        self.commonDivider = 3

    def doBusiness(self, monkeys):
        for i in range(len(self.items)):
            self.inspections += 1
            if self.val == "old":
                val = self.items[i]
            else:
                val = int(self.val)

            if self.op == "*":
                self.items[i] *= val
            else:
                self.items[i] += val
            
            if self.commonDivider == 3: # part1
                self.items[i] = self.items[i] // self.commonDivider
            else:                       #part2
                wholes = self.items[i] // self.commonDivider
                self.items[i] -= wholes * self.commonDivider

            if self.items[i] % self.divTest == 0:
                index = self.trueIndex
            else:
                index = self.falseIndex
            monkeys[index].items.append(self.items[i])
            
        self.items = []     
    
    def addCommonDivider(self, commonDivider):
        self.commonDivider = commonDivider

def readInput(lines, monkeys, setCommonDivider):
    commonDivider = 1
    i = 0
    while i < len(lines):
        items = lines[i+1][len("Starting items: "):].split(", ")
        items = list(map(int, items))
        op, val = lines[i+2][len("Operation: new = old "):].split()
        divTest = int(lines[i+3][len("Test: divisible by "):])
        commonDivider *= divTest
        trueIndex = int(lines[i+4][len("If true: throw to monkey "):])
        falseIndex = int(lines[i+5][len("If false: throw to monkey "):])
        monkeys.append(Monkey(items, op, val, divTest, trueIndex, falseIndex))
        i += 7
    if setCommonDivider: # Only in part 2
        for monkey in monkeys:
            monkey.addCommonDivider(commonDivider)

def processMonkeyBusiness(monkeys, rounds):
    for i in range(rounds):
        for monkey in monkeys:
            monkey.doBusiness(monkeys)

def findInspectionVal(monkeys):
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspections)
    inspections.sort()
    inspectionVal = inspections[-1]*inspections[-2]
    return inspectionVal

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        monkeys = []

        readInput(lines, monkeys, False)
        processMonkeyBusiness(monkeys, 20)
        inspectionVal = findInspectionVal(monkeys)

        print("part1: " + str(inspectionVal))

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        monkeys = []

        readInput(lines, monkeys, True)
        processMonkeyBusiness(monkeys, 10000)
        inspectionVal = findInspectionVal(monkeys)

        print("part2: " + str(inspectionVal))

part1('Day11/input/input.txt')
part2('Day11/input/testinput.txt')
