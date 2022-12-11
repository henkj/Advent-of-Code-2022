class Monkey:
    def __init__(self, monkeyIndex, items, op, val, divTest, trueIndex, falseIndex):
        self.monkeyIndex = monkeyIndex
        self.items = items
        self.op = op
        self.val = val
        self.divTest = divTest
        self.trueIndex = trueIndex
        self.falseIndex = falseIndex
        self.inspections = 0

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
            
            newItem = self.items[i] // 3
            if newItem % self.divTest == 0:
                index = self.trueIndex
            else:
                index = self.falseIndex
            monkeys[index].items.append(newItem)
        self.items = []     

class Monkey2:
    def __init__(self, monkeyIndex, items, op, val, divTest, trueIndex, falseIndex):
        self.monkeyIndex = monkeyIndex
        self.items = items
        self.op = op
        self.val = val
        self.divTest = divTest
        self.trueIndex = trueIndex
        self.falseIndex = falseIndex
        self.inspections = 0

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
            
            #wholes = self.items[i] // (23*19*13*17)
            #self.items[i] -= wholes * self.divTest
            if self.items[i] % self.divTest == 0:
                index = self.trueIndex
            else:
                index = self.falseIndex
            monkeys[index].addItem(self.items[i])
            
        self.items = []     
    
    def addItem(self, item):
        #wholes = item // (23*19*13*17)
        #item -= wholes * (23*19*13*17)
        wholes = item // (11*3*5*7*19*2*13*17)
        item -= wholes * (11*3*5*7*19*2*13*17)

        self.items.append(item)

def readInput(lines, monkeys):
    i = 0
    while i < len(lines):
        monkeyIndex = int(lines[i].split()[1].strip(":"))
        items = lines[i+1][len("Starting items: "):].split(", ")
        items = list(map(int, items))
        op, val = lines[i+2][len("Operation: new = old "):].split()
        divTest = int(lines[i+3][len("Test: divisible by "):])
        trueIndex = int(lines[i+4][len("If true: throw to monkey "):])
        falseIndex = int(lines[i+5][len("If false: throw to monkey "):])
        monkeys.append(Monkey(monkeyIndex, items, op, val, divTest, trueIndex, falseIndex))
        i += 7

def readInput2(lines, monkeys):
    i = 0
    while i < len(lines):
        monkeyIndex = int(lines[i].split()[1].strip(":"))
        items = lines[i+1][len("Starting items: "):].split(", ")
        items = list(map(int, items))
        op, val = lines[i+2][len("Operation: new = old "):].split()
        divTest = int(lines[i+3][len("Test: divisible by "):])
        trueIndex = int(lines[i+4][len("If true: throw to monkey "):])
        falseIndex = int(lines[i+5][len("If false: throw to monkey "):])
        monkeys.append(Monkey2(monkeyIndex, items, op, val, divTest, trueIndex, falseIndex))
        i += 7

def processMonkeyBusiness(monkeys, rounds):
    for i in range(rounds):
        for monkey in monkeys:
            monkey.doBusiness(monkeys)
        if i in (1, 20) or (i+1) % 1000 == 0:
            print("== After round " + str(i+1) + " ==")
            print("Monkey 0 inspected items " + str(monkeys[0].inspections) + " times.")
            print("Monkey 1 inspected items " + str(monkeys[1].inspections) + " times.")
            print("Monkey 2 inspected items " + str(monkeys[2].inspections) + " times.")
            print("Monkey 3 inspected items " + str(monkeys[3].inspections) + " times.")

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

        readInput(lines, monkeys)
        processMonkeyBusiness(monkeys, 10000)
        inspectionVal = findInspectionVal(monkeys)

        print("part1: " + str(inspectionVal))

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        monkeys = []

        readInput2(lines, monkeys)
        processMonkeyBusiness(monkeys, 10000)
        inspectionVal = findInspectionVal(monkeys)

        print("part2: " + str(inspectionVal))





#part1('Day11/input/input.txt')
part2('Day11/input/input.txt')
