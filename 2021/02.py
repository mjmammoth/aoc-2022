from aoc import read_input

horizontal = 0
vertical = 0
horizontal2=0
aim2=0
vertical2=0

data = read_input(2, str)
for movement in data:
    direction = movement.split(" ")[0]
    distance  = int(movement.split(" ")[1])

    match direction:
        case "forward":
            horizontal += distance
            horizontal2 += distance
            vertical2 += aim2 * distance
        case "up":
            vertical -= distance
            aim2 -= distance
        case "down":
            vertical += distance
            aim2 += distance

print(f"Part 1: {horizontal * vertical}")
print(f"Part 2: {horizontal2 * vertical2}")

