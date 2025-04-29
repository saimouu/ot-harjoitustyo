import pygame


class EventQueue:
    """Class responsible for getting pygame user events."""

    def __init__(self):
        pass

    def get(self):
        """Gets all pygame events

        Returns:
            list[event]: List of pygame events.
        """
        return pygame.event.get()
