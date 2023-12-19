import math

import numpy as np

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

MAPPER = {
    "|": NORTH | SOUTH,
    "-": EAST | WEST,
    "L": NORTH | EAST,
    "J": NORTH | WEST,
    "7": SOUTH | WEST,
    "F": SOUTH | EAST,
    ".": 0,
    "S": 16
}

DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
REVERSE = {0: 0, 1: 4, 2: 8, 4: 1, 8: 2}


def part_1(input_data):
    maze, s_point = parse_maze(input_data)

    sval = 0
    for i, d in enumerate(DIRS):
        m_val = maze[s_point[0]+d[0]][s_point[1]+d[1]]
        sval |= (1<<i) & REVERSE[REVERSE[1<<i] & m_val]
    
    maze[s_point[0]][s_point[1]] = sval

    loop_length = 0
    start_dir = 1<<[i for i in range(0, 4) if 1<<i & sval != 0][0]

    c = list(s_point)
    c_dir = start_dir

    while (not (c[0] == s_point[0] and c[1] == s_point[1])) or loop_length == 0:
        loop_length += 1
        d = DIRS[int(math.log2(c_dir))]
        c[0] += d[0]
        c[1] += d[1]

        val = maze[c[0]][c[1]]
        c_dir = val & (15 ^ REVERSE[c_dir])

    return int(loop_length/2)


LEFT = 1
RIGHT = 2
PATH = 4

def part_2(input_data):
    maze, s_point = parse_maze(input_data)

    sval = 0
    for i, d in enumerate(DIRS):
        m_val = maze[s_point[0]+d[0]][s_point[1]+d[1]]
        sval |= (1<<i) & REVERSE[REVERSE[1<<i] & m_val]
    
    maze[s_point[0]][s_point[1]] = sval

    diagram = [[0 for _ in maze[0]] for _ in maze]
    start_dir = 1<<[i for i in range(0, 4) if 1<<i & sval != 0][0]
    c = list(s_point)
    c_dir = start_dir

    while diagram[c[0]][c[1]] != PATH:
        diagram[c[0]][c[1]] = PATH
        d = DIRS[int(math.log2(c_dir))]

        l_d = DIRS[(int(math.log2(c_dir))-1)%4]
        r_d = DIRS[(int(math.log2(c_dir))+1)%4]
        try:
            if diagram[c[0]+l_d[0]][c[1]+l_d[1]] == 0:
                diagram[c[0]+l_d[0]][c[1]+l_d[1]] = LEFT
        except IndexError:
            pass
        
        try:
            if diagram[c[0]+r_d[0]][c[1]+r_d[1]] == 0:
                diagram[c[0]+r_d[0]][c[1]+r_d[1]] = RIGHT
        except IndexError:
            pass

        c[0] += d[0]
        c[1] += d[1]

        try:
            if diagram[c[0]+l_d[0]][c[1]+l_d[1]] == 0:
                diagram[c[0]+l_d[0]][c[1]+l_d[1]] = LEFT
        except IndexError:
            pass
        
        try:
            if diagram[c[0]+r_d[0]][c[1]+r_d[1]] == 0:
                diagram[c[0]+r_d[0]][c[1]+r_d[1]] = RIGHT
        except IndexError:
            pass

        val = maze[c[0]][c[1]]
        c_dir = val & (15 ^ REVERSE[c_dir])


    made_change = True
    while made_change:
        made_change = False

        for i, row in enumerate(diagram):
            for j, val in enumerate(row):
                if val != 1:
                    continue

                for d in DIRS:
                    try:
                        if diagram[i+d[0]][j+d[1]] == 0:
                            made_change = True
                            diagram[i+d[0]][j+d[1]] = 1
                    except IndexError:
                        pass



    counts = np.unique(np.array(diagram).flatten(), return_counts=True)
    return counts[1][1]
    

def parse_maze(maze):
    m = [list(map(lambda x: MAPPER[x], r)) for r in maze]

    for i, r in enumerate(m):
        for j, s in enumerate(r):
            if s == 16:
                return m, (i, j)