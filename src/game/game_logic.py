import random
from copy import deepcopy

from config import AMOUNT_OF_UNDOS_ALLOWED


class GameLogic:
    """Manages the core game mechanics and state of 2048 game.

    Attributes:
        grid (list[list[int]]): Game board containing block values in a 2D matrix.
        previous_grid (list[list[int]] | None): Previous grid state for undo functionality.
        undos_count (int): Number of undos used by the player.
        score (int): Current game score.
        moves (int): Total number of valid moves made.
    """

    def __init__(self):
        """Class constructor.

        Sets default values for attributes and initializes grid as a 4x4 2D matrix
        where zero valued blocks are empty spaces.

        """
        self._grid = [[0 for _ in range(4)] for _ in range(4)]
        self._previous_grid = None
        self._undos_count = 0
        self._score = 0
        self._moves = 0

    def reset_game(self):
        """Resets game to a state with two randomly placed blocks."""
        self._grid = [[0 for _ in range(4)] for _ in range(4)]
        self._score = 0
        self._moves = 0
        self.spawn_random_block()
        self.spawn_random_block()

    def _transpose_grid(self):
        """Transposes the current grid.

        Returns:
            list[list[int]]: Transposed version of the grid.
        """
        return list(map(list, zip(*self._grid)))

    def _get_empty_spaces(self):
        """Gets all empty spaces of the current grid in (x, y) format.

        Returns:
            list[tuple[int, int]]: List of empty spaces as coordinate pairs.

        """
        empty = []
        for row in range(4):
            for col in range(4):
                if self._grid[row][col] == 0:
                    empty.append((row, col))
        return empty

    def spawn_random_block(self):
        """Spawns either 2 or 4 -block to one of the empty empty_spaces

        Returns:
            bool: True if block was spawned, False if the grid is full

        """
        empty_spaces = self._get_empty_spaces()
        if not empty_spaces:
            return False

        space = random.choice(empty_spaces)
        num = 2 if random.random() <= 0.9 else 4

        self._grid[space[0]][space[1]] = num
        return True

    def check_win(self):
        """Checks if grid contains a 2048 block.

        Returns:
            bool: True if grid contains 2048, False otherwise.
        """
        for row in range(4):
            for col in range(4):
                if self._grid[row][col] == 2048:
                    return True
        return False

    def check_game_over(self):
        """Checks if game is over.

        Returns True if grid is full and there are no legal moves left

        Returns:
            bool: True if game is over, False otherwise.
        """
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
        """Moves all blocks to the left and combines blocks with the same value.

        Updates the game grid, score and move count accordingly.
        A block can only merge one time.
        """
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()
        for row in range(4):
            for col in range(4):
                # Zero-valued blocks are not moved
                if self._grid[row][col] == 0:
                    continue
                self._move_block_left(row, col, merged_blocks)
        if self.check_any_block_moved():
            self._moves += 1

    def move_all_blocks_right(self):
        """Moves all blocks to the right and combines blocks with the same value.

        Updates the game grid, score and move count accordingly.
        A block can only merge one time.
        """
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()
        for row in range(4):
            for col in range(3, -1, -1):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_right(row, col, merged_blocks)
        if self.check_any_block_moved():
            self._moves += 1

    def move_all_blocks_up(self):
        """Moves all blocks up and combines blocks with the same value.

        Updates the game grid, score and move count accordingly.
        A block can only merge one time.
        """
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()
        for col in range(4):
            for row in range(4):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_up(row, col, merged_blocks)
        if self.check_any_block_moved():
            self._moves += 1

    def move_all_blocks_down(self):
        """Moves all blocks down and combines blocks with the same value.

        Updates the game grid, score and move count accordingly.
        A block can only merge one time.
        """
        self._previous_grid = deepcopy(self._grid)
        merged_blocks = set()  # (row, col) tuple
        for col in range(4):
            for row in range(3, -1, -1):
                if self._grid[row][col] == 0:
                    continue
                self._move_block_down(row, col, merged_blocks)
        if self.check_any_block_moved():
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
        """Returns the amount of undos left.

        AMOUNT_OF_UNDOS_ALLOWED is specified in config.py.

        Returns:
            int: Number of undo actions the player can do.

        """
        return AMOUNT_OF_UNDOS_ALLOWED - self._undos_count

    def get_max_block(self):
        """Gets the largest block from the grid.

        Returns:
            int: Largest block value in the grid.

        """
        return max(map(max, self._grid))

    def check_any_block_moved(self):
        """Checks if the grid has changed.

        Returns:
            bool: True if the current grid and previous_grid are not the same, False otherwise.
        """
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
