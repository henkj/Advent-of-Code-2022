import re

def findEndOfStacks(lines):
    for i, line in enumerate(lines):
        line = line.strip()
        if line[0].isnumeric():
            return i
    return None

def doAction(matrix, moves, src, dest):
    if moves == 0:
        return matrix
    matrix[dest].append(matrix[src].pop())
    return doAction(matrix, moves-1, src, dest)

def doAction2(matrix, moves, src, dest):
    temp = matrix[src][-moves:]
    matrix[src] = matrix[src][:-moves]
    for t in temp:
        matrix[dest].append(t)
    return matrix

def main(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.replace("]", " ") for s in [s.replace("[", " ") for s in lines]]

        maxSize = 15
        matrix = []
        matrix2 = []

        for i in range(maxSize):
            matrix.append([])
            matrix2.append([])

        index = findEndOfStacks(lines)
        stackInput = lines[:index]
        stackInput.reverse()

        for line in stackInput:
            for i, c in enumerate(line):
                if c.isalpha():
                    stacknr = int((i - 1)/4) 
                    matrix[stacknr].append(c)
                    matrix2[stacknr].append(c)
                
        actionLines = lines[index+2:]

        for line in actionLines:
            line = line.strip()
            moves, src, dest = re.findall(r'\d+', line)
            matrix = doAction(matrix, int(moves), int(src)-1, int(dest)-1)
            matrix2 = doAction2(matrix2, int(moves), int(src)-1, int(dest)-1)

    
        part1String = ""
        part2String = ""
        for i in range(maxSize):
            if len(matrix[i]) > 0:
                part1String += matrix[i].pop()
                part2String += matrix2[i].pop()
        
        print("part1: " + part1String)
        print("part2: " + part2String)


main('Day05/input/input.txt')

