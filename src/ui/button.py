import pygame

from config import (
    BLOCK_SIZE,
    BOARD_COLOR,
    BUTTON_FONT_SIZE,
    FONT_FILE_PATH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Button:
    def __init__(self, text, rect, command):
        self._text = text
        self.rect = rect
        self._font = pygame.font.Font(FONT_FILE_PATH, BUTTON_FONT_SIZE)
        self._command = command

    def render(self, board):
        text = self._font.render(str(self._text), True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        pygame.draw.rect(board, BOARD_COLOR, self.rect, border_radius=10)
        board.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            board_position = self._relative_position(event.pos)
            if self.rect.collidepoint(board_position):
                return self._command()
        return None

    # quick fix to get the correct positions relative to the surface
    def _relative_position(self, screen_position):
        board_x = (SCREEN_WIDTH - BLOCK_SIZE * 4) / 2
        board_y = (SCREEN_HEIGHT - BLOCK_SIZE * 4) / 2

        return (screen_position[0] - board_x, screen_position[1] - board_y)
