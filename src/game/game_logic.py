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

    def _move_block_left(self, row, col):
        # Wall check
        if col - 1 < 0:
            return

        # Early return check
        if (
            self._grid[row][col - 1] != self._grid[row][col]
            and self._grid[row][col - 1] != 0
        ):
            return

        block_value = self._grid[row][col]
        # traverse backwards through the row
        for idx in range(col - 1, -1, -1):
            current_block = self._grid[row][idx]
            if current_block == 0:
                self._grid[row][idx] = self._grid[row][idx + 1]
                self._grid[row][idx + 1] = 0
            elif current_block == block_value:
                self._grid[row][idx] = block_value * 2
                self._grid[row][idx + 1] = 0
                break  # can only merge once
            else:
                break

    def _move_block_right(self, row, col):
        if col + 1 > 3:
            return

        if (
            self._grid[row][col + 1] != self._grid[row][col]
            and self._grid[row][col + 1] != 0
        ):
            return

        block_value = self._grid[row][col]
        for idx in range(col + 1, 4):
            current_block = self._grid[row][idx]
            if current_block == 0:
                self._grid[row][idx] = self._grid[row][idx - 1]
                self._grid[row][idx - 1] = 0
            elif current_block == block_value:
                self._grid[row][idx] = block_value * 2
                self._grid[row][idx - 1] = 0
                break
            else:
                break

    def _move_block_up(self, row, col):
        pass

    def _move_block_down(self, row, col):
        pass

    def move_all_blocks_left(self):
        for row in range(4):
            for col in range(4):
                # Zero-valued blocks are not moved
                if self._grid[row][col] == 0:
                    continue
                self._move_block_left(row, col)

    def move_all_blocks_right(self):
        for row in range(4):
            for col in range(3, -1, -1):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_right(row, col)

    def move_all_blocks_up(self):
        pass

    def move_all_blocks_down(self):
        pass

    @property
    def grid(self):
        return self._grid

    def __str__(self) -> str:
        s = ""
        for i in range(len(self._grid)):
            s += str(self._grid[i]) + "\n"
        return s
