import pytest

from src.char.stats import Stats, StatsModifier, StatModType


class TestStats(object):
    @pytest.fixture
    def stat(self):
        """Returns a Stats instance with a value of 10"""
        return Stats(10)

    def test_stat_default_value(self):
        stat = Stats()
        expected = 0
        actual = stat.value
        message = f"Wrong default value, expected: {expected}, actual: {actual}"
        assert actual == expected, message

    def test_stat_with_initial_value(self):
        stat = Stats(10)

        expected = 10
        actual = stat.value
        message = f"Wrong base value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_stat_return_type(self, stat):
        expected = int
        actual = type(stat.value)
        message = f"Wrong return type, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_stat_return_type_after_modification(self, stat):
        stat.add_modifier(StatsModifier(0.5, StatModType.PERCENT_MULT))
        expected = int
        actual = type(stat.value)
        message = f"Wrong return type, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_add_one_flat_modifier(self, stat):
        stat.add_modifier(StatsModifier(2, StatModType.FLAT))

        expected = 12
        actual = stat.value
        message = f"Wrong modified value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_add_mult_flat_modifier(self, stat):
        stat.add_modifier(StatsModifier(10, StatModType.FLAT))
        stat.add_modifier(StatsModifier(10, StatModType.FLAT))
        stat.add_modifier(StatsModifier(-5, StatModType.FLAT))

        expected = 25
        actual = stat.value
        message = f"Wrong modified value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_add_one_percentadd_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))

        expected = 11
        actual = stat.value
        message = f"Wrong modified value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_add_mult_percentadd_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))

        expected = 13
        actual = stat.value
        message = f"Wrong modified value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_add_one_percentmult_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_MULT))

        expected = 11
        actual = stat.value
        message = f"Wrong modified value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_add_mult_percentmult_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.2, StatModType.PERCENT_MULT))
        stat.add_modifier(StatsModifier(0.5, StatModType.PERCENT_MULT))

        expected = 18
        actual = stat.value
        message = f"Wrong modified value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_add_mult_diferent_modifiers(self, stat):
        stat.add_modifier(StatsModifier(0.25, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.25, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.5, StatModType.PERCENT_MULT))
        stat.add_modifier(StatsModifier(2, StatModType.FLAT))

        expected = 27
        actual = stat.value
        message = f"Wrong modified value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_rem_modifier_with_empty_list(self, stat):
        expected = False
        actual = stat.remove_modifier(StatsModifier(5, StatModType.FLAT))
        message = f"Wrong return value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_rem_modifier_with_ref(self, stat):
        mod = StatsModifier(5, StatModType.FLAT)
        stat.add_modifier(mod)
        stat.remove_modifier(mod)

        expected = 10
        actual = stat.value
        message = f"Failed to remove modifier from reference, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_rem_one_modifier_from_source(self, stat):
        source = list()
        mod = StatsModifier(5, StatModType.FLAT, source=source)
        source.append(mod)
        stat.add_modifier(source[0])
        stat.remove_all_modifiers_from_source(source)

        expected = 10
        actual = stat.value
        message = f"Failed to remove modifier from source, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_rem_mult_modifier_from_source(self, stat):
        source = list()
        source.append(StatsModifier(5, StatModType.FLAT, source=source))
        source.append(StatsModifier(10, StatModType.FLAT, source=source))
        source.append(StatsModifier(10, StatModType.FLAT, source=source))
        for mod in source:
            stat.add_modifier(mod)
        stat.remove_all_modifiers_from_source(source)

        expected = 10
        actual = stat.value
        message = f"Failed to remove all modifiers from source, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_modifier_with_order_param(self):
        mod = StatsModifier(5, StatModType.FLAT, order=500)

        expected = 500
        actual = mod.order
        message = f"Wrong order value, expected: {expected}, actual: {actual}"

        assert actual == expected, message

    def test_one_modifier_source(self):
        source = list()
        mod = StatsModifier(5, StatModType.FLAT, source=source)
        source.append(mod)

        expected = source
        actual = source[0].source
        message = f"Failed to attach modifier to source, expected: {expected}, actual: {actual}"

        assert actual is expected, message

    def test_mult_modifier_source(self):
        source = list()
        mod1 = StatsModifier(5, StatModType.FLAT, source=source)
        source.append(mod1)
        mod2 = StatsModifier(10, StatModType.FLAT, source=source)
        source.append(mod2)

        expected = source
        actual = source[0].source
        message = f"Failed to attach modifier to source, expected: {expected}, actual: {actual}"

        assert actual is expected, message

        actual = source[1].source
        message = f"Failed to attach modifier to source, expected: {expected}, actual: {actual}"

        assert actual is expected, message
