from typing import Union, List
from dataclasses import dataclass, field
from time import sleep
import random

from player import Player
from cards import FrenchDeck, Card



class War:
    def __init__(self):
        deck = FrenchDeck()

        self.player1 = Player(name="Player 1")
        self.player2 = Player(name="Player 2")

        self.player1.stack = [deck.deal() for _ in range(26)]
        self.player2.stack = [deck.deal() for _ in range(26)]

        self.winner = None


    def _war(self, pot: list[Card], n: int=2) -> None:
        try:
            for _ in range(n):
                pot.extend([self.player1.play_card(), self.player2.play_card()])

            c1, c2 = self.player1.play_card(), self.player2.play_card()
            print(f"Player1: {c1.rank}{c1.suit}\tPlayer2: {c2.rank}{c2.suit}")
            pot.extend([c1, c2])
            if c1.rank == c2.rank:
                self._war(pot=pot, n=1)
            elif c1 > c2:
                self.player1.pickup(pot)
            elif c1 < c2:
                self.player2.pickup(pot)
        except IndexError:
            # pop from empty list, occurs when one player runs out of cards
            # if a player runs out of cards, the game is over
            pass

    def _gameloop(self):
        self.cnt = 0
        while len(self.player1.stack) > 0 and len(self.player2.stack) > 0:
            # print(f"player 1: {len(player1.stack)}\t player 2: {len(player2.stack)}")

            self.cnt += 1
            c1, c2 = self.player1.play_card(), self.player2.play_card()
            print(f"Player1: {c1.rank}{c1.suit}\tPlayer2: {c2.rank}{c2.suit}")
            pot = [c1, c2]

            if c1.rank == c2.rank:
                self._war(pot=pot, n=2)
            elif c1 > c2:
                self.player1.pickup(pot)
            elif c1 < c2:
                self.player2.pickup(pot)

            # every 200 hands shuffle each players stack, avoids non-converging game
            if self.cnt % 200 == 0:
                random.shuffle(self.player1.stack)
                random.shuffle(self.player2.stack)

        # print(f"player 1: {len(player1.stack)}\t player 2: {len(player2.stack)}")
        self._set_winner()

    def _set_winner(self):
        self.winner = self.player1 if len(self.player1.stack) > len(self.player2.stack) else self.player2

    def play(self) -> "War":
        self._gameloop()
        print(f"{self.winner.name} wins after {self.cnt} rounds!")
        return self

if __name__ == "__main__":

    war = War().play()