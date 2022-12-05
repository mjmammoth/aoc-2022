import re 
import numpy as np
array2D = []
array2DPart2 = []

with open("day-5/input.txt") as f:
    linesArray = f.read().split("\n")


    # find # of arrays: 
    for count, line in enumerate(linesArray):
        
        # Populate matrix with starter data
        # Find width of matrix
        if re.match('\s+\d\s+\d', line):
            for stack in re.findall('\d', line):
                array2D.append([])
                array2DPart2.append([])
            matrixHeader = count
            prepopulatedValues = linesArray[:matrixHeader]
            break

    for valueLine in prepopulatedValues[::-1]:
        columnCount = (len(array2D)*3) + (len(array2D) - 1)
        for i in range(1, columnCount, 4):
            if valueLine[i].isalpha():
                if i == 1:
                    arrayIndex = 0
                else:
                    arrayIndex = int((i - 1)/4)
                array2D[arrayIndex].append(valueLine[i])
                array2DPart2[arrayIndex].append(valueLine[i])

    for instruction in linesArray[matrixHeader+2:]:
        instructionInts = re.split(' ', instruction)
        fromIndex = int(instructionInts[3]) - 1
        toIndex = int(instructionInts[5]) - 1
        countIndex = int(instructionInts[1])

        for i in range(countIndex):
            #array2D[toIndex].append(arrayIndex[fromIndex].pop())
            array2D[toIndex].append(array2D[fromIndex].pop())

        for i in array2DPart2[fromIndex][-countIndex:]:
            array2DPart2[toIndex].append(i)
            array2DPart2[fromIndex].pop()

part1 = ''
for i in array2D:
        part1 += i[-1]
part2 = ''
for i in array2DPart2:
        part2 += i[-1]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
