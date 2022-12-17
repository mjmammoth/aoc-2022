from aoc import read_input
import math

class Monkey():
    def __init__(self, items, worryOperator, testDivisor, throwTo):
        self.items = [ int(item) for item in items]
        self.worryOperator = worryOperator
        self.testDivisor = testDivisor
        self.throwTo = throwTo
        self.inspected = 0
    
    def inspectItem(self):
        operator, amount = self.worryOperator.split()
        old = self.items[0]
        number = old if amount == 'old' else int(amount)
        match operator:
            case '+':
                self.items[0] = self.items[0] + int(number)
            case '*':
                self.items[0] = self.items[0] * int(number)
        self.inspected += 1

    def getBored(self):
        self.items[0] = math.floor(self.items[0] / 3)

    def throwItem(self):
        if self.items[0] % self.testDivisor == 0:
            return self.items.pop(0), self.throwTo[0]
        else:
            return self.items.pop(0), self.throwTo[1]

    def catchItem(self, item):
        self.items.append(item)


def playRound(monkeys):
    for monkey in monkeys:
        itemsToThrow = len(monkey.items)
        for _ in range(itemsToThrow):
            monkey.inspectItem()
            monkey.getBored()
            thrownItem, monkeyIndex = monkey.throwItem()
            monkeys[monkeyIndex].catchItem(thrownItem)

def populateInitialMonkeyState():
    monkeySeparators = [1] + [i+2 for i, x in enumerate(aocInput) if x == '']
    monkeys = []
    for separatorIndex in monkeySeparators:
        # Items
        itemString = aocInput[separatorIndex][18:]
        if ',' in itemString:
            items = itemString.split(', ')
        else:
            items = [itemString]

        worryOperator = aocInput[separatorIndex+1][23:]
        testDivisor = int(aocInput[separatorIndex+2][21:])
        passTo = [ int(aocInput[valuation][-1]) for valuation in range(separatorIndex+3, separatorIndex+5) ]
        monkeys.append(Monkey(items, worryOperator, testDivisor, passTo))
    return monkeys

def calculateMonkeyBusiness(monkeys):
    array = []
    for monkey in monkeys:
        array.append(monkey.inspected)
    array.sort()
    return math.prod(array[-2:])

aocInput = read_input(__file__)
monkeys = populateInitialMonkeyState()

for _ in range(20):
    playRound(monkeys)

print(f"Part1: {calculateMonkeyBusiness(monkeys)}")