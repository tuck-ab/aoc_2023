def part_1(input_data):
    big_total = 0
    for data in input_data:
        mono, clues = data.split(" ")
        clues = tuple(map(int, clues.split(",")))

        mono_mask = sum([2**i * (c != "?") for i, c in enumerate(mono)])
        mono_hash = sum([2**i * (c == "#") for i, c in enumerate(mono)])
        mono_dots = sum([2**i * (c == ".") for i, c in enumerate(mono)])

        total = 0
        l = len(mono)
        for item in generate_sol(clues, l):
            item_hash = item
            item_dots = item ^ ((2**l)-1)

            total += item_hash&mono_mask == mono_hash and item_dots&mono_mask == mono_dots

        big_total += total
        print("done")

    return big_total

def part_2(input_data):
    transformed = list(map(transform, input_data))
    return part_1(transformed)

def transform(row):
    mono, clues = row.split(" ")
    clues = tuple(map(int, clues.split(",")))

    return f"{'?'.join(mono for _ in range(0, 5))} {','.join(','.join(map(str, clues)) for _ in range(0, 5))}"

def generate_sol(clues, n):
    startpoints = [0 for _ in clues]
    for i, c in enumerate(clues[:-1]):
        startpoints[i+1] = startpoints[i] + c + 1

    max_points = [n-(clues[-1]-1) for _ in clues]
    for i, c in enumerate(clues[-2::-1]):
        max_points[i+1] = max_points[i] - (c + 1)
    max_points = max_points[::-1]

    while startpoints[0] < max_points[0]:
        num = 0
        for s, l in zip(startpoints, clues):
            num |= 2**l - 1 << s
        yield num

        iter_i = len(clues) - 1
        startpoints[iter_i] += 1
        while startpoints[iter_i] >= max_points[iter_i] and startpoints[0] < max_points[0]:
            iter_i -= 1
            startpoints[iter_i] += 1

        for i, c in enumerate(clues[iter_i:-1]):
            startpoints[iter_i+i+1] = startpoints[iter_i+i] + c + 1


    return