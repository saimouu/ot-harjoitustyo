import unittest
from unittest.mock import MagicMock, Mock, patch

from game.game_loop import GameLoop
from ui.high_scores_screen import HighScoreScreen
from ui.win_screen import WinScreen


# Tests events related to mouse button events when a button is clicked.
# The actual event is abstracted away using mocks, since the point is not
#   to test te ui.
# The tests make sure that the correct functions are called and that the
#   functions called, change the gamestate accordingly.
class TestButtonEventCall(unittest.TestCase):
    def setUp(self):
        self.game_mock = Mock()
        self.renderer_mock = Mock()
        self.clock_mock = Mock()
        self.event_queue_mock = Mock()
        self.score_repo_mock = Mock()

        self.game_loop = GameLoop(
            self.game_mock,
            self.renderer_mock,
            self.clock_mock,
            self.event_queue_mock,
            self.score_repo_mock,
        )

    def test_when_button_event_is_exit_on_exit_is_called(self):
        self.game_loop._on_exit = MagicMock()
        self.game_loop._handle_mouse_button_events("exit")

        self.game_loop._on_exit.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_exit_changes_game_state_to_playing(self, font_mock):
        self.game_loop._game_state = "score"
        self.game_loop._popup = HighScoreScreen(Mock())

        self.game_loop._on_exit()

        self.assertEqual(self.game_loop._game_state, "playing")
        self.assertEqual(self.game_loop._popup, None)

    def test_when_button_event_is_undo_on_undo_is_called(self):
        self.game_loop._on_undo = MagicMock()
        self.game_loop._handle_mouse_button_events("undo")

        self.game_loop._on_undo.assert_called_once()

    def test_on_undo_calls_restore_previous_grid(self):
        self.game_loop._on_undo()

        self.game_mock.restore_previous_grid.assert_called_once()

    def test_when_button_event_is_continue_on_continue_is_called(self):
        self.game_loop._on_continue = MagicMock()
        self.game_loop._handle_mouse_button_events("continue")

        self.game_loop._on_continue.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_continue_changes_game_state_to_playing(self, font_mock):
        self.game_loop._game_state = "win"
        self.game_loop._popup = WinScreen()

        self.game_loop._on_continue()

        self.assertEqual(self.game_loop._game_state, "playing")
        self.assertEqual(self.game_loop._popup, None)
        self.assertEqual(self.game_loop._continue_pressed, True)

    def test_when_button_event_is_quit_on_quit_is_called(self):
        self.game_loop._on_quit = MagicMock()
        self.game_loop._handle_mouse_button_events("quit")

        self.game_loop._on_quit.assert_called_once()

    def test_on_quit_calls_write_score(self):
        self.game_loop._write_score = MagicMock()

        self.game_loop._on_quit()
        self.game_loop._write_score.assert_called_once()

    def test_when_button_event_is_retry_on_retry_is_called(self):
        self.game_loop._on_retry = MagicMock()
        self.game_loop._handle_mouse_button_events("retry")

        self.game_loop._on_retry.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_retry_changes_game_state_to_playing(self, font_mock):
        self.game_loop._game_state = "win"
        self.game_loop._popup = WinScreen()

        self.game_loop._on_retry()

        self.assertEqual(self.game_loop._game_state, "playing")
        self.assertEqual(self.game_loop._popup, None)
        self.assertEqual(self.game_loop._continue_pressed, False)

    def test_on_retry_calls_reset_game(self):
        self.game_loop._on_retry()

        self.game_mock.reset_game.assert_called_once()

    def test_when_button_event_is_score_on_score_is_called(self):
        self.game_loop._on_score = MagicMock()
        self.game_loop._handle_mouse_button_events("score")

        self.game_loop._on_score.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_score_changes_game_state_to_score(self, font_mock):
        self.game_loop._on_score()

        self.assertEqual(self.game_loop._game_state, "score")
        self.assertIsInstance(self.game_loop._popup, HighScoreScreen)

    def test_when_button_event_is_arbitary_returns_true(self):
        self.game_loop._on_score = MagicMock()
        result = self.game_loop._handle_mouse_button_events("random")

        self.assertEqual(result, True)
