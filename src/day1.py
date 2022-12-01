with open('../inputs/day1.txt') as f:
    cals = [line.rstrip() for line in f]

def part1():
    total = 0
    highest = 0
    for cal in cals:
        if cal == '':
            if total > highest:
                highest = total
            total = 0
        else:
            total = total + int(cal)
    print(f'Part1: {highest}')


def part2():
    total = 0
    highest1 = 0
    highest2 = 0
    highest3 = 0
    for cal in cals:
        if cal == '':
            if total > highest1:
                highest3 = highest2
                highest2 = highest1
                highest1 = total
            elif total > highest2:
                highest3 = highest2
                highest2 = total
            elif total > highest3:
                highest3 = total
            total = 0
        else:
            total = total + int(cal)
    print(f'Part2: {highest1+highest2+highest3}')


part1()
part2()
