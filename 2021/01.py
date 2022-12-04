with open("2021/inputs/01.txt") as f:
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

# from aoc import read_input
# 
# 
# data = read_input(1, int)
# for window in (1, 3):
#     print(sum(a < b for a, b in zip(data, data[window:])))