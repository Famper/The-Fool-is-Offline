from init.InitFoolOfflineVars import FoolOffline


if __name__ == '__main__':
    suits = FoolOffline()

    print(suits.suits.get(suits.trump_suit))

    player_one = {
        'suit': 'hearts',
        'value': '6'
    }

    player_two = {
        'suit': 'clubs',
        'value': 'Ace'
    }

    print(suits.check_possible(player_one, player_two))

    print(suits.print_card(player_one))
    print(suits.print_card(player_two))
