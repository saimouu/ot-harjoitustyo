import pygame

from config import FPS
from ui.high_scores_screen import HighScoreScreen
from ui.lose_screen import LoseScreen
from ui.win_screen import WinScreen


class GameLoop:
    def __init__(self, game, renderer, clock, event_queue, score_repository):
        self._game = game
        self._renderer = renderer
        self._clock = clock
        self._event_queue = event_queue
        self._score_repository = score_repository

        self._game_state = "playing"
        self._continue_pressed = False

        self._move_key_function = {
            pygame.K_LEFT: self._game.move_all_blocks_left,
            pygame.K_RIGHT: self._game.move_all_blocks_right,
            pygame.K_UP: self._game.move_all_blocks_up,
            pygame.K_DOWN: self._game.move_all_blocks_down,
        }

        self._popup = None

    def run(self):
        self._initialize_start()

        while True:
            self._render(self._popup)
            if self._game_state == "playing":
                if self._handle_events() is False:
                    break
            elif self._handle_popup_events() is False:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                res = self._renderer.handle_button_events(event)
                if res == "score":
                    self._popup = HighScoreScreen(self._score_repository)
                    self._game_state = "score"
                elif res == "undo":
                    self._on_undo()

        return True

    def _handle_popup_events(self):
        if self._popup is None:
            raise ValueError("Screen type should not be None")

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                result = self._popup.handle_event(event)
                match result:
                    case "exit":
                        self._on_exit()
                    case "continue":
                        self._on_continue()
                    case "quit":
                        self._on_quit()
                        return False
                    case "retry":
                        self._on_retry()
                    case _:
                        pass
        return True

    def _on_undo(self):
        self._game.restore_previous_grid()

    def _on_quit(self):
        self._write_score()

    def _on_exit(self):
        self._popup = None
        self._game_state = "playing"

    def _on_retry(self):
        self._write_score()
        self._game.reset_game()
        self._game_state = "playing"
        self._popup = None
        self._continue_pressed = False

    def _on_continue(self):
        self._continue_pressed = True
        self._game_state = "playing"
        self._popup = None

    # TODO: fix bug where a new block is spawned even though no blocks moved
    def _handle_move_key_down(self, key):
        if key in self._move_key_function:
            self._move_key_function[key]()

            self._game.spawn_random_block()
            self._check_game_state()

    def _check_game_state(self):
        if self._game.check_win() and not self._continue_pressed:
            self._game_state = "win"
            self._popup = WinScreen()
        elif self._game.check_game_over():
            self._game_state = "lose"
            self._popup = LoseScreen()

    def _render(self, popup=None):
        self._renderer.render(popup)

    def _write_score(self):
        self._score_repository.write_score([[self._game.score]])
