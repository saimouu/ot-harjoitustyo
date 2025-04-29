import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
BLOCK_SIZE = 110

OUTLINE_THICKNESS = 5

BACKGROUND_COLOR = (173, 163, 160)
BOARD_COLOR = (133, 111, 103)
OUTLINE_COLOR = (36, 30, 28)
BLOCK_COLORS = {
    2: (196, 188, 181),
    4: (168, 137, 111),
    8: (219, 127, 50),
    16: (219, 78, 50),
    32: (161, 48, 26),
    64: (191, 27, 27),
    128: (204, 202, 69),
    256: (163, 161, 28),
    512: (217, 194, 69),
    1024: (235, 202, 26),
    2048: (252, 213, 0),
}

FONT_SIZE = 60
BUTTON_FONT_SIZE = 40
TEXT_FONT_SIZE = 32
FONT_FILE_PATH = None

AMOUNT_OF_UNDOS_ALLOWED = 2

FPS = 30

dirname = os.path.dirname(__file__)
SCORES_FILE_PATH = os.path.join(dirname, "scores.csv")
