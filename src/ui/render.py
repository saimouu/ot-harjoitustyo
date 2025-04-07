import pygame

from config import (
    BACKGROUND_COLOR,
    BLOCK_COLORS,
    BLOCK_SIZE,
    BOARD_COLOR,
    FONT_FILE_PATH,
    FONT_SIZE,
    OUTLINE_COLOR,
    OUTLINE_THICKNESS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Renderer:
    def __init__(self, display, game):
        self._display = display
        self._game = game

        self._font = pygame.font.Font(FONT_FILE_PATH, FONT_SIZE)

        # For centering the board surface
        self._center_width_correction = (SCREEN_WIDTH - BLOCK_SIZE * 4) / 2
        self._center_height_correction = (SCREEN_HEIGHT - BLOCK_SIZE * 4) / 2

    def render(self, popup=None):
        self._display.fill(BACKGROUND_COLOR)

        board = self._get_board()
        self._render_all_blocks(board)

        if popup:
            popup.render(board)

        self._display.blit(
            board,
            (self._center_width_correction, self._center_height_correction),
        )
        self._render_score_text()

        pygame.display.update()

    def _render_score_text(self):
        bg_width = 150
        bg_height = 70

        score_text = self._font.render(str(self._game.score), True, (0, 0, 0))
        score_rect = score_text.get_rect()

        bg_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - bg_width // 2,
            BLOCK_SIZE - bg_height // 2,
            bg_width,
            bg_height,
        )

        pygame.draw.rect(self._display, BOARD_COLOR, bg_rect, border_radius=10)
        score_rect.center = bg_rect.center
        self._display.blit(score_text, score_rect)

    def _get_board(self):
        board = pygame.Surface(
            (
                BLOCK_SIZE * 4,
                BLOCK_SIZE * 4,
            )
        )
        board.fill(BOARD_COLOR)
        for i in range(5):
            pygame.draw.line(
                board,
                OUTLINE_COLOR,
                (0, i * BLOCK_SIZE),
                (BLOCK_SIZE * 4, i * BLOCK_SIZE),
                OUTLINE_THICKNESS,
            )
            pygame.draw.line(
                board,
                OUTLINE_COLOR,
                (i * BLOCK_SIZE, 0),
                (i * BLOCK_SIZE, BLOCK_SIZE * 4),
                OUTLINE_THICKNESS,
            )

        return board

    def _render_block(self, x, y, row, col, board):
        value = self._game.get_block_value(row, col)
        if value == 0:
            return

        color = BLOCK_COLORS[value] if value <= 2048 else BLOCK_COLORS[2048]

        rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        text = self._font.render(str(value), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)

        pygame.draw.rect(board, color, rect, border_radius=10)
        board.blit(text, text_rect)

    def _render_all_blocks(self, board):
        for x in range(4):
            for y in range(4):
                self._render_block(x, y, y, x, board)
