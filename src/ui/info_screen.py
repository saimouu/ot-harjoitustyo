import pygame

from config import BACKGROUND_COLOR, BLOCK_SIZE, FONT_FILE_PATH, TEXT_FONT_SIZE
from ui.button import Button
from ui.popup_screen import PopupScreen


class InfoScreen(PopupScreen):
    def __init__(self):
        self._info_text_font = pygame.font.Font(FONT_FILE_PATH, TEXT_FONT_SIZE)

        buttons = [
            Button(
                "Exit",
                pygame.Rect(0, 0, BLOCK_SIZE * 1.5, BLOCK_SIZE * 0.75),
                lambda: "exit",
            ),
        ]
        super().__init__("Info", buttons)

        self._rect = pygame.Rect(0, 0, BLOCK_SIZE * 3.5, BLOCK_SIZE * 3.5)

    def render(self, board):
        board_w, board_h = board.get_size()
        self._rect.center = (board_w // 2, board_h // 2)

        header = self._font.render(str(self._header), True, (0, 0, 0))
        header_rect = header.get_rect(midtop=self._rect.midtop)
        header_rect.y += 10

        pygame.draw.rect(board, BACKGROUND_COLOR, self._rect, border_radius=10)
        board.blit(header, header_rect)

        lines = [
            "Use arrow keys to slide blocks",
            "You can undo two times in a game",
            "Score will be saved on quit or retry",
        ]

        for i, line in enumerate(lines):
            info_text = self._info_text_font.render(line, True, (0, 0, 0))
            info_rect = info_text.get_rect(midtop=header_rect.midtop)
            info_rect.y += 50 + i * TEXT_FONT_SIZE
            board.blit(info_text, info_rect)

        for i, btn in enumerate(self._buttons):
            btn.rect.midbottom = self._rect.midbottom
            btn.rect.y = btn.rect.y - 10 - BLOCK_SIZE * i
            btn.render(board)
