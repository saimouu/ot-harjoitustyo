class GameLogic:
    def __init__(self):
        self._grid = [[0 for _ in range(4)] for _ in range(4)]

    @property
    def grid(self):
        return self._grid

    def __str__(self) -> str:
        s = ""
        for i in range(len(self._grid)):
            s += str(self._grid[i]) + "\n"
        return s
