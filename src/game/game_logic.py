import random
from copy import deepcopy

from config import AMOUNT_OF_UNDOS_ALLOWED


class GameLogic:
    def __init__(self):
        self._grid = [[0 for _ in range(4)] for _ in range(4)]
        self._previous_grid = None
        self._undos_count = 0
        self._score = 0
        self._moves = 0

    def reset_game(self):
        self._grid = [[0 for _ in range(4)] for _ in range(4)]
        self._score = 0
        self.spawn_random_block()
        self.spawn_random_block()

    def _transpose_grid(self):
        return list(map(list, zip(*self._grid)))

    def _get_empty_spaces(self):
        empty = []
        for row in range(4):
            for col in range(4):
                if self._grid[row][col] == 0:
                    empty.append((row, col))
        return empty

    def spawn_random_block(self):
        empty_spaces = self._get_empty_spaces()
        if not empty_spaces:
            return False

        space = random.choice(empty_spaces)
        num = 2 if random.random() <= 0.9 else 4

        self._grid[space[0]][space[1]] = num
        return True

    def check_win(self):
        for row in range(4):
            for col in range(4):
                if self._grid[row][col] == 2048:
                    return True
        return False

    def check_game_over(self):
        if len(self._get_empty_spaces()) != 0:
            return False

        for row in range(4):
            for col in range(4 - 1):
                if self._grid[row][col] == self._grid[row][col + 1]:
                    return False

        # Vertical check
        t_grid = self._transpose_grid()
        for row in range(4):
            for col in range(4 - 1):
                if t_grid[row][col] == t_grid[row][col + 1]:
                    return False

        return True

    def _move_block_left(self, row, col, merged_blocks):
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
            elif current_block == block_value and (row, idx) not in merged_blocks:
                self._grid[row][idx] = block_value * 2
                self._grid[row][idx + 1] = 0
                merged_blocks.add((row, idx))
                self._score += block_value * 2
                break  # can only merge once
            else:
                break

    def _move_block_right(self, row, col, merged_blocks):
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
            elif current_block == block_value and (row, idx) not in merged_blocks:
                self._grid[row][idx] = block_value * 2
                self._grid[row][idx - 1] = 0
                merged_blocks.add((row, idx))
                self._score += block_value * 2
                break
            else:
                break

    def _move_block_up(self, row, col, merged_blocks):
        if row - 1 < 0:
            return

        if (
            self._grid[row - 1][col] != self._grid[row][col]
            and self._grid[row - 1][col] != 0
        ):
            return

        block_value = self._grid[row][col]
        for idx in range(row - 1, -1, -1):
            current_block = self._grid[idx][col]
            if current_block == 0:
                self._grid[idx][col] = self._grid[idx + 1][col]
                self._grid[idx + 1][col] = 0
            elif current_block == block_value and (idx, col) not in merged_blocks:
                self._grid[idx][col] = block_value * 2
                self._grid[idx + 1][col] = 0
                merged_blocks.add((idx, col))
                self._score += block_value * 2
                break
            else:
                break

    def _move_block_down(self, row, col, merged_blocks):
        if row + 1 > 3:
            return

        if (
            self._grid[row + 1][col] != self._grid[row][col]
            and self._grid[row + 1][col] != 0
        ):
            return

        block_value = self._grid[row][col]
        for idx in range(row + 1, 4):
            current_block = self._grid[idx][col]
            if current_block == 0:
                self._grid[idx][col] = self._grid[idx - 1][col]
                self._grid[idx - 1][col] = 0
            elif current_block == block_value and (idx, col) not in merged_blocks:
                self._grid[idx][col] = block_value * 2
                self._grid[idx - 1][col] = 0
                merged_blocks.add((idx, col))
                self._score += block_value * 2
                break
            else:
                break

    def move_all_blocks_left(self):
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()
        for row in range(4):
            for col in range(4):
                # Zero-valued blocks are not moved
                if self._grid[row][col] == 0:
                    continue
                self._move_block_left(row, col, merged_blocks)
        self._moves += 1

    def move_all_blocks_right(self):
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()
        for row in range(4):
            for col in range(3, -1, -1):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_right(row, col, merged_blocks)
        self._moves += 1

    def move_all_blocks_up(self):
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()
        for col in range(4):
            for row in range(4):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_up(row, col, merged_blocks)
        self._moves += 1

    def move_all_blocks_down(self):
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()  # (row, col) tuple
        for col in range(4):
            for row in range(3, -1, -1):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_down(row, col, merged_blocks)
        self._moves += 1

    def restore_previous_grid(self):
        if (
            self._previous_grid
            and self._undos_count < 2
            and self._previous_grid != self._grid
        ):
            self._grid = deepcopy(self._previous_grid)
            self._undos_count += 1
            self._moves -= 1
            return True
        return False

    def undos_left(self):
        return AMOUNT_OF_UNDOS_ALLOWED - self._undos_count

    def get_max_block(self):
        return max(map(max, self._grid))

    def check_any_block_moved(self):
        return self._grid != self._previous_grid

    @property
    def moves(self):
        return self._moves

    @property
    def grid(self):
        return self._grid

    @property
    def score(self):
        return self._score

    @property
    def previous_grid(self):
        return self._previous_grid

    @grid.setter
    def grid(self, new_grid):
        if len(new_grid) != 4 or len(new_grid[0]) != 4:
            raise ValueError("Grid must be a 4x4 matrix")
        self._grid = new_grid

    def get_block_value(self, row, col):
        return self._grid[row][col]

    def __str__(self) -> str:
        s = ""
        for row in self._grid:
            s += str(row) + "\n"
        return s
