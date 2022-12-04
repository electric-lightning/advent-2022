with open('../inputs/day3.txt') as f:
    bags = [line.rstrip() for line in f]

dict = {}


def initDict():
    unicode = 97
    for i in range(1, 53):
        dict.setdefault(chr(unicode), i)
        if unicode == 122:
            unicode = 65
        else:
            unicode = unicode + 1

    print(f'dect: {dict}')


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
        item = getDupItem(bag1, bag2)
        total = total + dict[item]

    print(f'Part1: {total}')


def part2():
    total = 0
    while len(bags) > 0:
        bag1 = bags.pop(0)
        bag2 = bags.pop(0)
        bag3 = bags.pop(0)
        item = getDupItem2(bag1, bag2, bag3)
        total = total + dict[item]

    print(f'Part2: {total}')


initDict()
part1()
part2()


