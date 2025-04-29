import unittest
from unittest.mock import Mock, patch

import pygame

from game.event_handler import EventHandler


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class TestEventHandler(unittest.TestCase):
    def setUp(self):
        self.game_mock = Mock()
        self.renderer_mock = Mock()
        self.clock_mock = Mock()
        self.event_queue_mock = Mock()
        self.score_repo_mock = Mock()

        self.event_handler = EventHandler(
            self.game_mock,
            self.renderer_mock,
            self.score_repo_mock,
        )

    @patch("pygame.font.Font")
    def test_key_left_event_calls_spawn_random_block(self, font_mock):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]  # quit key doesn't matter

        self.event_handler.handle_events(events)

        self.game_mock.spawn_random_block.assert_called_once()

    @patch("pygame.font.Font")
    def test_non_arrow_key_doesnt_spawn_random_block(self, font_mock):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_u),
            StubEvent(pygame.QUIT, pygame.K_0),
        ]  # quit key doesn't matter

        self.event_handler.handle_events(events)

        self.game_mock.spawn_random_block.assert_not_called()
