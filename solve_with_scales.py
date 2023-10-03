import copy


def solve_with_scales(cards, memo):
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

        while i < len(cards_copy):
            previous = cards_copy[i]
            del cards_copy[i]

            res = solve_with_scales(cards_copy, memo) + 1

            memo[cards_tuple] = min(memo[cards_tuple], res)

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

solve_with_scales(cards, memo)
