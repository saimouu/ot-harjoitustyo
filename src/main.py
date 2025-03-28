from game.game_logic import GameLogic


def main():
    game = GameLogic()
    print(game)
    game._spawn_random_block()
    game._spawn_random_block()
    print(game)


if __name__ == "__main__":
    main()
