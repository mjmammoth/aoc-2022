import os

def read_input(file, example = 0):
    day = file[file.rfind('/')+1:-3]
    root = os.path.realpath(os.path.join(os.path.dirname(file), '..'))
    type = 'input' if not example else 'example'
    with open(f"{root}/inputs/{day}_{type}.txt") as f:
        return f.read().split("\n")
