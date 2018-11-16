import thewizard


def simulate(n_games, seed):
    player_strategies = {"Angela": "round_based", "Theresa": "round_based",
                         "Emmanuel": "bet_over_50", "Donald": "bet_over_75"}
    winner_tally = {"Angela": 0, "Theresa": 0, "Emmanuel": 0, "Donald": 0}

    for n in range(1, n_games + 1):
        winner = thewizard.game(seed)
        winner_tally[winner] += 1

    print("\n\nWins per player\n+++++++++++++\n")

    for player, wins in winner_tally.items():
        print("{}: {} ... strategy: {}".format(player, wins, player_strategies[player]))


if __name__ == "__main__":
    simulate(10000, seed=None)
