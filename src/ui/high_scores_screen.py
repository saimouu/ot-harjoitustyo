import pygame

from config import BACKGROUND_COLOR, BLOCK_SIZE, BUTTON_FONT_SIZE, FONT_FILE_PATH
from ui.button import Button
from ui.popup_screen import PopupScreen


class HighScoreScreen(PopupScreen):
    def __init__(self, score_repository):
        self._score_repository = score_repository
        self._rect = pygame.Rect(0, 0, BLOCK_SIZE * 3, BLOCK_SIZE * 4)
        self._score_font = pygame.font.Font(FONT_FILE_PATH, BUTTON_FONT_SIZE)

        buttons = [
            Button(
                "Exit",
                pygame.Rect(0, 0, BLOCK_SIZE * 0.75, BLOCK_SIZE * 0.5),
                self._handle_exit,
            ),
        ]
        super().__init__("High Scores", buttons)

    def render(self, board):
        board_w, board_h = board.get_size()
        self._rect.center = (board_w // 2, board_h // 2)

        text = self._font.render(str(self._header), True, (0, 0, 0))
        text_rect = text.get_rect(midtop=self._rect.midtop)
        text_rect.y += 10

        pygame.draw.rect(board, BACKGROUND_COLOR, self._rect, border_radius=10)
        board.blit(text, text_rect)

        high_scores = self._score_repository.get_top_5()
        for i, score in enumerate(high_scores):
            score_text = self._score_font.render(f"{i+1}. {score}", True, (0, 0, 0))
            score_rect = score_text.get_rect()
            score_rect.midtop = (
                self._rect.centerx,
                text_rect.bottom + 10 + i * (score_rect.height + 5),
            )
            board.blit(score_text, score_rect)

        for i, btn in enumerate(self._buttons):
            btn.rect.midbottom = self._rect.midbottom
            btn.rect.y = btn.rect.y - 10 - BLOCK_SIZE * i
            btn.render(board)

    def _handle_exit(self):
        return "exit"
