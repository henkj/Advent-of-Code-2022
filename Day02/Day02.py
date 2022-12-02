def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

       # A, X ROCK
       # B, Y PAPER
       # C, Z SCISSORS
        myScore = 0
        for line in lines:
            myScore += calcScore(line[2], line[0])
        print(myScore)



def calcScore(mySign, opponentSign):
    score = 0
    if mySign == "X":
        score += 1
        if opponentSign == "A":
            score += 3
        elif opponentSign == "C":
            score += 6
    if mySign == "Y":
        score += 2
        if opponentSign == "A":
            score += 6
        elif opponentSign == "B":
            score += 3  
    if mySign == "Z":
        score += 3
        if opponentSign == "B":
            score += 6
        elif opponentSign == "C":
            score += 3      
    return score   

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

       # A, X ROCK
       # B, Y PAPER
       # C, Z SCISSORS
        myScore = 0
        for line in lines:
            myScore += calcScore2(line[2], line[0])
        print(myScore)

def calcScore2(mySign, opponentSign):
    score = 0
    if mySign == "X":
        if opponentSign == "A":
            score += 3
        elif opponentSign == "B":
            score += 1
        else:
            score += 2
    if mySign == "Y":
        score += 3
        if opponentSign == "A":
            score += 1
        elif opponentSign == "B":
            score += 2
        else:
            score += 3
    if mySign == "Z":
        score += 6
        if opponentSign == "A":
            score += 2
        elif opponentSign == "B":
            score += 3
        else:
            score += 1
    return score   

part1('Day02/input/input.txt')
part2('Day02/input/input.txt')