from aoc import read_input

data = read_input(3, str)
mostCommon = ''
leastCommon = ''
#gammaRate
#epsilonRate
array2d = [[],[],[],[],[],[],[],[],[],[],[],[]]
count = 0
for reading in data:
    count+=1
    for i, bit in enumerate(reading):
        array2d[i].append(int(bit))

for bitRepresentation in array2d:
    mostCommon += str(round(sum(bitRepresentation)/count))

for bit in mostCommon:
    if bit == "0": leastCommon += "1"
    if bit == "1": leastCommon += "0"

energyRate = int(mostCommon, 2) * int(leastCommon, 2)
print(f"Part 1: {energyRate}")