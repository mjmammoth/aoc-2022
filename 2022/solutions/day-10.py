from aoc import read_input

class Register:
    def __init__(self):
        self.value = 1
        self.cycles = 0
        self.history = []
    
    def cycle(self):
        self.cycles += 1
        self.history.append(self.value)

    def addx(self, value):
        self.cycle()
        self.value += value
        self.cycle()

register = Register()

aocInput = read_input(__file__)
for instruction in aocInput:
    if instruction == 'noop':
        register.cycle()
    else:
        _, value = instruction.split()
        register.addx(int(value))

signalStrengthPart1 = 0
for i in range(18,220,40):
    signalStrengthPart1 += register.history[i] * (i+2)

print(f"Part 1: {signalStrengthPart1}")