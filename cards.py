from dataclasses import dataclass, field
import random


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class Card:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit))

    def __str__(self):
        return f"{self.suit}{self.rank}"


# as is this is something of an ABC...
# it is instantiated like Deck(_french()) which is a bit odd
@dataclass
class Deck:
    """create a deck of Cards, shuffle on init"""
    deck: list[Card]

    def shuffle(self):
        """i want this to shuffle the self.deck attribue..."""
        random.shuffle(self.deck)
        return self

    def deal(self) -> Card:
        return self.deck.pop(0)

    def __post_init__(self):
        # shuffle the deck on init
        self.shuffle()

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.deck)
        return f'{self.__class__.__name__}({cards})'


def _french() -> list[Card]:
    """52 card deck, all ranks and suits"""
    ranks = RANKS
    suits = SUITS
    return [Card(rank=r, suit=s) for r in ranks for s in suits]

def _pinochle() -> list[Card]:
    """48 card deck, Ranks[9:A] all suits"""
    ranks = '9 10 J Q K A'.split()
    suits = SUITS
    return [Card(rank=r, suit=s) for r in ranks for s in suits for _ in range(2)]
    


# if we don't set the repr as false, we do not inherit Deck's repr method
@dataclass(repr=False)
class PinocleDeck(Deck):
    deck: list[Card] = field(default_factory=_pinochle)


@dataclass(repr=False)
class FrenchDeck(Deck):
    deck: list[Card] = field(default_factory=_french)


if __name__ == "__main__":

    f = FrenchDeck()
    p = PinocleDeck()