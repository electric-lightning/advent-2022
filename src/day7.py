# Really enjoyable challenge! Quite a contrast to yesterday. Reckon I spent 2.5h on it
# Lost about 30mins tracking down a bug, but it got well squished... Tired now.

with open('../inputs/day7.txt') as f:
    commands = [line.rstrip() for line in f]

# commands start with $
# everything else output of ls command
# items starting dir are a directory
# files are "size filename"

class File:
    name = ""
    size = 0
    dir = False
    parent = None
    contents = []

    def __init__(self, name, size, dir, parent):
        self.name = name
        self.size = size
        self.dir = dir
        self.parent = parent
        self.contents = []


root = None
cwd = None

def chdir(path):
    global cwd

    if '/' == path:
        cwd = root
    elif '..' == path:
        cwd = cwd.parent
    else:
        for item in cwd.contents:
            if item.dir and path == item.name:
                cwd = item
                break


def treewalk(item):
    total = 0
    for itm in item.contents:
        if itm.dir:
            total += treewalk(itm)
        else:
            total += itm.size

    return total


def get_directories(item, dirs):
    dirs.append(item)
    for itm in item.contents:
        if itm.dir:
            get_directories(itm, dirs)
    return dirs


def init_file_system():
    global root
    global cwd
    root = File('/', 0, True, None)
    cwd = None

    for command in commands:
        x = command.split()
        if command.find('$') >= 0:
            # command
            op = x[1]
            if 'cd' == op:
                path = x[2]
                chdir(path)
        elif 'dir' == x[0]:
            # directory
            cwd.contents.append(File(x[1], 0, True, cwd))
        else:
            # file
            cwd.contents.append(File(x[1], int(x[0]), False, cwd))


def part1():
    init_file_system()

    total = 0
    for dir in get_directories(root, []):
        result = treewalk(dir)
        if result <= 100000:
            total += result

    print(f'Part1: {total}')


def part2():
    init_file_system()

    total_used = treewalk(root)
    remaining = int(70000000)-total_used
    required = 30000000

    delete_candidate = []
    for dir in get_directories(root, []):
        result = treewalk(dir)
        if remaining + result >= required:
            delete_candidate.append(result)

    delete_candidate.sort()

    print(f'Part2: {delete_candidate[0]}')

part1()
part2()