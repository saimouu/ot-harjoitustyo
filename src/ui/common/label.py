import pygame

from config import BUTTON_FONT_SIZE, FONT_FILE_PATH


class Label:
    def __init__(self, get_text, rect):
        self._get_text = get_text
        self.rect = rect
        self._font = pygame.font.Font(FONT_FILE_PATH, BUTTON_FONT_SIZE)

    def render(self, board):
        text = self._font.render(str(self._get_text()), True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        board.blit(text, text_rect)
