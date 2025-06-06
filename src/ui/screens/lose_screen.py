import pygame

from config import BLOCK_SIZE
from ui.common.button import Button
from ui.screens.popup_screen import PopupScreen


class LoseScreen(PopupScreen):
    """Lose screen popup class."""

    def __init__(self):
        buttons = [
            Button(
                "Retry",
                pygame.Rect(0, 0, BLOCK_SIZE * 1.5, BLOCK_SIZE * 0.75),
                self._handle_retry,
            ),
            Button(
                "Quit",
                pygame.Rect(0, 0, BLOCK_SIZE * 1.5, BLOCK_SIZE * 0.75),
                self._handle_quit,
            ),
        ]
        super().__init__("Game Over!", buttons)

    def _handle_retry(self):
        return "retry"

    def _handle_quit(self):
        return "quit"
