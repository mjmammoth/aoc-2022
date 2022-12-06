with open("day-6/input.txt") as f:
    datastream = f.readline()

    # Part 1
    for count, character in enumerate(datastream):
        if count < 3: continue
        temp = set(datastream[count-4:count])
        if len(temp) == 4:
            part1 = count
            break

    # Part 2
    part2 = 0
    for count, character in enumerate(datastream):
        if count < 13: continue
        temp = set(datastream[count-14:count])
        if len(temp) == 14:
            part2 = count
            break

print(f"Part1: {part1}")
print(f"Part2: {part2}")
