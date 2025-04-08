import pygame

from config import BLOCK_SIZE
from ui.button import Button
from ui.popup_screen import PopupScreen


class LoseScreen(PopupScreen):
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
        super().__init__("You Lose!", buttons)

    def _handle_retry(self):
        return "retry"

    def _handle_quit(self):
        return "quit"
