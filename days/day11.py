def part_1(input_data, scale=2):
    empty_rows = [i for i, row in enumerate(input_data) if all(map(lambda x: x==".", row))]
    empty_cols = [i for i, row in enumerate(zip(*input_data)) if all(map(lambda x: x==".", row))]

    galaxies = {}
    index = 0

    for i, row in enumerate(input_data):
        for j, val in enumerate(row):
            if val == "#":
                i_corr = i + sum(map(lambda x: (x < i)*(scale-1), empty_rows))
                j_corr = j + sum(map(lambda x: (x < j)*(scale-1), empty_cols))
                galaxies[(i_corr, j_corr)] = index
                index += 1

    total = 0

    found = set()

    for galaxy in galaxies:
        for other in galaxies:
            if galaxy == other or tuple(sorted((galaxies[galaxy], galaxies[other]))) in found:
                continue

            total += dist(galaxy, other)
            found.add(tuple(sorted((galaxies[galaxy], galaxies[other]))))

    return total

def part_2(input_data):
    return part_1(input_data, scale=1000000)


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])