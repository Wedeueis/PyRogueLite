from enum import IntEnum
import numpy as np


class Stats:
    def __init__(self, value):
        self._base_value = value
        self._value = self._base_value
        self._modifiers = []

        self._is_dirty = True

    @property
    def value(self):
        if self._is_dirty:
            self._value = self.calculate_final_value()
            return self._value
        else:
            return self._value

    def add_modifier(self, mod):
        self._is_dirty = True
        self._modifiers.append(mod)
        self._modifiers.sort(key=lambda x: x.order)

    def remove_modifier(self, mod):
        if mod in self._modifiers:
            self._is_dirty = True
            self._modifiers.remove(mod)
            return True
        return False

    def remove_all_modifiers_from_source(self, source):
        did_remove = False
        for mod in self._modifiers:
            if mod.source == source:
                self.remove_modifier(mod)
                did_remove = True
        return did_remove

    def calculate_final_value(self):
        final_value = self._base_value
        sum_percent_add = 0

        for mod in self._modifiers:
            if mod.type == StatModType.FLAT:
                final_value += mod.value
            elif mod.type == StatModType.PERCENT_MULT:
                final_value *= 1 + mod.value
            elif mod.type == StatModType.PERCENT_ADD:
                sum_percent_add += mod.value

            if (mod.type != StatModType.PERCENT_ADD) and (sum_percent_add != 0):
                final_value *= 1 + sum_percent_add
                sum_percent_add = 0

        final_value = round(final_value, 4)

        self._is_dirty = False

        return final_value


class StatModType(IntEnum):
    FLAT = 100
    PERCENT_ADD = 200
    PERCENT_MULT = 300


class StatsModifier:
    def __init__(self, value, type, order=None, source=None):
        self._value = value
        self._type = type
        if order == None:
            self._order = int(type)
        else:
            self._order = order
        self._source = source

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type

    @property
    def order(self):
        return self._order

    @property
    def source(self):
        return self._source


if __name__ == "__main__":
    _str = Stats(10)
    print(_str.value)
    _str.add_modifier(StatsModifier(2, StatModType.FLAT))
    _str.add_modifier(StatsModifier(2, StatModType.PERCENT_ADD))
    _str.add_modifier(StatsModifier(3, StatModType.PERCENT_ADD))
    _str.add_modifier(StatsModifier(2, StatModType.PERCENT_MULT))
    print(_str.value)
