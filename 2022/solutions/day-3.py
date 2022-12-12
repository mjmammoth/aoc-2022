import string

with open("day-3/example.txt") as f:
    rucksacks = f.read().split("\n")

    sumPriorities = 0
    sumPrioritiesPart2 = 0
    count = 1
    elf1 = ''
    elf2 = ''
    elf3 = ''

    for rucksack in rucksacks:
        # Part One
        half = int(len(rucksack.strip())/2)
        compartmentOne = rucksack[0:half]
        compartmentTwo = rucksack[half:]
        intersection = set(compartmentOne).intersection(compartmentTwo)
        letters = list(string.ascii_letters)
        sumPriorities += letters.index(list(intersection)[0]) + 1

        # Part 2
        match count:
          case 1:
            elf1 = set(rucksack)
          case 2:
            elf2 = set(rucksack)
          case 3:
            elf3 = set(rucksack)
            badge = elf1.intersection(elf2, elf3)
            #print(elf1)
            #print(elf2)
            #print(elf3)
            print(badge)
            sumPrioritiesPart2 += letters.index(list(badge)[0]) + 1
            count = 0
        count += 1

print(sumPriorities)
print(sumPrioritiesPart2)