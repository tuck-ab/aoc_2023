from typing import List

def part_1(input_data: List[str]):
    total = 0

    for word in input_data:
        counter = 0
        while not word[counter].isnumeric():
            counter += 1
        
        first_num = int(word[counter])

        counter = len(word) - 1
        while not word[counter].isnumeric():
            counter -= 1
        
        second_num = int(word[counter])

        total += first_num*10 + second_num

    return total

def part_2(input_data: List[str]):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    transformed = []
    for word in input_data:
        new_word = ""

        for i in range(0, len(word)):
            new_word += get_char(word, i, numbers)

        transformed.append(new_word)

    return part_1(transformed)

def get_char(word, i, numbers):
    for num in numbers:
        if len(word[i:]) >= len(num):
            if check_substr(word[i:], num):
                return str(numbers[num])
    return word[i]

def check_substr(substr, num):
    for c1, c2 in zip(substr, num):
        if c1 != c2:
            return False
        
    return True