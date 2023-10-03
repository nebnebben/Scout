def get_values_of_all_hands():
    all_hands_values = {}
    current_value = 0
    for i in range(1, 11):

        for j in range(1, 11 - (i - 1)):
            cur_hand = [x for x in range(j, j + i)]
            all_hands_values[tuple(cur_hand)] = current_value

            cur_hand = [x for x in range(j + i - 1, j - 1, - 1)]
            all_hands_values[tuple(cur_hand)] = current_value
            current_value += 1

        if i == 1:
            continue

        for j in range(1, 11):
            cur_hand = [j] * i
            all_hands_values[tuple(cur_hand)] = current_value
            current_value += 1

    return all_hands_values


def a_beats_b(a, b):
    if len(a) > len(b):
        return True
    if len(b) > len(a):
        return False

    a_type = 'set' if len(set(a)) == 1 else 'run'
    b_type = 'set' if len(set(b)) == 1 else 'run'

    if a_type == 'set' and b_type == 'run':
        return True
    if a_type == 'run' and b_type == 'set':
        return False

    return a[0] > b[0]


all_hands_values = get_values_of_all_hands()