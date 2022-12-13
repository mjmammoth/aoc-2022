# AoC day 9
# NOT MINE, stolen from reddit.com/user/ElliotDG/
# Best example of how it should be done IMO

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def pos(self):
        return self.x, self.y


class Head(Knot):
    def step(self, direction):
        # move 1 step in the direction
        match direction:
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1
            case 'L':
                self.x -= 1
            case 'R':
                self.x += 1


class Tail(Knot):
    def __init__(self):
        super().__init__()
        self.history = set()

    def follow(self, pos):
        x, y = pos
        dist_x = x - self.x
        dist_y = y - self.y
        if abs(dist_x) == 2 and not dist_y: # horizontal
            xv = 1 if dist_x > 0 else -1
            self.x += xv
        elif abs(dist_y) == 2 and not dist_x: # vertical
            yv = 1 if dist_y > 0 else -1
            self.y += yv
        elif (abs(dist_y) == 2 and abs(dist_x) in (1, 2)) or (abs(dist_x) == 2 and abs(dist_y) in (1, 2)):
            xv = 1 if dist_x > 0 else -1
            self.x += xv
            yv = 1 if dist_y > 0 else -1
            self.y += yv
        self.history.add((self.x, self.y))


head = Head()
tail = Tail()
with open('day-9/input.txt') as f:
    directions = f.read().splitlines()

for direction in directions:
    dir_, steps = direction.split()
    for _ in range(int(steps)):
        head.step(dir_)
        tail.follow(head.pos)
print(f"Number of positions visited: {len(tail.history)}")

# part 2
head = Head()
tails = [Tail() for _ in range(9)]
for direction in directions:
    dir_, steps = direction.split()
    for _ in range(int(steps)):
        head.step(dir_)
        tails[0].follow(head.pos)
        for i in range(1, 9):
            tails[i].follow(tails[i-1].pos)
print(f"Number of positions visited: {len(tails[8].history)}")