with open("2021/day-1/input.txt") as f:
    linesArray = f.read().split("\n")

    increaseCount = 0
    cache = 0
    firstRun = True

    for line in linesArray:
        if firstRun == True:
            firstRun = False
            cache = int(line)
            continue
        if int(line) > cache:
            increaseCount += 1
        cache = int(line)


print(increaseCount)