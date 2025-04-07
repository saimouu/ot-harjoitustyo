import pygame

from config import BACKGROUND_COLOR, BLOCK_SIZE, FONT_FILE_PATH, FONT_SIZE
from ui.button import Button


class WinScreen:
    def __init__(self):
        self._rect = pygame.Rect(0, 0, BLOCK_SIZE * 3, BLOCK_SIZE * 3)

        self._font = pygame.font.Font(FONT_FILE_PATH, FONT_SIZE)

        self._buttons = []

        self._continue_btn = Button(
            "Continue",
            pygame.Rect(0, 0, BLOCK_SIZE * 1.5, BLOCK_SIZE),
            self._handle_continue,
        )
        self._quit_btn = Button(
            "Quit",
            pygame.Rect(0, 0, BLOCK_SIZE * 1.5, BLOCK_SIZE),
            self._handle_quit,
        )

        self._buttons.append(self._continue_btn)
        self._buttons.append(self._quit_btn)

    def render(self, board):
        board_w, board_h = board.get_size()
        self._rect.center = (board_w // 2, board_h // 2)

        text = self._font.render(str("You Win!"), True, (0, 0, 0))
        text_rect = text.get_rect(midtop=self._rect.midtop)
        text_rect.y += 10

        pygame.draw.rect(board, BACKGROUND_COLOR, self._rect, border_radius=10)
        board.blit(text, text_rect)

        self._quit_btn.rect.midbottom = self._rect.midbottom
        self._quit_btn.rect.y -= 10
        self._quit_btn.render(board)

        self._continue_btn.rect.midbottom = self._rect.midbottom
        self._continue_btn.rect.y -= BLOCK_SIZE + 20
        self._continue_btn.render(board)

    def handle_event(self, event):
        for btn in self._buttons:
            res = btn.handle_event(event)
            if res:
                return res
        return None

    def _handle_continue(self):
        return "continue"

    def _handle_quit(self):
        return "quit"
