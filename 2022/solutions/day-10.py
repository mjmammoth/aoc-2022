from aoc import read_input
import math

class Register():
    def __init__(self):
        self.value = 1
        self.cycles = 0
        self.history = []
        self.screen = [[] for _ in range(6)]

    def addx(self, value):
        self.cycle()
        self.cycle()
        self.value += value
    
    def cycle(self):
        if self.cycles == 38:
            print(1)
        self.draw()
        self.history.append(self.value)
        self.cycles += 1
    
    def draw(self):
        self.row = math.floor(self.cycles/40)
        if self.cycles - (self.row * 40) in range(self.value-1, self.value+2):
            self.screen[self.row] += '#'
        else:
            self.screen[self.row] += '.'

    def render(self):
        for row in self.screen:
            print(''.join(row))

register = Register()
aocInput = read_input(__file__)
signalStrengthPart1 = 0

for instruction in aocInput:
    if instruction == 'noop':
        register.cycle()
    else:
        _, value = instruction.split()
        register.addx(int(value))

# Part 1
for i in range(19,240,40):
    signalStrengthPart1 += register.history[i] * (i+2)
print(f"Part 1: {signalStrengthPart1}")

# Part 2
register.render()
