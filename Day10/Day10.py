def part1(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        x = 1
        signalStrengths = []

        cycle = 1
        for line in lines:
            val = 0
            if line != "noop":
                val = int(line.split()[1])
                signalStrengths.append(cycle*x)
                cycle +=1
            signalStrengths.append(cycle*x)
            x += val
            cycle += 1
        
        part1 = signalStrengths[19] + signalStrengths[59] + signalStrengths[99] + signalStrengths[139] + signalStrengths[179] + signalStrengths[219]
        print("part1: " + str(part1))
        
def writeToCrt(pos, sprite):
    if pos in sprite:
        return "#"
    else:
        return "."

def part2(input):
    with open(input) as f:
        lines = f.readlines()
        lines = [s.strip() for s in lines]

        sprite = (0, 1, 2)
        val = 1
        crtOutput = ""

        position = 0
        for line in lines:
            position = position % 40
            val = 0
            if line != "noop":
                val = int(line.split()[1])
                crtOutput += writeToCrt(position, sprite)
                position = (position + 1) % 40
            crtOutput += writeToCrt(position, sprite)
            sprite = (sprite[0]+val, sprite[1]+val, sprite[2]+val)
            position += 1
            
        print("part2:")
        for i in range(0, 201, 40):
            print(crtOutput[i:i+40])
      
part1('Day10/input/input.txt')
part2('Day10/input/input.txt')