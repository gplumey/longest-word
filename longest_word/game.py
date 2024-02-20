# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False

        if len(word)> 0:
            copy = self.grid.copy()
            for letter in word:
                if letter in copy:
                    copy.remove(letter)
                else:
                    return False
            return True

        return False
