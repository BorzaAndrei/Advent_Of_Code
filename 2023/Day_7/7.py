from collections import Counter
import functools

@functools.total_ordering
class Hand:

    strength = ["2", "3", "4", "5", "6", "7", "8", "9", "T", 'J', "Q", "K", "A"]

    strength_part_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    
    def __init__(self, cards) -> None:
        self.cards = [card for card in cards]
        counter = Counter(self.cards).most_common(5)

        # Part 1
        # replace most_common_non_j with counter[0][1]
        # replace second_most_common_non_j with counter[1][1]
        # replace strength with first one
 
        # Part 2
        j_list = list(filter(lambda x: x[0] == 'J', counter))
        j_counter = j_list[0][1] if len(j_list) > 0 else 0
        counter_non_j = list(filter(lambda x: x[0] != 'J', counter))
        most_common_non_j = counter_non_j[0][1] + j_counter if len(counter_non_j) > 0 else j_counter
        second_most_common_non_j = counter_non_j[1][1] if len(counter_non_j) > 1 else 0

        if most_common_non_j == 5:
            self.type = 7
        elif most_common_non_j == 4:
            self.type = 6
        elif most_common_non_j == 3 and second_most_common_non_j == 2:
            self.type = 5
        elif most_common_non_j == 3:
            self.type = 4
        elif most_common_non_j == 2 and second_most_common_non_j == 2:
            self.type = 3
        elif most_common_non_j == 2:
            self.type = 2
        else:
            self.type = 1


    def __eq__(self, other) -> bool:
        return self.cards == other.cards


    def __lt__(self, other) -> bool:
        if self.type != other.type:
            return self.type < other.type
        
        for ind in range(5):
            if self.cards[ind] != other.cards[ind]:
                return self.strength_part_2.index(self.cards[ind]) < self.strength_part_2.index(other.cards[ind])
        return False
    
    def __repr__(self) -> str:
        cards = "".join(self.cards)
        return f"{cards} - {self.type}"

with open("2023/Day_7/input.txt") as r:

    print(sum(list(map(lambda x: (x[0] + 1) * x[1][1], list(enumerate(sorted((map(lambda x: (Hand(x[0]), int(x[1])), [line.strip('\n').split() for line in r.readlines()])), key=lambda x: x[0])))))))
