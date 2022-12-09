def shouldTailMove(tailPos, headPos):
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

def moveTail(tailPos, headPos, direction):
    match direction:
        case 'R':
            tailPos[0] += 1
            if tailPos[1] != headPos[1]: tailPos[1] = headPos[1]
        case 'L':
            tailPos[0] -= 1
            if tailPos[1] != headPos[1]: tailPos[1] = headPos[1]
        case 'U':
            tailPos[1] += 1
            if tailPos[0] != headPos[0]: tailPos[0] = headPos[0]
        case 'D':
            tailPos[1] -= 1
            if tailPos[0] != headPos[0]: tailPos[0] = headPos[0]
    tailUniquePositions.add(f'{tailPos[0]}:{tailPos[1]}')
    return tailPos


def moveHead(tailPos, headPos, direction, amount):
    for i in range(amount):
        match direction:
            case 'R': headPos[0] += 1
            case 'L': headPos[0] -= 1
            case 'U': headPos[1] += 1
            case 'D': headPos[1] -= 1
        if shouldTailMove(tailPos, headPos):
            tailPos = moveTail(tailPos, headPos, direction)
    return tailPos, headPos

tailUniquePositions = {'0:0'}
with open("day-9/input.txt") as f:
    linesArray = f.read().split("\n")
    tailPos = [0, 0]
    headPos = [0, 0]
    
    for instruction in linesArray:
        instruction = instruction.split(' ')
        tailPos, headPos = moveHead(tailPos, headPos, instruction[0], int(instruction[1]))
        
print(len(tailUniquePositions))

    