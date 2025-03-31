import copy
import unittest

from game.game_logic import GameLogic

BOARD_1 = [[0, 0, 0, 0], [2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
BOARD_2 = [[0, 2, 0, 0], [0, 2, 0, 0], [0, 2, 0, 0], [0, 2, 0, 0]]


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        pass

    def test_move_left_merge_with_full_row(self):
        game = GameLogic()
        game.grid = copy.deepcopy(BOARD_1)

        game.move_all_blocks_left()
        expected = [[0, 0, 0, 0], [4, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(game.grid, expected)

    def test_move_right_merge_with_full_row(self):
        game = GameLogic()

        game.grid = copy.deepcopy(BOARD_1)

        game.move_all_blocks_right()
        expected = [[0, 0, 0, 0], [0, 0, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(game.grid, expected)

    def test_move_up_merge_with_full_column(self):
        game = GameLogic()

        game.grid = copy.deepcopy(BOARD_2)

        game.move_all_blocks_up()
        expected = [[0, 4, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(game.grid, expected)

    def test_move_down_merge_with_full_column(self):
        game = GameLogic()

        game.grid = copy.deepcopy(BOARD_2)

        game.move_all_blocks_down()
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 0, 0], [0, 4, 0, 0]]

        self.assertEqual(game.grid, expected)
