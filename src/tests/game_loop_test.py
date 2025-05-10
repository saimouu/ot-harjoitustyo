import unittest
from unittest.mock import Mock, patch

import pygame

from game.event_handler import EventHandler
from game.game_logic import GameLogic
from game.game_loop import GameLoop
from ui.screens.lose_screen import LoseScreen
from ui.screens.win_screen import WinScreen


class StubClock:
    def tick(self, fps):
        pass


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self, popup=None):
        pass


# The block positions cannot be easily changed/initialized since game_loop initializes
# the grid when run() is called. So conditions are mainly simulated by mocking return values.
class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()

        self.renderer = StubRenderer()
        self.clock = StubClock()

        self.event_handler = EventHandler(self.game, self.renderer, Mock())

    def test_right_arrow_key_moves_blocks(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]

        game_loop = GameLoop(
            self.renderer, self.clock, StubEventQueue(events), self.event_handler
        )

        game_loop.run()

        self.assertEqual(self.game.check_any_block_moved(), True)

    @patch("pygame.font.Font")
    def test_shows_win_popup_when_win_condition_is_true(self, font_mock):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]

        self.game.check_win = Mock(return_value=True)  # simulates win

        game_loop = GameLoop(
            self.renderer, self.clock, StubEventQueue(events), self.event_handler
        )

        game_loop.run()

        self.assertEqual(self.event_handler.state, "win")
        self.assertIsInstance(self.event_handler.popup, WinScreen)

    @patch("pygame.font.Font")
    def test_shows_lose_popup_when_game_is_over(self, font_mock):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]

        self.game.check_game_over = Mock(return_value=True)  # simulates lose

        game_loop = GameLoop(
            self.renderer, self.clock, StubEventQueue(events), self.event_handler
        )

        game_loop.run()

        self.assertEqual(self.event_handler.state, "lose")
        self.assertIsInstance(self.event_handler.popup, LoseScreen)

    @patch("pygame.font.Font")
    def test_clicking_exit_on_scores_popup_closes_the_popup(self, font_mock):
        events = [
            StubEvent(pygame.MOUSEBUTTONDOWN, 1),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]

        mock_popup = Mock()
        mock_popup.handle_event.return_value = "exit"

        self.event_handler._popup = mock_popup
        self.event_handler._state = "score"

        game_loop = GameLoop(
            self.renderer, self.clock, StubEventQueue(events), self.event_handler
        )

        game_loop.run()

        self.assertEqual(self.event_handler.state, "playing")
        self.assertEqual(self.event_handler.popup, None)
