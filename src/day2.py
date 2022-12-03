with open('../inputs/day2.txt') as f:
    rounds = [line.rstrip() for line in f]

rocks = ["A", "X"]
papers = ["B", "Y"]
scissors = ["C", "Z"]

rock = 1
paper = 2
scissor = 3


def score_part_1(theirs, yours):
    if theirs in rocks:
        if yours in rocks:
            return 3 + rock
        elif yours in scissors:
            return scissor
        elif yours in papers:
            return 6 + paper
    elif theirs in papers:
        if yours in rocks:
            return rock
        elif yours in scissors:
            return 6 + scissor
        elif yours in papers:
            return 3 + paper
    elif theirs in scissors:
        if yours in rocks:
            return 6 + rock
        elif yours in scissors:
            return 3 + scissor
        elif yours in papers:
            return paper


def score_part_2(theirs, yours):
    if theirs in rocks:
        if yours == "X":
            return 0 + scissor
        elif yours == "Y":
            return 3 + rock
        elif yours == "Z":
            return 6 + paper
    elif theirs in papers:
        if yours == "X":
            return 0 + rock
        elif yours == "Y":
            return 3 + paper
        elif yours == "Z":
            return 6 + scissor
    elif theirs in scissors:
        if yours == "X":
            return 0 + paper
        elif yours == "Y":
            return 3 + scissor
        elif yours == "Z":
            return 6 + rock


def part1():
    round_score = 0
    for round in rounds:
        round_result = round.split()
        round_score = round_score + score_part_1(round_result[0], round_result[1])
    print( round_score )


def part2():
    round_score = 0
    for round in rounds:
        round_result = round.split()
        round_score = round_score + score_part_2(round_result[0], round_result[1])
    print( round_score )


part1()
part2()

