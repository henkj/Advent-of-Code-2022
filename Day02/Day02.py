def part(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        myScore = myScore2 = 0

        for line in lines:
            op, me = line.split()
            myScore += calcScore1(me, op)
            myScore2 += calcScore2(me, op)
        
        print("part1: " + str(myScore))
        print("part2: " + str(myScore2))



def calcScore1(me, opponent):
    score = 0
    if me == "X":
        score += 1
        if opponent == "A":
            score += 3
        elif opponent == "C":
            score += 6
    if me == "Y":
        score += 2
        if opponent == "A":
            score += 6
        elif opponent == "B":
            score += 3  
    if me == "Z":
        score += 3
        if opponent == "B":
            score += 6
        elif opponent == "C":
            score += 3      
    return score   


def calcScore2(me, opponent):
    score = 0
    if me == "X":
        if opponent == "A":
            score += 3
        elif opponent == "B":
            score += 1
        else:
            score += 2
    if me == "Y":
        score += 3
        if opponent == "A":
            score += 1
        elif opponent == "B":
            score += 2
        else:
            score += 3
    if me == "Z":
        score += 6
        if opponent == "A":
            score += 2
        elif opponent == "B":
            score += 3
        else:
            score += 1
    return score   

part('Day02/input/input.txt')
