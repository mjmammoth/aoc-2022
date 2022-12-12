with open("day-4/input.txt") as f:
    linesArray = f.read().split("\n")

    subsetCount = 0
    intersectionCount = 0
    for line in linesArray:
        elfAssignments = line.split(",")
        # print(elfAssignments)
        elf1A = elfAssignments[0].split("-")
        elf2A = elfAssignments[1].split("-")
        elf1 = set(range(int(elf1A[0]), int(elf1A[1])+1))
        elf2 = set(range(int(elf2A[0]), int(elf2A[1])+1))
        if elf1.issubset(elf2) or elf2.issubset(elf1): subsetCount += 1
        if elf1.intersection(elf2): intersectionCount += 1

print("Part 1: "+str(subsetCount))
print("Part 2: "+str(intersectionCount))