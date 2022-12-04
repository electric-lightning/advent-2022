with open('../inputs/day3.txt') as f:
    bags = [line.rstrip() for line in f]

priority = {}


def createItemPriority():
    unicode = 97
    for i in range(1, 53):
        priority.setdefault(chr(unicode), i)
        if unicode == 122:  # Reached lowercase z, switch to upper case A
            unicode = 65
        else:
            unicode += 1
    print(f'Item priorities: {priority}')


def getDupItem(bag1, bag2):
    for item in bag1:
        if item in bag2:
            return item


def getDupItem2(bag1, bag2, bag3):
    for item in bag1:
        if item in bag2 and item in bag3:
            return item


def part1():
    total = 0
    for bag in bags:
        bag1, bag2 = bag[:len(bag) // 2], bag[len(bag) // 2:]
        dupItem = getDupItem(bag1, bag2)
        total += priority[dupItem]

    print(f'Part1: {total}')


def part2():
    total = 0
    while len(bags) > 0:
        bag1, bag2, bag3 = bags.pop(), bags.pop(), bags.pop()
        dupItem = getDupItem2(bag1, bag2, bag3)
        total += priority[dupItem]

    print(f'Part2: {total}')


createItemPriority()
part1()
part2()


