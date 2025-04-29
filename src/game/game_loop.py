from config import FPS


class GameLoop:
    def __init__(self, game, renderer, clock, event_queue, event_handler):
        self._game = game
        self._renderer = renderer
        self._clock = clock
        self._event_queue = event_queue
        self._event_handler = event_handler

    def run(self):
        self._initialize_start()

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

    def _initialize_start(self):
        self._game.spawn_random_block()
        self._game.spawn_random_block()

    def _render(self, popup=None):
        self._renderer.render(popup)
