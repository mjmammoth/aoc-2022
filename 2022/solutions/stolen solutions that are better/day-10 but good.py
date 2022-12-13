# AoC day 10 part 1

class Clock:
    def __init__(self):
        self.cycle = 0
        self.signal_strength = 0

    def inc(self, x):
        self.cycle += 1
        if self.cycle in range(20, 221, 40):
            self.signal_strength += x * self.cycle


with open('p10.txt') as f:
    program = f.read().splitlines()

x = 1
clock = Clock()
for instruction in program:
    match instruction.split():
        case ['noop']:
            clock.inc(x)
        case 'addx', number:
            clock.inc(x)
            clock.inc(x)
            x += int(number)
print(f'Total Signal Strength: {clock.signal_strength}')

# AoC day 10 part 2

class Clock:
    def __init__(self):
        self.cycle = 0
        self.signal_strength = 0
        self.crt = ['.' for _ in range(240)]

    def inc(self, pos):
        if self.cycle % 40 in [pos -1, pos, pos +1]:
            self.crt[self.cycle] = '#'
        self.cycle += 1

    def display(self):
        for row in range(6):
            start = row * 40
            end = start + 40
            print(''.join(self.crt[start:end]))


with open('p10.txt') as f:
    program = f.read().splitlines()

x = 1
clock = Clock()
for instruction in program:
    match instruction.split():
        case ['noop']:
            clock.inc(x)
        case ['addx', number]:
            clock.inc(x)
            clock.inc(x)
            x += int(number)
clock.display()