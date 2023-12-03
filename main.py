from argparse import ArgumentParser
from importlib import import_module
import json
import os
import pathlib

import requests

DIR = pathlib.Path(__file__).parent.resolve()

def get_input(day):
    with open(os.path.join(DIR, "private.json")) as f:
        data = json.load(f)

    cookies = data["aoc_cookies"]

    response = requests.get(f"https://adventofcode.com/2023/day/{day}/input",
                            cookies=cookies)
    
    return response.content.decode().splitlines()

parser = ArgumentParser(prog="Advent of Code 2023",
                        description="Solutions for the Advent of Code 2023 problems")

parser.add_argument("-d", "--day", action="store", required=True)
parser.add_argument("-p", "--part", action="store", required=True, choices=["1", "2"])


if __name__ == "__main__":
    args = parser.parse_args()

    try:
        problem = import_module(f"days.day{args.day}")
    except Exception as e:
        print("Could not find implemenation for day number")
        exit(0)

    if args.part == "1":
        result = problem.part_1(input_data=get_input(args.day))
    elif args.part == "2":
        result = problem.part_2(input_data=get_input(args.day))
    else:
        print("Invalid part number entered")
    
    print(result)
