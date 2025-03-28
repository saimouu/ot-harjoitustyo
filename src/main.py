from game.game_logic import GameLogic


def main():
    game = GameLogic()
    game._grid[0][1] = 2
    game._grid[0][0] = 2

    game._grid[2][3] = 2
    game._grid[2][0] = 2

    game._grid[3][1] = 2
    game._grid[1][0] = 2
    print(game)
    game.move_all_blocks_left()
    print(game)


if __name__ == "__main__":
    main()
