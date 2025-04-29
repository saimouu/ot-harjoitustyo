import unittest
from unittest.mock import MagicMock, Mock, patch

from game.event_handler import EventHandler
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

        self.event_handler = EventHandler(
            self.game_mock,
            self.renderer_mock,
            self.score_repo_mock,
        )

    def test_when_button_event_is_exit_on_exit_is_called(self):
        self.event_handler._on_exit = MagicMock()
        self.event_handler._handle_button_event("exit")

        self.event_handler._on_exit.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_exit_changesstate_to_playing(self, font_mock):
        self.event_handler._state = "score"
        self.event_handler._popup = HighScoreScreen(Mock())

        self.event_handler._on_exit()

        self.assertEqual(self.event_handler.state, "playing")
        self.assertEqual(self.event_handler._popup, None)

    def test_when_button_event_is_undo_on_undo_is_called(self):
        self.event_handler._on_undo = MagicMock()
        self.event_handler._handle_button_event("undo")

        self.event_handler._on_undo.assert_called_once()

    def test_on_undo_calls_restore_previous_grid(self):
        self.event_handler._on_undo()

        self.game_mock.restore_previous_grid.assert_called_once()

    def test_when_button_event_is_continue_on_continue_is_called(self):
        self.event_handler._on_continue = MagicMock()
        self.event_handler._handle_button_event("continue")

        self.event_handler._on_continue.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_continue_changesstate_to_playing(self, font_mock):
        self.event_handler._state = "win"
        self.event_handler._popup = WinScreen()

        self.event_handler._on_continue()

        self.assertEqual(self.event_handler.state, "playing")
        self.assertEqual(self.event_handler._popup, None)
        self.assertEqual(self.event_handler._continue_pressed, True)

    def test_when_button_event_is_quit_on_quit_is_called(self):
        self.event_handler._on_quit = MagicMock()
        self.event_handler._handle_button_event("quit")

        self.event_handler._on_quit.assert_called_once()

    def test_on_quit_calls_write_score(self):
        self.event_handler._write_score = MagicMock()

        self.event_handler._on_quit()
        self.event_handler._write_score.assert_called_once()

    def test_when_button_event_is_retry_on_retry_is_called(self):
        self.event_handler._on_retry = MagicMock()
        self.event_handler._handle_button_event("retry")

        self.event_handler._on_retry.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_retry_changesstate_to_playing(self, font_mock):
        self.event_handler._state = "win"
        self.event_handler._popup = WinScreen()

        self.event_handler._on_retry()

        self.assertEqual(self.event_handler.state, "playing")
        self.assertEqual(self.event_handler._popup, None)
        self.assertEqual(self.event_handler._continue_pressed, False)

    def test_on_retry_calls_reset_game(self):
        self.event_handler._on_retry()

        self.game_mock.reset_game.assert_called_once()

    def test_when_button_event_is_score_on_score_is_called(self):
        self.event_handler._on_score = MagicMock()
        self.event_handler._handle_button_event("score")

        self.event_handler._on_score.assert_called_once()

    @patch("pygame.font.Font")
    def test_on_score_changesstate_to_score(self, font_mock):
        self.event_handler._on_score()

        self.assertEqual(self.event_handler.state, "score")
        self.assertIsInstance(self.event_handler._popup, HighScoreScreen)

    def test_when_button_event_is_arbitary_returns_true(self):
        self.event_handler._on_score = MagicMock()
        result = self.event_handler._handle_button_event("random")

        self.assertEqual(result, True)
