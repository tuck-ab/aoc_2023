def part_1(input_data):
    patterns = parse_input(input_data)

    left = 0
    above = 0

    for p in patterns:
        conv = list(map(str, map(convert_str, p)))
        val = check_reflection(conv)
        if val:
            above += val

        conv = list(map(str, map(convert_str, zip(*p))))
        val = check_reflection(conv)
        if val:
            left += val

    return above * 100 + left

def part_2(input_data):
    patterns = parse_input(input_data)

    left = 0
    above = 0

    for p in patterns:
        conv = list(map(convert_str, p))
        val = smudge_reflection(conv)
        if val:
            above += val

        conv = list(map(convert_str, zip(*p)))
        val = smudge_reflection(conv)
        if val:
            left += val

    return above * 100 + left

def convert_str(s):
    val = 0
    for c in s:
        val = (val<<1) + (c=="#")
    return val

def smudge_reflection(p):
    for i in range(0, len(p)-1):
        if sum(map(lambda x: (x[0]^x[1]).bit_count(), zip(p[i::-1], p[i+1:]))) == 1:
            return i + 1

def check_reflection(p):
    for i in range(0, len(p)-1):
        if all(map(lambda x: x[0]==x[1], zip(p[i::-1], p[i+1:]))):
            return i + 1
        
def parse_input(input_data):
    patterns = []
    current = []
    
    for line in input_data:
        if line == "":
            patterns.append(current)
            current = []
        else:
            current.append(line)
    patterns.append(current)

    return patterns
        