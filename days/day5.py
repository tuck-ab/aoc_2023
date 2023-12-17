def part_1(input_data):
    seeds = input_data[0].split(": ")[1].split(" ")

    maps = get_maps(input_data)

    nearest = 1000000000000000000000000000

    for seed in seeds:
        s = int(seed)
        for map_data in maps:
            s = convert(s, map_data)

        nearest = min(s, nearest)

    return nearest

def part_2(input_data):
#     input_data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4
# """.splitlines()
    
    seeds = input_data[0].split(": ")[1].split(" ")

    maps = get_maps(input_data)

    ranges = [tuple(map(int, s)) for s in zip(seeds[::2], seeds[1::2])]

    layer = 6

    for m in maps[:layer+1]:
        debugger = []
        new_ranges = []
        while len(ranges) > 0:
            start, length = ranges.pop(0)
            endpoint = start + length
            for d, s, l in m:
                e = s + l
                if length <= 0:
                    continue

                if start < s and start + length > s:
                    new_ranges.append((d, min(l, endpoint-s)))
                    debugger.append((s, d, min(l, endpoint-s)))
                    if endpoint > e:
                        ranges.append((e, endpoint - e))

                    length = s - start
                    endpoint = start + length

                if start >= s and start < e:
                    new_ranges.append((d + (start - s), min(length, l)))
                    debugger.append((start, d + (start - s), min(length, l)))

                    start = e
                    length = endpoint - e

            if length > 0:
                new_ranges.append((start, length))
                debugger.append((s, s, length))

        ranges = new_ranges

    print("Mapper")
    for item in maps[layer]:
        print(item)
    print("Transitions")
    for item in debugger:
        print(item)

    return min(ranges, key=lambda x:x[0])[0]

def convert(x, map_data):
    for d, s, l in map_data:
        if x >= s and x < s+l:
            return d + (x - s)
        
    return x

def convert_rev(x, map_data):
    for s, d, l in map_data:
        if x >= s and x < s+l:
            return d + (x - s)
        
    return x

def get_maps(data):
    maps = []
    line_i = 3
    while line_i < len(data):
        local_map_data = []
        while line_i < len(data) and data[line_i] != "":
            local_map_data.append(tuple(map(int, data[line_i].split(" "))))
            line_i += 1
        maps.append(local_map_data)
        line_i += 2
    return maps
