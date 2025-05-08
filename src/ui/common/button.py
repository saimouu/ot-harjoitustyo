import pygame

from config import (
    BLOCK_SIZE,
    BOARD_COLOR,
    BUTTON_FONT_SIZE,
    FONT_FILE_PATH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Button:
    """Button base class.

    Works relative to the main board.
    """

    def __init__(self, text, rect, command):
        """Class contructor.

        Args:
            text (str): Text to display in the middle of the button.
            rect: Pygame rect object.
            command (func): Return value when clicked.
        """
        self._text = text
        self.rect = rect
        self._font = pygame.font.Font(FONT_FILE_PATH, BUTTON_FONT_SIZE)
        self._command = command

    def render(self, board):
        """Draws the button.

        Args:
            board: Pygame surface or display object.
        """
        text = self._font.render(str(self._text), True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        pygame.draw.rect(board, BOARD_COLOR, self.rect, border_radius=10)
        board.blit(text, text_rect)

    def handle_event(self, event):
        """Handles event if button was clicked.

        Calls button's command function if the event was MOUSEBUTTONDOWN and
        the event position collides with the button's position.

        Event position is converted to position on the board surface.

        Args:
            event: Pygame event.

        Returns:
            (str | None): String according to the buttons command attribute,
                            or None if the button was not clicked.

        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            board_position = self._relative_position(event.pos)
            if self.rect.collidepoint(board_position):
                return self._command()
        return None

    # Fix to get the correct positions relative to the surface
    def _relative_position(self, screen_position):
        board_x = (SCREEN_WIDTH - BLOCK_SIZE * 4) / 2
        board_y = (SCREEN_HEIGHT - BLOCK_SIZE * 4) / 2

        return (screen_position[0] - board_x, screen_position[1] - board_y)


class DisplayButton(Button):
    """Same as button but event positions are not relative to the board.

    The event positions are treated 'regularly' relative to the display.
    """

    def __init__(self, text, rect, command):
        super().__init__(text, rect, command)

    def handle_event(self, event):
        """Handles event if button was clicked.

        Calls button's command function if the event was MOUSEBUTTONDOWN and
        the event position collides with the button's position.

        Args:
            event: Pygame event.

        Returns:
            (str | None): String according to the buttons command attribute,
                            or None if the button was not clicked.

        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self._command()
        return None
