def isList(str):
    if str[0] == '[':
        return True
    return False

# -1 if left is higher, +1 if right is higher, 0 if neutral
def processList(left, right):

    leftElements = getSubElements(left[1:-1])
    rightElements = getSubElements(right[1:-1])

    for l, r in zip(leftElements, rightElements):
        if not (isList(l) or isList(r)): # Both value
            if int(l) > int(r):
                return -1
            elif int(r) > int(l):
                return 1
        elif isList(l) and isList(r): # Both lists
            ret = processList(l, r)
            if ret != 0:
                return ret
        elif isList(r): # r List
            l = "[" + l + "]"
            ret = processList(l, r)
            if ret != 0:
                return ret
        elif isList(l): # l List
            r = "[" + r + "]"
            ret = processList(l, r)
            if ret != 0:
                return ret

    if len(leftElements) > len(rightElements):
        return -1
    elif len(rightElements) > len(leftElements):
        return 1
    else:
        return 0


def getSubElements(a):
    elements = []
    i = 0
    while i < len(a):
        if a[i] == "[": # List need matching paranthesis
            start = i
            lp = 1
            i += 1
            while lp != 0:
                if a[i] == "[":
                    lp += 1
                if a[i] == "]":
                    lp -= 1
                i += 1
            elements.append(a[start:i])
        elif a[i] == ",": # Find next value
            i += 1
        else:   # value, find all numbers
            start = i
            while i < len(a) and a[i].isnumeric():
                i += 1
            elements.append(a[start:i])
    return elements

def bubbleSort(input):
    n = len(input)
    swapped = False
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if processList(input[j], input[j+1]) == -1:
                swapped = True
                input[j], input[j+1] = input[j+1],  input[j]
        if not swapped:
            return

def findDecoderKey(lines, val1, val2):
    for n, line in enumerate(lines):
        if line == val1:
            a = n + 1
        if line == val2:
            b = n + 1
    return a * b

def main(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        lines = [n for n in lines if n]
    
        left = lines[0::2]
        right = lines[1::2]

        sum = 0
        for i in range(len(left)):
            
            if processList(left[i], right[i]) == 1:
                sum += i + 1

        print("part1: " + str(sum))

        lines.append("[[2]]")   
        lines.append("[[6]]")
        
        bubbleSort(lines)
        decKey = findDecoderKey(lines, "[[2]]", "[[6]]")
        print("part2: " + str(decKey))

main('Day13/input/input.txt')