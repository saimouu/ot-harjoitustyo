from config import FPS


class GameLoop:
    """Class that manages the main loop of the game."""

    def __init__(self, renderer, clock, event_queue, event_handler):
        """Class constructor

        Args:
            renderer: Renderer object responsible for drawing the game on the screen.
            clock: Clock object that controls the frame rate.
            event_queue: Object used to retrieve user input events.
            event_handler: Object that handles user input events.
        """
        self._renderer = renderer
        self._clock = clock
        self._event_queue = event_queue
        self._event_handler = event_handler

    def run(self):
        """Main run function which starts the game, and runs in a infinite loop.

        Loop stops if the event_handler returns False.
        """
        self._event_handler.initialize_start()

        while True:
            self._render(self._event_handler.popup)
            events = self._event_queue.get()
            state = self._event_handler.state

            if state == "playing":
                if self._event_handler.handle_events(events) is False:
                    break
            elif self._event_handler.handle_popup_events(events) is False:
                break

            self._clock.tick(FPS)

    def _render(self, popup=None):
        """Calls the renderer which renders the game.

        Args:
            popup: PopupScreen object which the renderer displays if popup is not None.
        """
        self._renderer.render(popup)
