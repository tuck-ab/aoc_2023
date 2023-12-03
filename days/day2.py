from typing import List

COLOURS = ["red", "blue", "green"]

def part_1(input_data: List[str]):
    parsed = map(parse_game, input_data)
    max_vals = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    total = 0

    for g_num, rounds in parsed:
        exceded = 0
        for r in rounds:
            for c in r:
                exceded += max_vals[c] < r[c]
        if exceded == 0:
            total += g_num

    return total


def part_2(input_data: List[str]):
    parsed = map(parse_game, input_data)

    total = 0

    for _, rounds in parsed:
        min_vals = dict.fromkeys(COLOURS, 0)
        for r in rounds:
            for c in r:
                min_vals[c] = max(min_vals[c], r[c])

        power = 1
        for item in min_vals.values():
            power *= item
        
        total += power

    return total


def parse_game(game: str):
    num, data = game.split(": ")

    num = num.split(" ")[1]

    data = data.split("; ")
    rounds = []
    for d in data:
        r = dict.fromkeys(COLOURS, 0)
        for cube in d.split(", "):
            n, c = cube.split(" ")
            r[c] = int(n)

        rounds.append(r)

    return int(num), rounds
