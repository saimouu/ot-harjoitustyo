import unittest
from unittest.mock import Mock, patch

import pygame

from game.game_loop import GameLoop
from ui.lose_screen import LoseScreen
from ui.win_screen import WinScreen


class StubClock:
    def tick(self, fps):
        pass


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubRenderer:
    def render(self):
        pass


BOARD_1 = [[0, 0, 0, 0], [2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.game_mock = Mock()
        self.score_repo_mock = Mock()
        self.event_queue_mock = Mock()

    # patch fixes pygame.font not initialized error,
    #   which happens because GameLoop initializes popup classes
    @patch("pygame.font.Font")
    def test_shows_win_popup_when_condition_win_condition_is_true(self, font_mock):
        self.game_mock.check_win.return_value = True

        game_loop = GameLoop(
            self.game_mock,
            StubRenderer(),
            StubClock(),
            self.event_queue_mock,
            self.score_repo_mock,
        )

        game_loop._check_game_state()

        self.assertEqual(game_loop._game_state, "win")
        self.assertIsInstance(game_loop._popup, WinScreen)

    @patch("pygame.font.Font")
    def test_shows_lose_popup_when_condition_lose_condition_is_true(self, font_mock):
        self.game_mock.check_win.return_value = False
        self.game_mock.check_game_over.return_value = True

        game_loop = GameLoop(
            self.game_mock,
            StubRenderer(),
            StubClock(),
            self.event_queue_mock,
            self.score_repo_mock,
        )

        game_loop._check_game_state()

        self.assertEqual(game_loop._game_state, "lose")
        self.assertIsInstance(game_loop._popup, LoseScreen)

    @patch("pygame.font.Font")
    def test_key_left_event_calls_move_blocks_left(self, font_mock):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]  # quit key doesn't matter

        game_loop = GameLoop(
            self.game_mock,
            Mock(),
            StubClock(),
            StubEventQueue(events),
            self.score_repo_mock,
        )

        game_loop.run()

        self.game_mock.move_all_blocks_left.assert_called_once()

    @patch("pygame.font.Font")
    def test_key_left_event_calls_spawn_random_block(self, font_mock):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]  # quit key doesn't matter

        game_loop = GameLoop(
            self.game_mock,
            Mock(),
            StubClock(),
            StubEventQueue(events),
            self.score_repo_mock,
        )

        game_loop._handle_events()

        self.game_mock.spawn_random_block.assert_called_once()
