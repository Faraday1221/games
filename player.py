from typing import Union
from dataclasses import dataclass, field

from cards import Card


@dataclass
class Player:
    name: str
    stack: list[Card] = field(init=False)

    def __str__(self):
        stack = ", ".join([f"{c.suit}{c.rank}" for c in self.stack])
        return f"{self.__class__.__name__}(name={self.name}, stack=[{stack}])"

    def play_card(self) -> Card:
        """put down a card"""
        return self.stack.pop(0)

    def pickup(self, card: Union[Card, list[Card]]):
        """pick up a card and add it to the bottom your stack"""
        self.stack.extend(card)
