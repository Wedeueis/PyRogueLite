from enum import IntEnum


class StatModType(IntEnum):
    FLAT = 100
    PERCENT_ADD = 200
    PERCENT_MULT = 300


class StatsModifier:
    def __init__(
        self,
        value: int,
        type: StatModType,
        order: int = None,
        source: object = None,
    ):
        self._value = value
        self._type = type
        if order == None:
            self._order = int(type)
        else:
            self._order = order
        self._source = source

    def __repr__(self) -> str:
        return f"Modifier value: {self._value} type: {self._type}  order: {self._order}"

    @property
    def value(self) -> int:
        return self._value

    @property
    def type(self) -> StatModType:
        return self._type

    @property
    def order(self) -> int:
        return self._order

    @property
    def source(self) -> object:
        return self._source


class Stats:
    def __init__(self, value: int = 0, name: str = None):
        self._base_value = value
        self._last_base_value = value
        self._name = name
        self._value = self._base_value
        self._modifiers = []

        self._is_dirty = True

    def __repr__(self) -> str:
        return f"{self.name} stats - base value: {self._base_value} current value: {self.value}\n"

    @property
    def value(self) -> int:
        if self._is_dirty or (self._base_value != self._last_base_value):
            self._value = self.calculate_final_value()
            self._last_base_value = self._base_value
        return round(self._value)

    @property
    def name(self) -> str:
        return self._name

    @property
    def base_value(self) -> int:
        return self._base_value

    @base_value.setter
    def base_value(self, value):
        self._base_value = value

    def add_modifier(self, mod: StatsModifier):
        self._is_dirty = True
        self._modifiers.append(mod)
        self._modifiers.sort(key=lambda x: x.order)

    def remove_modifier(self, mod: StatsModifier):
        if mod in self._modifiers:
            self._is_dirty = True
            self._modifiers.remove(mod)
            return True
        return False

    def remove_all_modifiers_from_source(self, source: object):
        did_remove = False
        for mod in self._modifiers[::-1]:
            if mod.source is source:
                did_remove = self.remove_modifier(mod)
                if not did_remove:
                    raise Exception("Failed to remove modifier")
        return did_remove

    def calculate_final_value(self) -> float:
        final_value = self._base_value
        sum_percent_add = 0

        for mod in self._modifiers:
            if mod.type == StatModType.FLAT:
                final_value += mod.value
            elif mod.type == StatModType.PERCENT_MULT:
                final_value *= 1 + mod.value
            elif mod.type == StatModType.PERCENT_ADD:
                sum_percent_add += mod.value

        if sum_percent_add != 0:
            final_value *= 1 + sum_percent_add
            sum_percent_add = 0

        final_value = round(final_value, 4)

        self._is_dirty = False

        return final_value
