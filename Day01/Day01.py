def part(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        calories = 0
        elf = 1
        myDict = {}
        for line in lines:
            if line == "":
                myDict.update({elf: calories})
                elf+=1
                calories = 0
            else:
                calories += int(line)
        if calories != 0:
            myDict.update({elf: calories})  

    myDict = dict(sorted(myDict.items(), key=lambda item: item[1])) 
    res = dict(reversed(list(myDict.items())))
    print("part1: " + str(list(res.values())[0]))

    top3Cal = list(res.values())[0] + list(res.values())[1] + list(res.values())[2]
    print("part2: " + str(top3Cal))

part('Day01/input/input.txt')