from typing import List

NUMBER = set(map(str, range(0, 10)))
NON_SYMBOL = NUMBER | {"."}

def part_1(input_data: List[str]):
    total = 0

    for i, sub_list in enumerate(input_data):
        j = 0
        while j < len(sub_list):
            if not sub_list[j].isnumeric():
                j += 1
            else:
                num = int(sub_list[j])
                col_nums = [j]
                j += 1
                while j < len(sub_list) and sub_list[j].isnumeric():
                    num *= 10
                    num += int(sub_list[j])
                    col_nums.append(j)
                    j += 1

                to_add = False

                for col in col_nums:
                    if i > 0:
                        to_add |= input_data[i-1][col] not in NON_SYMBOL
                    if i < len(input_data) - 1:
                        to_add |= input_data[i+1][col] not in NON_SYMBOL

                min_col = min(col_nums)
                if min_col > 0:
                    to_add |= input_data[i][min_col-1] not in NON_SYMBOL
                    if i > 0:
                        to_add |= input_data[i-1][min_col-1] not in NON_SYMBOL
                    if i < len(input_data) - 1:
                        to_add |= input_data[i+1][min_col-1] not in NON_SYMBOL

                max_col = max(col_nums)
                if max_col < len(sub_list) - 1:
                    to_add |= input_data[i][max_col+1] not in NON_SYMBOL
                    if i > 0:
                        to_add |= input_data[i-1][max_col+1] not in NON_SYMBOL
                    if i < len(input_data) - 1:
                        to_add |= input_data[i+1][max_col+1] not in NON_SYMBOL

                if to_add:
                    total += num
                    
    return total

DIRECTIONS = [
    [1, 1],
    [1, 0],
    [1, -1],
    [0, 1],
    [0, -1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
]

def part_2(input_data: List[str]):
    total = 0

    for i, sub_list in enumerate(input_data):
        for j, char in enumerate(sub_list):
            if char == "*":
                nums = []
                searched = set()
                for di, dj in DIRECTIONS:
                    if (i+di, j+dj) in searched:
                        continue
                    if i + di < 0 or i + di >= len(input_data):
                        continue
                    if j + dj < 0 or j + dj >= len(sub_list):
                        continue
                    if input_data[i + di][j + dj].isnumeric():
                        ti, tj = i + di, j + dj
                        while tj > 0 and input_data[ti][tj].isnumeric():
                            tj -= 1
                        
                        if not input_data[ti][tj].isnumeric():
                            tj += 1

                        num = 0
                        while tj < len(sub_list) and input_data[ti][tj].isnumeric():
                            num *= 10
                            num += int(input_data[ti][tj])
                            searched.add((ti, tj))
                            tj += 1
                        nums.append(num)

                if len(nums) == 2:
                    total += nums[0]*nums[1]

    return total


