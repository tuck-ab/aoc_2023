from enum import Enum
from collections import Counter

def part_1(input_data, p2=False):
    data = map(lambda x: x.split(" "), input_data)

    sorted_hands = sorted(data, key=lambda x: Hand(x[0], p2=p2))

    total = sum(int(bet) * (i+1) for i, (_, bet) in enumerate(sorted_hands))
    return total

def part_2(input_data):    
    return part_1(input_data=input_data, p2=True)

class Hand:
    def __init__(self, hand, p2=False):
        self.pre_hand = hand
        self.hand = hand

        if p2:
            self.m = dict(zip("J23456789TQKA", range(0, 13)))
        else:
            self.m = dict(zip("23456789TJQKA", range(0, 13)))


        if self.hand == "JJJJJ":
            self.hand = "AAAAA"

        if p2 and "J" in self.hand:
            counts = Counter(self.hand)
            counts.pop("J")
            target = max(counts.items(), key=lambda x: (x[1], self.m[x[0]]))[0]
            self.hand = "".join(char if char != "J" else target for char in self.hand)

    def __lt__(self, other):
        my_counts = sorted(Counter(self.hand).values(), reverse=True)
        other_co = sorted(Counter(other.hand).values(), reverse=True)

        if my_counts == other_co:
            i = 0
            while self.pre_hand[i] == other.pre_hand[i]:
                i += 1
            
            return self.m[self.pre_hand[i]] < self.m[other.pre_hand[i]]
        
        return my_counts < other_co
    