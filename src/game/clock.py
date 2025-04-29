import pygame


class Clock:
    """Wrapper for pygame clock."""

    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Limits the game loops execution

        Args:
            fps (int): Maximum number of frames per second.

        """
        self._clock.tick(fps)
