import math

def part_1(input_data):
    instructions = list(map(lambda x: x == "R", input_data[0]))
    num = len(input_data[0])

    mapper = {}

    for data in input_data[2:]:
        node, paths = data.split(" = ")
        paths = paths[1:-1]
        l, r = paths.split(", ")

        mapper[node] = (l, r)

    steps = 0
    current = "AAA"

    while current != "ZZZ":
        current = mapper[current][instructions[steps%num]]
        steps += 1

    return steps

def part_2(input_data):
    instructions = list(map(lambda x: x == "R", input_data[0]))
    num = len(input_data[0])

    mapper = {}
    starts = []
    ends = []

    for data in input_data[2:]:
        node, paths = data.split(" = ")
        paths = paths[1:-1]
        l, r = paths.split(", ")

        mapper[node] = (l, r)

        if node[-1] == "A":
            starts.append(node)

        if node[-1] == "Z":
            ends.append(node)

    print(ends)

    chains_data = []
    funcs = []

    for start in starts:
        counter = 0
        current = start
        chain = {}
        data = {
            "z_list": [],
            "chain_start": 0,
            "chain_len": 0
        }

        while (current, counter%num) not in chain:
            chain[(current, counter%num)] = counter
            if current[-1] == "Z":
                data["z_list"].append(counter)
            current = mapper[current][instructions[counter%num]]

            counter += 1

        data["chain_start"] = chain[(current, counter%num)]
        data["chain_len"] = counter - data["chain_start"]
        chains_data.append(data)

        chain_len = counter - chain[(current, counter%num)]
        for z in data["z_list"]:
            funcs.append((chain_len, z))
            
    # Through analysis of functions its found that only one z value
    # appears in each chain and the loc of z value == length of chain
    # Therefore need to find the lcm of the values

    values = list(map(lambda x: x[0], funcs))

    lcm = 1
    for val in values:
        lcm = lcm * (val // math.gcd(lcm, val))

    return lcm
