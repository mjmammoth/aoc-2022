def shouldSegmentMove(tailPos, headPos):
    noNeedToMovePositions = set()
    tailX = tailPos[0]
    tailY = tailPos[1]
    xPositions = list(range(tailX-1, tailX+2))
    yPositions = list(range(tailY-1, tailY+2))
    for x in xPositions:
        for y in yPositions:
            noNeedToMovePositions.add(str(f"{x}:{y}"))
    headPos = f"{headPos[0]}:{headPos[1]}"
    return not headPos in noNeedToMovePositions

def moveTail(t, h):
    if t[0] < h[0]-1:
        if t[1] == h[1]:
            t[0] += 1
        elif t[1] > h[1]:
            t[0] += 1
            t[1] -= 1
        elif t[1] < h[1]:
            t[0] += 1
            t[1] += 1
    elif t[0] > h[0]+1:
        if t[1] == h[1]:
            t[0] -= 1
        elif t[1] > h[1]:
            t[0] -= 1
            t[1] -= 1
        elif t[1] < h[1]:
            t[0] -= 1
            t[1] += 1
    elif t[1] < h[1]-1:
        if t[0] == h[0]:
            t[1] += 1
        elif t[0] < h[0]:
            t[0] += 1
            t[1] += 1
        elif t[0] > h[0]:
            t[0] -= 1
            t[1] += 1
    elif t[1] > h[1]+1:
        if t[0] == h[0]:
            t[1] -= 1
        elif t[0] < h[0]:
            t[0] += 1
            t[1] -= 1
        elif t[0] > h[0]:
            t[0] -= 1
            t[1] -= 1

def moveHead(headPos, direction):
    match direction:
        case 'R': headPos[0] += 1
        case 'L': headPos[0] -= 1
        case 'U': headPos[1] += 1
        case 'D': headPos[1] -= 1    
    return headPos

segment2UniquePositions = {'0:0'}
segment10UniquePositions = {'0:0'}
with open("day-9/input.txt") as f:
    linesArray = f.read().split("\n")
    ropeSegments = [[0, 0] for i in range(10)]
    
    for instruction in linesArray:
        instruction = instruction.split(' ')
        direction = instruction[0]
        amountToMove = int(instruction[1])
        
        for i in range(amountToMove):
            headPos = ropeSegments[0]
            headPos = moveHead(headPos, direction)
            for x, segment in enumerate(ropeSegments[1:]):
                headPos = ropeSegments[x]
                if shouldSegmentMove(segment, headPos):
                    moveTail(segment, headPos)
                    if x+1 == 1: segment2UniquePositions.add(f'{ropeSegments[x+1][0]}:{ropeSegments[x+1][1]}')
                    if x+1 == 9: segment10UniquePositions.add(f'{ropeSegments[x+1][0]}:{ropeSegments[x+1][1]}')
                else: break
        
print(f"Part 1: {len(segment2UniquePositions)}")
print(f"Part 2: {len(segment10UniquePositions)}")


    