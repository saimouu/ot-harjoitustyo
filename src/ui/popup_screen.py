import pygame

from config import BACKGROUND_COLOR, BLOCK_SIZE, FONT_FILE_PATH, FONT_SIZE


class PopupScreen:
    """Base class for popup screens."""

    def __init__(self, header, buttons):
        """
        Class constructor.

        Args:
            header: Text displayed at the top of the popup.
            buttons (list): List of button objects shown in the popup.
        """
        self._rect = pygame.Rect(0, 0, BLOCK_SIZE * 3, BLOCK_SIZE * 3)

        self._font = pygame.font.Font(FONT_FILE_PATH, FONT_SIZE)
        self._header = header

        self._buttons = buttons

    def render(self, board):
        """Draws the popup screen on top of the game board.

        Args:
            board: Pygame surface where popup will be drawn.
        """
        board_w, board_h = board.get_size()
        self._rect.center = (board_w // 2, board_h // 2)

        text = self._font.render(str(self._header), True, (0, 0, 0))
        text_rect = text.get_rect(midtop=self._rect.midtop)
        text_rect.y += 10

        pygame.draw.rect(board, BACKGROUND_COLOR, self._rect, border_radius=10)
        board.blit(text, text_rect)

        for i, btn in enumerate(self._buttons):
            btn.rect.midbottom = self._rect.midbottom
            btn.rect.y = btn.rect.y - 10 - BLOCK_SIZE * i
            btn.render(board)

    def handle_event(self, event):
        """Handles button click events.

        Args:
            event: Pygame event.

        Returns:
            Result of the event according to the buttons command.
        """
        for btn in self._buttons:
            res = btn.handle_event(event)
            if res:
                return res
        return None
