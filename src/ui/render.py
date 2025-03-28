import pygame

from config import BLOCK_SIZE, FONT_FILE_PATH, FONT_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH


class Renderer:
    def __init__(self, display, game):
        self._display = display
        self._game = game

        self._font = pygame.font.Font(FONT_FILE_PATH, FONT_SIZE)

        self._board = self._init_board()

        # For centering the board surface
        self._center_width_correction = (SCREEN_WIDTH - BLOCK_SIZE * 4) / 2
        self._center_height_correction = (SCREEN_HEIGHT - BLOCK_SIZE * 4) / 2

    def render(self):
        self._display.fill((173, 163, 160))
        self._display.blit(
            self._board, (self._center_width_correction, self._center_height_correction)
        )
        self._render_all_blocks()

    def _init_board(self):
        board = pygame.Surface((BLOCK_SIZE * 4, BLOCK_SIZE * 4))
        board.fill((94, 79, 74))  # TODO: change later
        for x in range(4):
            for y in range(4):
                rect = pygame.Rect(
                    x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                )
                pygame.draw.rect(board, (36, 30, 28), rect, 5)
        return board

    def _render_block(self, x, y, row, col):
        value = self._game.get_block_value(row, col)
        if value == 0:
            return

        rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        text = self._font.render(str(value), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)

        pygame.draw.rect(self._board, (217, 118, 26), rect)
        self._board.blit(text, text_rect)

    def _render_all_blocks(self):
        # TODO: board values and visual values are not the same
        for x in range(4):
            for y in range(4):
                self._render_block(x, y, y, x)
