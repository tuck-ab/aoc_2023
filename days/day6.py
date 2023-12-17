import math

def part_1(input_data):
    times, distances = parse_data(input_data)
    
    product = 1

    for t, d in zip(times, distances):
        total = 0
        for i in range(1, t):
            total += calc_dist(i, t) > d
        product *= total

    return product

def part_2(input_data):
    times, distances = parse_data(input_data)

    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))

    press = 0
    while calc_dist(press, time) <= distance:
        press += 1

    return time - (2*press) + 1

def parse_data(d):
    times = list(map(int, [i for i in d[0].split(" ") if i != ""][1:]))
    distances = list(map(int, [i for i in d[1].split(" ") if i != ""][1:]))
    return times, distances

def calc_dist(p, t):
    return p * (t - p)