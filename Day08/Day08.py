
def checkVisible(treeLine):
    indexList = []
    currentTop = -1
    for index in range(len(treeLine)):
        if int(treeLine[index]) > currentTop:
            indexList.append(index)
            currentTop = int(treeLine[index])
        if currentTop == 9:
            break
    return indexList

def setTreeVisibilityRow(treeVisibility, row, indexes, reverse):
    for index in indexes:
        if reverse:
            treeVisibility[row][-index-1] = True
        else:
            treeVisibility[row][index] = True

def setTreeVisibilityCol(treeVisibility, col, indexes, reverse):
    for index in indexes:
        if reverse:
            treeVisibility[-index-1][col] = True
        else:
            treeVisibility[index][col] = True

def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        # Setup bool matrix
        treesVisible = []
        for i in range(len(lines)):
            treesVisible.append([])
            for j in range(len(lines[0])):
                treesVisible[i].append(False)

        for i, treeLine in enumerate(lines):
            indexList = checkVisible(treeLine)
            indexList2 = checkVisible(treeLine[::-1])
            setTreeVisibilityRow(treesVisible, i, indexList, False)
            setTreeVisibilityRow(treesVisible, i, indexList2, True)

        for i in range(len(lines[0])):  
            col = [line[i] for line in lines]
            indexList = checkVisible(col)
            indexList2 = checkVisible(col[::-1])
            setTreeVisibilityCol(treesVisible, i, indexList, False)
            setTreeVisibilityCol(treesVisible, i, indexList2, True)

        visibleTreeCount = 0
        for treeLine in treesVisible:
            for treeVisible in treeLine:
                if treeVisible:
                    visibleTreeCount += 1
        print("part1: " + str(visibleTreeCount))

def findScore(treeLines, row, col):
    height = int(treeLines[row][col])
    # Rows
    cur = row - 1
    while cur > 0 and int(treeLines[cur][col]) < height:
        cur -= 1
    a = row - max(0,cur) 
    cur = row + 1
    while cur < len(treeLines)-1 and int(treeLines[cur][col]) < height:
        cur += 1
    b = min(cur, len(treeLines)-1) - row 

    # Columns
    cur = col - 1
    while cur > 0 and int(treeLines[row][cur]) < height:
        cur -= 1
    c = col - max(0,cur)
    cur = col + 1
    while cur < len(treeLines[0])-1 and int(treeLines[row][cur]) < height:
        cur += 1
    d = min(cur, len(treeLines[0])-1) - col
    return a*b*c*d

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        # Setup score matrix
        treeScores = []
        for i in range(len(lines)):
            treeScores.append([])
            for j in range(len(lines[0])):
                treeScores[i].append(0)

        # Calc scores
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                treeScores[i][j] = findScore(lines, i, j)
        
        # Find highest
        highScore = -1
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if treeScores[i][j] > highScore:
                    highScore = treeScores[i][j]
       
        print("part2: " + str(highScore))

part1('Day08/input/input.txt')
part2('Day08/input/input.txt')