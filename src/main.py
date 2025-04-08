import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from game.clock import Clock
from game.event_queue import EventQueue
from game.game_logic import GameLogic
from game.game_loop import GameLoop
from repositories.score_repository import ScoreRepository
from ui.render import Renderer


def main():
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2048")

    # pylint: disable=no-member
    pygame.init()

    game = GameLogic()
    renderer = Renderer(display, game)
    clock = Clock()
    event_queue = EventQueue()
    score_repository = ScoreRepository()

    game_loop = GameLoop(game, renderer, clock, event_queue, score_repository)

    game_loop.run()


if __name__ == "__main__":
    main()
