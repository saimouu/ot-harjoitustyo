import pygame

from config import BACKGROUND_COLOR, BLOCK_SIZE, FONT_FILE_PATH, FONT_SIZE


class PopupScreen:
    def __init__(self, header, buttons):
        self._rect = pygame.Rect(0, 0, BLOCK_SIZE * 3, BLOCK_SIZE * 3)

        self._font = pygame.font.Font(FONT_FILE_PATH, FONT_SIZE)
        self._header = header

        self._buttons = buttons

    def render(self, board):
        board_w, board_h = board.get_size()
        self._rect.center = (board_w // 2, board_h // 2)

        text = self._font.render(str("You Win!"), True, (0, 0, 0))
        text_rect = text.get_rect(midtop=self._rect.midtop)
        text_rect.y += 10

        pygame.draw.rect(board, BACKGROUND_COLOR, self._rect, border_radius=10)
        board.blit(text, text_rect)

        for i, btn in enumerate(self._buttons):
            btn.rect.midbottom = self._rect.midbottom
            btn.rect.y = btn.rect.y - 10 - BLOCK_SIZE * i
            btn.render(board)

    def handle_event(self, event):
        for btn in self._buttons:
            res = btn.handle_event(event)
            if res:
                return res
        return None
