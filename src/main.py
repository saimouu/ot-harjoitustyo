from game.game_logic import GameLogic


def main():
    game = GameLogic()
    game._spawn_random_block()
    game._spawn_random_block()
    game._spawn_random_block()
    game._spawn_random_block()
    game._spawn_random_block()
    # game._grid[0][1] = 2
    # game._grid[0][2] = 2
    # game._grid[1][3] = 2
    # game._grid[3][1] = 2

    print(game)
    game.move_all_blocks_right()
    print("right")
    print(game)
    game.move_all_blocks_down()
    print("down")
    print(game)
    game.move_all_blocks_up()
    print("up")
    print(game)
    game.move_all_blocks_left()
    print("left")
    print(game)


if __name__ == "__main__":
    main()
