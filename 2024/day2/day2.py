import copy

def isIncreasing(xs):
    for i in range(len(xs) - 1):
        if not xs[i] < xs[i + 1]:
            return False
    return True

def isDecreasing(xs):
    for i in range(len(xs) - 1):
        if not xs[i] > xs[i + 1]:
            return False
    return True

def isGradual(xs):
    for i in range(len(xs) - 1):
        diff = abs(xs[i] - xs[i + 1])
        if not (diff >= 1 and diff <= 3):
            return False
    return True

def isSafe(xs):
    return isGradual(xs) and (isIncreasing(xs) or isDecreasing(xs))

# https://stackoverflow.com/questions/157039/most-pythonic-way-of-counting-matching-elements-in-something-iterable#157141
def quantify(seq, pred=None):
    "Count how many times the predicate is true in the sequence"
    return sum(map(pred, seq))

def part1():
    with open("./input.txt") as f:
        lines = f.readlines()
        reports = list(map(lambda line: list(map(int, line.split())), lines))
        return quantify(reports, isSafe)

def dampenedReports(report):
    copies = list(map(lambda _idx: copy.deepcopy(report), range(len(report))))
    for i in range(len(report)):
        copies[i].pop(i)
    return copies

def isSafeDampened(report):
    if isSafe(report):
        return True
    return any(map(isSafe, dampenedReports(report)))

def part2():
    with open("./input.txt") as f:
        lines = f.readlines()
        reports = list(map(lambda line: list(map(int, line.split())), lines))
        return quantify(reports, isSafeDampened)

print(part2())