f = open("input.txt", "r")
lines = f.readlines()
f.close()

summedCaloriesbyElf = []
calorieSum = 0
highestCalorieCount = 0
top3 = 0

for line in lines:
    if line not in ['\n', '\r\n']:
        calorieSum += int(line)
    else:
        if calorieSum > highestCalorieCount: highestCalorieCount = calorieSum
        summedCaloriesbyElf.append(calorieSum)
        calorieSum = 0

summedCaloriesbyElf.sort()
for value in summedCaloriesbyElf[-3:]:
    top3 += value

print("Part 1: " + str(summedCaloriesbyElf[-1]))
print("Part 2: " + str(top3))
