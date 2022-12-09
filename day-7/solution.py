def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def getContext(currentContext: str, command: str):
    if command[5:] == '/':
        return '/'    
    elif command[5:] == '..':
        folderIndices = find(currentContext, '/')
        return currentContext[:folderIndices[-2]+1]
    else:
        return currentContext + command[5:] + '/'

with open("day-7/input.txt") as f:
    linesArray = f.read().split("\n")
    
    directories = []
    directoryCount = 0
    beginIndex = 0
    context = ''
    adict = {}
    for index, line in enumerate(linesArray):
        if line.startswith('$ cd'):          
            if beginIndex != index:
                if beginIndex + 1 != index:
                    adict[context] = linesArray[beginIndex+2:index]
            beginIndex = index
            context = getContext(context, line)
            #print(line)
            #print(context)
    adict[context] = linesArray[beginIndex+2:]


# First find the size of each directory excluding other directories
filesize = {}
for directory in adict:
    sumOfDirectory = 0

    for ls in adict[directory]:
        try:
            sumOfDirectory += int(ls.split(' ')[0])
        except:
            #do nothing
            print('')

    filesize[directory] = sumOfDirectory

# Then find total size of each directory (including others)
directorySize = {}
for directory in filesize:
    directorySize[directory] = filesize[directory]

    folderIndices = find(directory, '/')
    print(folderIndices)
    if len(folderIndices) > 1:
        for parent in folderIndices[:-1]:
            tempParent = directory[0:parent+1]
            directorySize[tempParent] += filesize[directory]
print(directorySize)

part1 = 0
for recursiveSize in directorySize:
    if directorySize[recursiveSize] < 100000:
        part1 += directorySize[recursiveSize]

unusedDiskSpace = 70000000 - directorySize['/']
diskSpaceRequired = 30000000 - unusedDiskSpace

part2 = 70000000
for directory in directorySize:
    if directorySize[directory] > diskSpaceRequired:
        if directorySize[directory] < part2:
            part2 = directorySize[directory]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")