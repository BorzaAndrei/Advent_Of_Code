import re
from dataclasses import dataclass
from typing import List, Set

@dataclass
class Card:
    id: int
    matching: int
    acquired: int = 1

    def __str__(self) -> str:
        return f"Card #{self.id} - Matching: {self.matching} - {self.acquired}"


cards: List[Card] = []
with open("input.txt") as r:
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Part 1
    lines = r.readlines()
    print(sum(map(lambda x: pow(2, len(x[0].intersection(x[1])) - 1) if len(x[0].intersection(x[1])) > 0 else 0, map(lambda wON: (set([int(no) for no in re.findall('\d+', wON[0])]), set([int(no) for no in re.findall('\d+', wON[1])])), [line.strip('\n').split(': ')[1].split(' | ') for line in lines]))))


    for line in lines:
        cardNumbers = line.strip('\n').split(': ')
        winningOtherNumbers = cardNumbers[1].split(' | ')
        winningNumbers = set([int(no) for no in re.findall('\d+', winningOtherNumbers[0])])
        otherNumbers = set([int(no) for no in re.findall('\d+', winningOtherNumbers[1])])

        cards.append(Card(re.findall('\d+', cardNumbers[0])[0], len(winningNumbers.intersection(otherNumbers))))
    
    for ind, card in enumerate(cards):
        for card_ind in range(ind + 1, ind + 1 + card.matching):
            cards[card_ind].acquired += card.acquired
    
    print(sum([card.acquired for card in cards]))
