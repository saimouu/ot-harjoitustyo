import pygame

from config import BLOCK_SIZE, FONT_FILE_PATH, FONT_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from game.game_logic import GameLogic


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

    def _render_block(self, x, y, value):
        pass
        # text = self._font.render(str(value), True, (0, 0, 0))
