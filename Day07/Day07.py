class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
        self.files = []

    def addParent(self, parent):
        self.parent = parent

    def addFolder(self, folder):
        sub = Directory(folder)
        sub.addParent(self)
        self.subdirectories.append(sub)

    def addFile(self, name, size):
        self.files.append(File(name, int(size)))

    def findSubDirectoryNamed(self, name):
        for dir in self.subdirectories:
            if name == dir.name:
                return dir
        return None
    
    def calcSize(self, list):
        mySize = 0
        for dir in self.subdirectories:
            mySize += dir.calcSize(list)
        for file in self.files:
            mySize += file.size
        list.append((self.name, mySize))
        return mySize


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def updateContent(currentDir, lines, i):
    while i < len(lines) and lines[i][0] != "$":
        if lines[i].startswith("dir"):
            currentDir.addFolder(lines[i].split()[1]) # Check if alrdy exist?
        else:
            size, name = lines[i].split()
            currentDir.addFile(name, size)
        i += 1
    return i

def navigateDirectory(currentDir, baseDir, dirName):
    if dirName == "/":
        return baseDir
    elif dirName == "..":
        return currentDir.parent
    else:
        return currentDir.findSubDirectoryNamed(dirName)
        

def main(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        dir = Directory("/")
        dir.addParent(dir)
        i = 1
        currentDir = dir
        baseDir = currentDir
        while i < len(lines):
            if lines[i] == "$ ls":
                i=updateContent(currentDir, lines, i+1)
            elif lines[i].startswith("$ cd"):
                currentDir = navigateDirectory(currentDir, baseDir, lines[i].split()[2])
                i += 1
        sizes = []
        baseDir.calcSize(sizes)     

        sum = 0
        for element in sizes:
            if element[1] <= 100000:
                sum += element[1] 

        print("part1: " + str(sum))

        minimumDeletion = sizes[-1][1] - 40000000
        smallestAcceptableSize = 0
        for element in sizes:
            if element[1] >= minimumDeletion:
                if element[1] < smallestAcceptableSize or smallestAcceptableSize == 0:
                    smallestAcceptableSize = element[1]
                    

        print("part2: " + str(smallestAcceptableSize))


main('Day07/input/input.txt')