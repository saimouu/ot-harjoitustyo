import random


class GameLogic:
    def __init__(self):
        self._grid = [[0 for _ in range(4)] for _ in range(4)]

    def _get_empty_spaces(self):
        empty = []
        for row in range(4):
            for col in range(4):
                if self._grid[row][col] == 0:
                    empty.append((row, col))
        return empty

    def _spawn_random_block(self):
        empty_spaces = self._get_empty_spaces()
        space = random.choice(empty_spaces)
        num = 2 if random.random() <= 0.9 else 4

        self._grid[space[0]][space[1]] = num

    def _check_win(self):
        for row in range(4):
            for col in range(4):
                if self._grid[row][col] == 2048:
                    return True
        return False

    @property
    def grid(self):
        return self._grid

    def __str__(self) -> str:
        s = ""
        for i in range(len(self._grid)):
            s += str(self._grid[i]) + "\n"
        return s
