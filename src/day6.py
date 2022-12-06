# For me, the easiest to date... on day 6? Could have done with this one last night.

with open('../inputs/day6.txt') as f:
    data = [line.rstrip() for line in f]


def popnpush(char, fifo_stack, stack_size):
    if len(fifo_stack) == stack_size:
        fifo_stack.pop(0)
    fifo_stack.append(char)


def part(part, stack_size):
    fifo_stack = []

    index = 0
    for char in data[index]:
        if len(fifo_stack) == stack_size \
                and len(set(fifo_stack)) == stack_size:
            break
        else:
            popnpush(char, fifo_stack, stack_size)

        index += 1

    print(f'Part{part}: {index}')


part(1, 4)
part(2, 14)