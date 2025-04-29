import pygame

from config import BLOCK_SIZE
from ui.button import Button
from ui.popup_screen import PopupScreen


class WinScreen(PopupScreen):
    """Info screen popup class."""

    def __init__(self):
        buttons = [
            Button(
                "Continue",
                pygame.Rect(0, 0, BLOCK_SIZE * 1.5, BLOCK_SIZE * 0.75),
                self._handle_continue,
            ),
            Button(
                "Quit",
                pygame.Rect(0, 0, BLOCK_SIZE * 1.5, BLOCK_SIZE * 0.75),
                self._handle_quit,
            ),
        ]
        super().__init__("You Win!", buttons)

    def _handle_continue(self):
        return "continue"

    def _handle_quit(self):
        return "quit"
