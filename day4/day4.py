from collections import defaultdict
import re
import operator

with open('input') as file:
    puzzle = file.readlines()

def solve():
    guards = defaultdict(list)
    sleepingTime = defaultdict(int)
    puzzle.sort()

    for i in range(len(puzzle)):
        if "Guard" in puzzle[i]:
            guardId = puzzle[i].split()[3]
        else:
            guards[guardId].append(puzzle[i])

    for k, v in guards.items():
        sleepStart = 0
        for instans in v:
            if 'asleep' in instans:
                sleepStart = re.split("[:\]]", instans)[1]
            else:
                wakeUp = re.split("[:\]]", instans)[1]
                sleepingTime[k] += int(wakeUp) - int(sleepStart)

    sleepiestGuard = max(sleepingTime.items(), key=lambda a: a[1])
    print(sleepiestGuard)

    minutes = [0]*60
    shifts = guards[sleepiestGuard[0]]
    sleepStart = 0
    for info in shifts:
        if 'asleep' in info:
            sleepStart = re.split("[:\]]", info)[1]
        else:
            wakeUp = re.split("[:\]]", info)[1]
            for i in range(int(sleepStart), int(wakeUp)):
                minutes[i] += 1

    index_max = max(enumerate(minutes), key=operator.itemgetter(1))
    print(index_max)
    guardIdNumber = sleepiestGuard[0][1:]
    print(int(guardIdNumber) * index_max[0])


solve()