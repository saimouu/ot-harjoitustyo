import unittest

import pygame

from game.game_logic import GameLogic
from game.game_loop import GameLoop


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


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        pass
