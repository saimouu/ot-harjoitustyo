import copy
import unittest

from game.game_logic import GameLogic

BOARD_1 = [[0, 0, 0, 0], [2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
BOARD_2 = [[0, 2, 0, 0], [0, 2, 0, 0], [0, 2, 0, 0], [0, 2, 0, 0]]
BOARD_EMPTY = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
BOARD_GAME_OVER = [[8, 32, 2, 16], [2, 4, 8, 2], [8, 256, 64, 8], [2, 8, 4, 2]]


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()

    def test_move_left_merge_with_full_row(self):
        self.game.grid = copy.deepcopy(BOARD_1)

        self.game.move_all_blocks_left()
        expected = [[0, 0, 0, 0], [4, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(self.game.grid, expected)

    def test_move_right_merge_with_full_row(self):

        self.game.grid = copy.deepcopy(BOARD_1)

        self.game.move_all_blocks_right()
        expected = [[0, 0, 0, 0], [0, 0, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(self.game.grid, expected)

    def test_move_up_merge_with_full_column(self):

        self.game.grid = copy.deepcopy(BOARD_2)

        self.game.move_all_blocks_up()
        expected = [[0, 4, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(self.game.grid, expected)

    def test_move_down_merge_with_full_column(self):

        self.game.grid = copy.deepcopy(BOARD_2)

        self.game.move_all_blocks_down()
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 0, 0], [0, 4, 0, 0]]

        self.assertEqual(self.game.grid, expected)

    def test_empty_spaces_correct_with_no_blocks(self):
        self.game.grid = copy.deepcopy(BOARD_EMPTY)

        result = self.game._get_empty_spaces()
        expected = [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 0),
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
        ]
        self.assertEqual(result, expected)

    def test_empty_spaces_with_blocks(self):
        self.game.grid = copy.deepcopy(BOARD_1)

        result = self.game._get_empty_spaces()
        expected = [
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
            (2, 0),
            (2, 1),
            (2, 2),
            (2, 3),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
        ]
        self.assertEqual(result, expected)

    def test_game_over_no_moves_or_empty_spaces(self):
        self.game.grid = copy.deepcopy(BOARD_GAME_OVER)

        result = self.game.check_game_over()
        self.assertEqual(result, True)

    def test_game_over_with_vertical_moves_but_no_empty_spaces(self):
        self.game.grid = copy.deepcopy(BOARD_GAME_OVER)
        self.game._grid[3][2] = 2

        result = self.game.check_game_over()
        self.assertEqual(result, False)

    def test_game_over_with_horizontal_moves_but_no_empty_spaces(self):
        self.game.grid = copy.deepcopy(BOARD_GAME_OVER)
        self.game._grid[3][3] = 8

        result = self.game.check_game_over()
        self.assertEqual(result, False)

    def test_game_over_with_empty_spaces(self):
        self.game.grid = copy.deepcopy(BOARD_2)
        result = self.game.check_game_over()
        self.assertEqual(result, False)

    def test_check_win_with_2048(self):
        self.game.grid = copy.deepcopy(BOARD_1)
        self.game._grid[3][1] = 2048

        result = self.game.check_win()
        self.assertEqual(result, True)

    def test_check_win_without_2048(self):
        self.game.grid = copy.deepcopy(BOARD_1)

        result = self.game.check_win()
        self.assertEqual(result, False)

    def test_score_move_left(self):
        self.game.grid = copy.deepcopy(BOARD_1)
        self.game.move_all_blocks_left()

        self.assertEqual(self.game.score, 8)

    def test_score_nothing_to_move(self):
        self.game.grid = copy.deepcopy(BOARD_GAME_OVER)
        self.game.move_all_blocks_left()

        self.assertEqual(self.game.score, 0)

    def test_score_move_right(self):
        self.game.grid = copy.deepcopy(BOARD_1)
        self.game.move_all_blocks_left()

        self.assertEqual(self.game.score, 8)
