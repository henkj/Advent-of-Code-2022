def findMarker(line, charList, size):
    for i, c in enumerate(line, 1):
        if c in charList:
            index = charList.index(c)
            charList = charList[index+1:]
        charList.append(c)
        if len(charList) == size:
            return i

def main(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        charList = []
        
        print("part1: " + str(findMarker(lines[0], charList, 4)))
        charList.clear()
        print("part2: " + str(findMarker(lines[0], charList, 14)))

main('Day06/input/input.txt')