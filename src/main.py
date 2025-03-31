import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from game.clock import Clock
from game.game_logic import GameLogic
from game.game_loop import GameLoop
from ui.render import Renderer


def main():
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2048")

    pygame.init()

    game = GameLogic()
    renderer = Renderer(display, game)
    clock = Clock()

    game_loop = GameLoop(game, renderer, clock)

    game_loop.run()


if __name__ == "__main__":
    main()
