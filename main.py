import copy

from comparison import all_hands_values, a_beats_b
from playablehand import PlayableHand
from solve_with_scales import solve_with_scales


def get_possible_hands(cards, memo, opposing_hand, possible_hands):
    if not cards:
        return 0

    cards_tuple = tuple(cards)

    if cards_tuple in memo:
        return memo[cards_tuple]

    memo[cards_tuple] = float('inf')
    for i in range(len(cards)):

        cards_copy = copy.deepcopy(cards)
        pattern = ''
        if i + 1 < len(cards):
            if cards[i + 1] == cards[i] + 1:
                pattern = 'asc'
            elif cards[i + 1] == cards[i] - 1:
                pattern = 'desc'
            elif cards[i + 1] == cards[i]:
                pattern = 'same'

        current_hand = []

        while i < len(cards_copy):
            current_hand.append(cards_copy[i])

            previous = cards_copy[i]
            del cards_copy[i]

            res = solve_with_scales(cards_copy, memo) + 1

            memo[cards_tuple] = min(memo[cards_tuple], res)

            if a_beats_b(current_hand, opposing_hand):
                current_hand_inds = [j for j in range(i, i + len(current_hand))]

                hand = PlayableHand(inds=current_hand_inds,
                                    cards=copy.deepcopy(current_hand),
                                    value=all_hands_values[tuple(current_hand)],
                                    min_steps_to_end=memo[cards_tuple] - 1
                                    )

                possible_hands[tuple(current_hand_inds)] = hand

            if pattern == '' or i == len(cards_copy):
                break
            if pattern == 'asc' and previous != cards_copy[i] - 1:
                break
            elif pattern == 'desc' and previous != cards_copy[i] + 1:
                break
            elif pattern == 'same' and previous != cards_copy[i]:
                break

    return memo[cards_tuple]


memo = {}
cards = [3, 2, 2, 1, 1, 2, 2, 3, 3, 3]
opposing_hand = [2, 3]
possible_hands = {}
get_possible_hands(cards, memo, opposing_hand, possible_hands)

for v in possible_hands.values():
    v.print_values()
    print('')


