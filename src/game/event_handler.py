import pygame

from ui.high_scores_screen import HighScoreScreen
from ui.info_screen import InfoScreen
from ui.lose_screen import LoseScreen
from ui.win_screen import WinScreen


class EventHandler:
    def __init__(self, game, renderer, score_repository):
        self._game = game
        self._renderer = renderer
        self._score_repository = score_repository

        self._state = "playing"
        self._continue_pressed = False
        self._popup = None

        self._move_key_function = {
            pygame.K_LEFT: self._game.move_all_blocks_left,
            pygame.K_RIGHT: self._game.move_all_blocks_right,
            pygame.K_UP: self._game.move_all_blocks_up,
            pygame.K_DOWN: self._game.move_all_blocks_down,
        }

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                self._handle_move_key_down(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                result = self._renderer.handle_button_events(event)
                if not self._handle_button_event(result):
                    return False
        return True

    def handle_popup_events(self, events):
        if self._popup is None:
            raise ValueError("Screen type should not be None")

        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                result = self._popup.handle_event(event)
                if not self._handle_button_event(result):
                    return False
        return True

    def _handle_button_event(self, result):
        match result:
            case "exit":
                self._on_exit()
            case "score":
                self._on_score()
            case "undo":
                self._on_undo()
            case "continue":
                self._on_continue()
            case "quit":
                self._on_quit()
                return False
            case "retry":
                self._on_retry()
            case "info":
                self._on_info()
            case _:
                pass
        return True

    def _on_info(self):
        self._popup = InfoScreen()
        self._state = "info"

    def _on_score(self):
        self._popup = HighScoreScreen(self._score_repository)
        self._state = "score"

    def _on_undo(self):
        self._game.restore_previous_grid()

    def _on_quit(self):
        self._write_score()

    def _on_exit(self):
        self._popup = None
        self._state = "playing"

    def _on_retry(self):
        self._write_score()
        self._game.reset_game()
        self._state = "playing"
        self._popup = None
        self._continue_pressed = False

    def _on_continue(self):
        self._continue_pressed = True
        self._state = "playing"
        self._popup = None

    def _handle_move_key_down(self, key):
        if key in self._move_key_function:
            self._move_key_function[key]()
            if self._game.check_any_block_moved():
                self._game.spawn_random_block()
            self._check_state()

    def _check_state(self):
        if self._game.check_win() and not self._continue_pressed:
            self._state = "win"
            self._popup = WinScreen()
        elif self._game.check_game_over():
            self._state = "lose"
            self._popup = LoseScreen()

    def _write_score(self):
        self._score_repository.write_score(
            self._game.score, self._game.get_max_block(), self._game.moves
        )

    @property
    def popup(self):
        return self._popup

    @property
    def state(self):
        return self._state
