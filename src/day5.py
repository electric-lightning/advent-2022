#
# Cor blimey! That was intense after a hard day.
#

import queue

with open('../inputs/day5.txt') as f:
    changes = f.readlines()[10:]
    changes = [line.rstrip().replace('move ', '').replace(' from ', ' ').replace('to ', '') for line in changes]

q1 = queue.LifoQueue()
q1.put('T')
q1.put('D')
q1.put('W')
q1.put('Z')
q1.put('V')
q1.put('P')

q2 = queue.LifoQueue()
q2.put('L')
q2.put('S')
q2.put('W')
q2.put('V')
q2.put('F')
q2.put('J')
q2.put('D')

q3 = queue.LifoQueue()
q3.put('Z')
q3.put('M')
q3.put('L')
q3.put('S')
q3.put('V')
q3.put('T')
q3.put('B')
q3.put('H')

q4 = queue.LifoQueue()
q4.put('R')
q4.put('S')
q4.put('J')

q5 = queue.LifoQueue()
q5.put('C')
q5.put('Z')
q5.put('B')
q5.put('G')
q5.put('F')
q5.put('M')
q5.put('L')
q5.put('W')

q6 = queue.LifoQueue()
q6.put('Q')
q6.put('W')
q6.put('V')
q6.put('H')
q6.put('Z')
q6.put('R')
q6.put('G')
q6.put('B')

q7 = queue.LifoQueue()
q7.put('V')
q7.put('J')
q7.put('P')
q7.put('C')
q7.put('B')
q7.put('D')
q7.put('N')

q8 = queue.LifoQueue()
q8.put('P')
q8.put('T')
q8.put('B')
q8.put('Q')

q9 = queue.LifoQueue()
q9.put('H')
q9.put('G')
q9.put('Z')
q9.put('R')
q9.put('C')


def part1():
    lookup = {'1': q1, '2': q2, '3': q3, '4': q4, '5': q5, '6': q6, '7': q7, '8': q8, '9': q9}

    for change in changes:
        n_to_txf, q_from, q_to = change.split(' ')
        if n_to_txf == 1:
            lookup[q_to].put(lookup[q_from].get())
        else:
            flux = []
            for n in range(0, int(n_to_txf)):
                flux.append(lookup[q_from].get())
            for n in range(int(n_to_txf)-1, -1, -1):
                lookup[q_to].put(flux[n])

    topOfQ = ''
    for q in lookup.values():
        topOfQ += q.get()
    print(f'Top of each queue: {topOfQ}')


part1()


