with open('../inputs/day4.txt') as f:
    zones = [line.rstrip() for line in f]


def createrangelist(zone):
    return [item for item in range(int(zone[0]), int(zone[1])+1)]


def within(zone1, zone2):
    for n in zone1:
        if n not in zone2:
            return False
    return True


def within2(zone1, zone2):
    for n in zone1:
        if n in zone2:
            return True
    return False


def doit():
    total = 0
    total2 = 0
    for zone in zones:
        zonepair = zone.split(',')
        zone1 = createrangelist(zonepair[0].split('-'))
        zone2 = createrangelist(zonepair[1].split('-'))

        if within(zone1, zone2) or within(zone2, zone1):
            total += 1

        if within2(zone1, zone2) or within(zone2, zone1):
            total2 += 1

    print(f'part1: {total}')
    print(f'part2: {total2}')


doit()


