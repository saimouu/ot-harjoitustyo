import pygame

from ui.screens.high_scores_screen import HighScoreScreen
from ui.screens.info_screen import InfoScreen
from ui.screens.lose_screen import LoseScreen
from ui.screens.win_screen import WinScreen


class EventHandler:
    """Class that handles user events.

    Attributes:
        game: Core game logic object.
        renderer: Renderer object responsible for drawing the game on the screen.
        score_repository: Object responsible for writing and getting scores from a file.
        state: Keeps track of the current screen.
        continue_pressed: Keeps track if continue has been pressed in win screen.
        popup: Stores the current popup screen.
        move_key_function: Maps the arrow keys to appropriate move functions.
    """

    def __init__(self, game, renderer, score_repository):
        """Class constructor.

        Args:
            game: Core game logic object.
            renderer: Renderer object responsible for drawing the game on the screen.
            score_repository: Object responsible for writing and getting scores from a file.
        """
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
        """Handles the main screen events.

        Args:
            events (list[event]): List of events.

        Returns:
            bool: False if event is QUIT or user quits the game, True otherwise.
        """
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
        """Handles the popup screen events.

        Args:
            events (list[event]): List of events.

        Returns:
            bool: False if event is QUIT or user quits the game, True otherwise.
        """
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
        """Matches button event result to appropriate function.

        If no match is found state doesn't change and returns True.

        Args:
            result (str): Returned result from button event.

        Returns:
            False if result is quit, True otherwise.
        """
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
        """Sets popup to InfoScreen and updates game state to 'info'."""
        self._popup = InfoScreen()
        self._state = "info"

    def _on_score(self):
        """Sets popup to HighScoreScreen and updates game state to 'score'."""
        self._popup = HighScoreScreen(self._score_repository)
        self._state = "score"

    def _on_undo(self):
        """Restores the previous game grid if there are undos left."""
        self._game.restore_previous_grid()

    def _on_quit(self):
        """Writes score to file."""
        self._write_score()

    def _on_exit(self):
        """Closes the currently displayed popup and sets state to 'playing'"""
        self._popup = None
        self._state = "playing"

    def _on_retry(self):
        """Resets the game.

        Writes score and restores default values.

        """
        self._write_score()
        self._game.reset_game()
        self._state = "playing"
        self._popup = None
        self._continue_pressed = False

    def _on_continue(self):
        """Continues the game even though win condition is met."""
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
        """Checks win and lose conditions and changes state and popup accordingly."""
        if self._game.check_win() and not self._continue_pressed:
            self._state = "win"
            self._popup = WinScreen()
        elif self._game.check_game_over():
            self._state = "lose"
            self._popup = LoseScreen()

    def _write_score(self):
        """Writes the current game score, largest block and move count to file."""
        self._score_repository.write_score(
            self._game.score, self._game.get_max_block(), self._game.moves
        )

    def initialize_start(self):
        """Initializes the first two blocks to random positions.

        Called only once at the startup of the game.

        """
        self._game.spawn_random_block()
        self._game.spawn_random_block()

    @property
    def popup(self):
        return self._popup

    @property
    def state(self):
        return self._state
