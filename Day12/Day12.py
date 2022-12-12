import sys

def findMinSteps(old, current, endNode, grid, distances, visited):
    if current[0] < 0 or current[0] > len(grid)-1:
        return sys.maxsize
    if current[1] < 0 or current[1] > len(grid[0])-1:
        return sys.maxsize
    if grid[current[0]][current[1]] > chr(ord(old)+1): # new charvalue max 1 higher than old charvalue
        return sys.maxsize
    if visited + 1 >= distances[current[0]][current[1]]:
        return sys.maxsize
    if current == endNode:
        return 0
    visited += 1
    distances[current[0]][current[1]] = visited
    a = findMinSteps(grid[current[0]][current[1]], (current[0]-1,current[1]), endNode, grid, distances, visited)
    b = findMinSteps(grid[current[0]][current[1]], (current[0]+1,current[1]), endNode, grid, distances, visited)
    c = findMinSteps(grid[current[0]][current[1]], (current[0],current[1]-1), endNode, grid, distances, visited)
    d = findMinSteps(grid[current[0]][current[1]], (current[0],current[1]+1), endNode, grid, distances, visited)
    return 1 + min(a, b, c, d)

def findLetters(grid, c):
    coords = []
    for row, line in enumerate(grid):
        for col, c2 in enumerate(line):
            if c == c2:
                coords.append((row,col))
    return coords

def main(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        grid = []
        distances = []
        visits = 0

        for i, line in enumerate(lines):
            grid.append([])
            distances.append([])
            for j, c in enumerate(line):
                grid[i].append(c)
                distances[i].append(sys.maxsize)

        start = findLetters(grid, 'S')[0]
        end = findLetters(grid, 'E')[0]

        grid[start[0]][start[1]] = 'a'
        grid[end[0]][end[1]] = 'z'

        minSteps = findMinSteps('a', start, end, grid, distances, visits)
        print("part1: " + str(minSteps))


        potentialStarts = findLetters(grid, 'a')
        for start in potentialStarts:
            visits = 0
            minSteps = min(findMinSteps('a', start, end, grid, distances, visits), minSteps)
        
        print("part2: " +  str(minSteps))

main('Day12/input/input.txt')