with open("day-8/input.txt") as f:
    linesArray = f.read().split("\n")
    columns = [ [] for i in range(len(linesArray[0]))]
    rows = [ [] for i in range(len(linesArray))]
    columnCount = len(linesArray[0]) - 1
    rowCount = len(linesArray) - 1

    # calculate edges which will always be visible
    visible = (len(linesArray)*2 - 2) + (len(linesArray[0])*2 - 2)

    for y, row in enumerate(linesArray):
        for x, tree in enumerate(row):
            columns[y] += tree
            rows[x] += tree

    part1 = visible
    for y in range( 1, len(linesArray[0]) - 1 ):
        for x in range( 1, len(linesArray) - 1 ):
            left = columns[y][:x]
            right = columns[y][x+1:]
            up = rows[x][:y]
            down = rows[x][y+1:]
            number = columns[y][x]

            if all(x < number for x in left) or all(x < number for x in right) or all(x < number for x in up) or all(x < number for x in down):
                part1 += 1
                
print(f"Part 1: {part1}")
