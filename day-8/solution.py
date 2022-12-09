def determineViewDistance(height: int, directionalArray):
    viewDistance = 0
    for tree in directionalArray:
        if int(tree) < height:
            viewDistance += 1
        elif int(tree) >= height: 
            return viewDistance + 1
        else:
            return viewDistance
    return viewDistance

def scenicScore(potentialTree, left, right, up, down):
    leftView = determineViewDistance(potentialTree, left)
    rightView = determineViewDistance(potentialTree, right)
    upView = determineViewDistance(potentialTree, up)
    downView = determineViewDistance(potentialTree, down)
    return leftView * rightView * upView * downView
        

with open("day-8/input.txt") as f:
    linesArray = f.read().split("\n")
    columns = [ [] for i in range(len(linesArray[0]))]
    rows = [ [] for i in range(len(linesArray))]
    part2 = 0

    # calculate edges which will always be visible
    part1 = (len(linesArray)*2 - 2) + (len(linesArray[0])*2 - 2)

    for y, row in enumerate(linesArray):
        for x, tree in enumerate(row):
            columns[y] += tree
            rows[x] += tree

    for y in range( 1, len(linesArray[0]) - 1 ):
        for x in range( 1, len(linesArray) - 1 ):
            left = columns[y][:x]
            right = columns[y][x+1:]
            up = rows[x][:y]
            down = rows[x][y+1:]
            number = columns[y][x]

            if all(x < number for x in left) or all(x < number for x in right) or all(x < number for x in up) or all(x < number for x in down):
                part1 += 1

    for y in range(len(linesArray[0])):
        for x in range(len(linesArray)):
            left = columns[y][:x]
            right = columns[y][x+1:]
            up = rows[x][:y]
            down = rows[x][y+1:]
            number = columns[y][x]
    
            left.reverse()
            up.reverse()
            if x == 2 and y == 3:
                print('now')
            temp = scenicScore(int(number), left, right, up, down)
            if temp > part2: part2 = temp
                
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
