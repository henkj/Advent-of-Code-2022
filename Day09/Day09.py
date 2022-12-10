def updatePos(knotList, dir):
    # Update head
    if dir == "U":
        knotList[0] = (knotList[0][0], knotList[0][1]+1)
    if dir == "D":
        knotList[0] = (knotList[0][0], knotList[0][1]-1)
    if dir == "R":
        knotList[0] = (knotList[0][0]+1, knotList[0][1])
    if dir == "L":
        knotList[0] = (knotList[0][0]-1, knotList[0][1])

    # Update tail
    for i in range(1, len(knotList)):
        if abs(knotList[i][0]-knotList[i-1][0]) <= 1 and abs(knotList[i][1]-knotList[i-1][1]) <= 1: # touching
            continue
            
        if knotList[i-1][0] > knotList[i][0]:
            knotList[i] = (knotList[i][0]+1, knotList[i][1])
        elif knotList[i][0] > knotList[i-1][0]:
            knotList[i] = (knotList[i][0]-1, knotList[i][1])
        if knotList[i-1][1] > knotList[i][1]:
            knotList[i] = (knotList[i][0], knotList[i][1]+1)
        elif knotList[i][1] > knotList[i-1][1]:
            knotList[i] = (knotList[i][0], knotList[i][1]-1)
    return knotList

def tailVisits(input, knots):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        tailVisitedNodes = []
        knotList = []
        for i in range(knots):
            knotList.append((0,0))
        
        for line in lines:
            dir, length = line.split()
            for i in range(int(length)):
                knotList = updatePos(knotList, dir)
                if knotList[-1] not in tailVisitedNodes:
                    tailVisitedNodes.append(knotList[-1])
        
        return len(tailVisitedNodes)

print("part1: " + str(tailVisits('Day09/input/input.txt', 2)))
print("part2: " + str(tailVisits('Day09/input/input.txt', 10)))