# Didn't enjoy this one! Disjointed story too which didn't seem to pick up from the day before.
# Did part 1 no issues. Then didn't notice the requirement change in rope movement for part2 so wasted a lot of time
# before re-reading and clicking to that and by then it was time for bed.
# I had another stab at part 2 on sat evening but got fed up doing the tedious debugging required for this. I beat
# last year by a day! Woo hoo! The impetus is lost now so probably won't do many more.

with open('../inputs/day9.test') as f:
    moves = [line.rstrip() for line in f]


class RopeSection:
    x = None
    y = None
    prevx = None
    prevy = None

    def __init__(self, x, y, prevx, prevy):
        self.x = x
        self.y = y
        self.prevx = prevx
        self.prevy = prevy


def ahead_adjacent_to_behind(knot_ahead, knot_behind):

    x = knot_behind.x
    y = knot_behind.y

    if knot_ahead.x == x and knot_ahead.y == y:
        return True
    if knot_ahead.x == x+1 and knot_ahead.y == y:
        return True
    if knot_ahead.x == x+1 and knot_ahead.y == y+1:
        return True
    if knot_ahead.x == x and knot_ahead.y == y+1:
        return True
    if knot_ahead.x == x-1 and knot_ahead.y == y+1:
        return True
    if knot_ahead.x == x-1 and knot_ahead.y == y:
        return True
    if knot_ahead.x == x-1 and knot_ahead.y == y-1:
        return True
    if knot_ahead.x == x and knot_ahead.y == y-1:
        return True
    if knot_ahead.x == x+1 and knot_ahead.y == y-1:
        return True

    return False


def part1():
    start = RopeSection(0, 0, None, None)
    prev_head = start
    cur_tail = start
    head = [start]
    tail = [start]

    for move in moves:
        direction, steps = move.split(' ')

        cur_head = None
        for step in range(0, int(steps)):
            if 'U' == direction:
                cur_head = RopeSection(prev_head.x, prev_head.y+1, prev_head.x, prev_head.y)
            elif 'D' == direction:
                cur_head = RopeSection(prev_head.x, prev_head.y-1, prev_head.x, prev_head.y)
            elif 'L' == direction:
                cur_head = RopeSection(prev_head.x-1, prev_head.y, prev_head.x, prev_head.y)
            elif 'R' == direction:
                cur_head = RopeSection(prev_head.x+1, prev_head.y, prev_head.x, prev_head.y)

            head.append(cur_head)
            if not ahead_adjacent_to_behind(cur_head, cur_tail):
                cur_tail = RopeSection(prev_head.x, prev_head.y, None, None)
                tail.append(cur_tail)

            prev_head = cur_head

    tails = []
    for t in tail:
        tails.append(f'{t.x},{t.y}')

    unique = set(tails)
    print('Part1:', len(unique))


def part2():
    knots = [[RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)],
             [RopeSection(0, 0, None, None)]]
    prev_head = knots[0][0]

    for move in moves:
        direction, steps = move.split(' ')

        for step in range(0, int(steps)):
            if 'U' == direction:
                cur_head = RopeSection(prev_head.x, prev_head.y+1, prev_head.x, prev_head.y)
            elif 'D' == direction:
                cur_head = RopeSection(prev_head.x, prev_head.y-1, prev_head.x, prev_head.y)
            elif 'L' == direction:
                cur_head = RopeSection(prev_head.x-1, prev_head.y, prev_head.x, prev_head.y)
            else:
                cur_head = RopeSection(prev_head.x+1, prev_head.y, prev_head.x, prev_head.y)

            knots[0].append(cur_head)

            i = 1
            while i < len(knots):
                knot_before = knots[i-1][len(knots[i-1])-1]
                knot = knots[i][len(knots[i])-1]
                if not ahead_adjacent_to_behind(knot_before, knot):
                    if i == 1:
                        # knot 1 just follows heads previous
                        knots[i].append(RopeSection(knot_before.prevx, knot_before.prevy, knot.x, knot.y))
                    else:
                        # the rest follow the next knot in a stricter fashion, no diagonal moves
                        move_x = knot_before.x - knot_before.prevx
                        move_y = knot_before.y - knot_before.prevy
                        if move_x == 0 and move_y != 0:
                            knots[i].append(RopeSection(knot_before.x, knot.y + move_y, knot.x, knot.y))
                        elif move_x != 0 and move_y == 0:
                            knots[i].append(RopeSection(knot.x+move_x, knot_before.y, knot.x, knot.y))
                        else:
                            knots[i].append(RopeSection(knot.x+move_x, knot.y+move_y, knot.x, knot.y))
                i += 1

            prev_head = cur_head
            nines = []
            for k in knots[9]:
                nines.append(f'{k.x},{k.y}')
            print(nines)

    tails = []
    for k in knots[9]:
        tails.append(f'{k.x},{k.y}')

    unique = set(tails)
    print('Part2:', len(unique))



part1()
part2()
