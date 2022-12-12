# Read contents of input text file into an array
# Each line being an element in the array
f = open("input.txt", "r")
lines = f.readlines()
f.close()

# Initialize variables
summedCaloriesbyElf = []
tempCalorieSum = 0
top3 = 0

# Loop over each line in the text file
for line in lines:
    # Check if line is not empty
    if line not in ['\n', '\r\n']:
        # If line contains a number, add it to a temporary calorieSum variable
        tempCalorieSum += int(line)
    else:
        # If the line is empty, add the summed amount of calories for the elf to an array
        summedCaloriesbyElf.append(tempCalorieSum)
        # Revert temporary calorieSum variable to 0 so that we can calculate the next elf's calorieSum
        tempCalorieSum = 0

# Use python's sort method to easily sort the array from smallest to largest
summedCaloriesbyElf.sort()

# Sum the top 3 values in the array
# Last 3 values are gathered by list comprehension
top3 = sum(summedCaloriesbyElf[-3:])

# Print the highest number for the solution to part 1
print("Part 1: " + str(summedCaloriesbyElf[-1]))
# Print the sum of the 3 high
print("Part 2: " + str(top3))
