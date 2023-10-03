class PlayableHand:

    def __init__(self, inds, cards, value, min_steps_to_end):
        self.inds = inds
        self.cards = cards
        self.value = value
        self.min_steps_to_end = min_steps_to_end

    def print_values(self):
        print(f'indices are {self.inds}')
        print(f'cards are {self.cards}')
        print(f'value is {self.value}')
        print(f'min_steps_to_end are {self.min_steps_to_end}')