with open('../inputs/day8.txt') as f:
    tree_heights = [line.rstrip() for line in f]
    #tree_heights = f.read().replace('\n', '')


class Tree:
    height = None
    n = None
    e = None
    s = None
    w = None
    def __init__(self, height):
        self.height = height

    def is_border_tree(self):
        return self.n is None \
                or self.e is None \
                or self.s is None \
                or self.w is None

    def get_neighbour(self, direction):
        if 'n' == direction:
            return self.n
        elif 'e' == direction:
            return self.e
        elif 's' == direction:
            return self.s
        elif 'w' == direction:
            return self.w


def is_tree_visible_from_edge(neighbour_tree, direction, height):

    if neighbour_tree.height >= height:
        # not visible
        return False
    elif neighbour_tree.height < height and neighbour_tree.is_border_tree():
        # visible
        return True
    else:
        # Not at edge so check the next...
        return is_tree_visible_from_edge(neighbour_tree.get_neighbour(direction), direction, height)


def is_visible(tree):
    directions = ['n', 's', 'e', 'w']
    for direction in directions:
        visible = is_tree_visible_from_edge(tree.get_neighbour(direction), direction, tree.height)
        if visible:
            return True

    return False


forest = []


def create_forest():
    # Build a list of trees where each tree will know where the next tree is (N, S, E & W) and each tree `
    # will also know if it is a border tree.
    previous_tree = None
    row_count = len(tree_heights[0])
    row = 0
    col = 0
    for heights in tree_heights:
        for height in heights:
            tree = Tree(height)
            # there won't be a prev tree if on first tree in a row
            if previous_tree is not None:
                # curr tree and prev tree can ref each other
                tree.w = previous_tree
                previous_tree.e = tree
            # Add this tree and temp store it for next round
            forest.append(tree)
            previous_tree = tree

            # as long as we're past the first row, start populating refs to north/south trees
            if row > 0:
                tree.n = forest[(row_count*(row-1))+col]
                tree.n.s = tree

            col += 1

        # end of row of trees, reset previous tree for next row, inc row and reset col
        previous_tree = None
        row += 1
        col = 0


def part1():
    # 1. visible trees from the edge
    visible = 0
    for tree in forest:
        if tree.is_border_tree():
            visible += 1
            continue
        else:
            if is_visible(tree):
                visible += 1

    print(f'Part1. Trees in forest: {len(forest)}. Number visible from edge: {visible}')


create_forest()
part1()
#part2()

def part2():
    # 2. visible trees from the edge
    visible = 0
    for tree in forest:
        if tree.is_border_tree():
            visible += 1
            continue
        else:
            if is_visible(tree):
                visible += 1
    print(f'Part1. Trees in forest: {len(forest)}. Number visible from edge: {visible}')