from longest_word.game import Game
import string
# tests/test_game.py
class TestGame:
    def test_game_initialization(self):
            # setup
        game = Game()
            # exercise
        grid = game.grid
            # verify
        assert type(grid) == list
        assert len(grid) == 9

        for letter in grid:
            assert letter in string.ascii_uppercase
            # teardown
