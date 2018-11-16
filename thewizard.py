import random


def one_round(round_n, deck, players, strategy):
    player_bets = {}
    player_results = {}
    round_score = {}

    # Deck shuffled, hands dealt
    shuffled_cards = list(random.sample(deck, len(players) * round_n))
    player_hands = dict(zip(players, deal_cards(shuffled_cards, round_n)))

    # Players receive cards, make bet
    for player, hand in player_hands.items():
        print("{} is dealt ... {}".format(player, hand))
        player_bets[player] = strategy[player](hand)
        print("{} bets ... {}\n".format(player, player_bets[player]))

    # Winning cards shown
    winning_cards = sorted(shuffled_cards, reverse=True)[0: round_n]
    print("Winning cards for Round {} ... {}\n".format(round_n, winning_cards))

    # Results calculated, added to score
    for player, bet in player_bets.items():
        player_results[player] = calculate_player_result(player_hands[player], winning_cards)
        print("{} has ... {}".format(player, player_results[player]))
        round_score[player] = score_round(player_results[player], player_bets[player])
    return round_score


def deal_cards(cards, round_n):
    for i in range(0, len(cards), round_n):
        yield cards[i:i + round_n]


def calculate_player_result(cards, winners):
    score_tally = 0
    for card in winners:
        if card in cards:
            score_tally += 1
        else:
            score_tally += 0
    return score_tally


def score_round(actual, bet):
    score = 0
    if bet == actual:
        score += (2 + actual)
    elif bet != actual:
        score += -(abs(actual - bet))
    return score


# Betting strategies
def bet_over_50(cards):
    return len([c for c in cards if c > 50])


def bet_over_75(cards):
    return len([c for c in cards if c > 75])


def round_based(cards):
    if len(cards) < 5:
        return len([c for c in cards if c > 50])
    else:
        return len([c for c in cards if c > 75])


def game(seed=None):
    deck = list(range(1, 101))
    players = ["Angela", "Theresa", "Emmanuel", "Donald"]
    scoreboard = {"Angela": 0, "Theresa": 0, "Emmanuel": 0, "Donald": 0}
    player_strategies = {"Angela": round_based, "Theresa": round_based,
                         "Emmanuel": bet_over_50, "Donald": bet_over_75}
    random.seed(seed)

    # Run round, update scoreboard with round result
    for round_n in range(1, 11):
        print("\n======== Round {} ========".format(round_n))
        round_result = one_round(round_n, deck, players, player_strategies)
        for player, score in scoreboard.items():
            scoreboard[player] += round_result[player]
        print("\n -------- Scoreboard!! --------\n")
        for player, score in scoreboard.items():
            print("{}: {}".format(player, score))

    # Return winner of 10 rounds
    winner = max(scoreboard.keys(), key=(lambda name: scoreboard[name]))
    print("\n ...and the winner is... {}!!  Strategy: {}".format(winner, str(player_strategies[winner])))
    return winner


if __name__ == "__main__":
    game()
