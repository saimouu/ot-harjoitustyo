import pygame

from config import FPS
from ui.win_screen import WinScreen


class GameLoop:
    def __init__(self, game, renderer, clock, event_queue):
        self._game = game
        self._renderer = renderer
        self._clock = clock
        self._event_queue = event_queue

        # self._running = True
        self._game_state = "playing"
        self._continue_pressed = False

        self._move_key_function = {
            pygame.K_LEFT: self._game.move_all_blocks_left,
            pygame.K_RIGHT: self._game.move_all_blocks_right,
            pygame.K_UP: self._game.move_all_blocks_up,
            pygame.K_DOWN: self._game.move_all_blocks_down,
        }

        self._screen_type = None

    def run(self):
        self._initialize_start()

        while True:
            if self._game_state == "playing":
                if self._handle_events() == False:
                    break
                self._render()

            elif self._game_state == "win":
                self._render_win_screen()
                if self._handle_win_screen_events() == False:
                    break

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

    def _handle_win_screen_events(self):
        if self._screen_type == None:
            raise ValueError("Screen type should not be None")

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            res = self._screen_type.handle_event(event)
            if res == "continue":
                self._continue_pressed = True
                self._game_state = "playing"
                self._screen_type = None
                return True
            elif res == "quit":
                return False

    def _handle_move_key_down(self, key):
        if key in self._move_key_function:
            self._move_key_function[key]()

            self._game.spawn_random_block()
            self._check_game_state()

    def _check_game_state(self):
        if self._game.check_win() and not self._continue_pressed:
            self._game_state = "win"
            self._screen_type = WinScreen()

        if self._game.check_game_over():
            print("You Lose!")  # Placeholder

    def _render(self):
        self._renderer.render()

    def _render_win_screen(self):
        self._renderer.render_win_screen(self._screen_type)
