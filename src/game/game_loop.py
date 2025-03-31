import pygame

from config import FPS


class GameLoop:
    def __init__(self, game, renderer, clock, event_queue):
        self._game = game
        self._renderer = renderer
        self._clock = clock
        self._event_queue = event_queue

        self._running = True

        self._move_key_function = {
            pygame.K_LEFT: self._game.move_all_blocks_left,
            pygame.K_RIGHT: self._game.move_all_blocks_right,
            pygame.K_UP: self._game.move_all_blocks_up,
            pygame.K_DOWN: self._game.move_all_blocks_down,
        }

    def run(self):
        self._initialize_start()

        while self._running:
            if self._handle_events() == False:
                break

            self._render()
            self._clock.tick(FPS)

    def _initialize_start(self):
        self._game.spawn_random_block()
        self._game.spawn_random_block()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                self._handle_move_key_down(event.key)

    def _handle_move_key_down(self, key):
        if key in self._move_key_function:
            self._move_key_function[key]()

            self._game.spawn_random_block()
            self._check_game_state()

    def _check_game_state(self):
        if self._game.check_win():
            print("You Win!")  # Placeholder
            self._running = False

        if self._game.check_game_over():
            print("You Lose!")  # Placeholder
            self._running = False

    def _render(self):
        self._renderer.render()
