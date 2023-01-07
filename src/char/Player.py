from Stats import Stats


class Character:
    def __init__(self, strength):
        self._strength = Stats(strength)

    @property
    def strength(self):
        return self._strength
