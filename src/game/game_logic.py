import random

# Note: move methods have a lot of repeating but are quite hard to split to other functions or combine to one,
#   without making it even more complicated


class GameLogic:
    def __init__(self):
        self._grid = [[0 for _ in range(4)] for _ in range(4)]
        self._score = 0

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
        merged_blocks = set()
        for row in range(4):
            for col in range(4):
                # Zero-valued blocks are not moved
                if self._grid[row][col] == 0:
                    continue
                self._move_block_left(row, col, merged_blocks)

    def move_all_blocks_right(self):
        merged_blocks = set()
        for row in range(4):
            for col in range(3, -1, -1):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_right(row, col, merged_blocks)

    def move_all_blocks_up(self):
        merged_blocks = set()
        for col in range(4):
            for row in range(4):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_up(row, col, merged_blocks)

    def move_all_blocks_down(self):
        merged_blocks = set()  # (row, col) tuple
        for col in range(4):
            for row in range(3, -1, -1):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_down(row, col, merged_blocks)

    @property
    def grid(self):
        return self._grid

    @property
    def score(self):
        return self._score

    @grid.setter
    def grid(self, new_grid):
        if len(new_grid) != 4 or len(new_grid[0]) != 4:
            raise ValueError("Grid must be a 4x4 matrix")
        self._grid = new_grid

    def get_block_value(self, row, col):
        return self._grid[row][col]

    def __str__(self) -> str:
        s = ""
        for i in range(len(self._grid)):
            s += str(self._grid[i]) + "\n"
        return s
