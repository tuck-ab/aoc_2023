def part_1(input_data):
    total = 0
    for card in input_data:
        num_matching = 0
        winners, nums = parse_card(card)
        winners = set(winners)

        for num in nums:
            num_matching += num in winners

        if num_matching:
            total += 2**(num_matching-1)

    return total


def part_2(input_data):
    copies = [0 for _ in input_data]

    for i, card in enumerate(input_data):
        copies[i] += 1
        winners, nums = parse_card(card)
        winners = set(winners)

        matching = 0
        for num in nums:
            matching += num in winners

        duplicates = copies[i]
        for j in range(1, matching+1):
            copies[i+j] += duplicates

    return sum(copies)


def parse_card(x: str):
    data = x.split(":")[1].strip().split("|")

    winners = [int(d) for d in data[0].split(" ") if d != ""]
    numbers = [int(d) for d in data[1].split(" ") if d != ""]

    return winners, numbers