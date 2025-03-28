import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from game.game_logic import GameLogic
from ui.render import Renderer


def main():
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2048")

    pygame.init()

    game = GameLogic()
    renderer = Renderer(display, game)

    clock = pygame.time.Clock()

    # Delete
    game._grid[0][0] = 2
    game._grid[2][3] = 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        renderer.render()
        pygame.display.update()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
