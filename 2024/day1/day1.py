from collections import Counter

def part1():
    lefts = []
    rights = []
    with open("./input.txt") as f:
        for line in f.readlines():
            tokens = line.split()
            lefts.append(int(tokens[0]))
            rights.append(int(tokens[1]))
    lefts.sort()
    rights.sort()
    zipped = zip(lefts, rights)
    return sum(map(lambda pair: abs(pair[0] - pair[1]), zipped))

def part2():
    lefts = []
    rights = []
    with open("./input.txt") as f:
        for line in f.readlines():
            tokens = line.split()
            lefts.append(int(tokens[0]))
            rights.append(int(tokens[1]))
    rightCounts = Counter(rights)
    return sum(map(lambda left: left * rightCounts[left], lefts))

print(part2())