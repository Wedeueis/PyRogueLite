import pytest

from src.char.stats import Stats, StatsModifier, StatModType


class TestStats(object):
    @pytest.fixture
    def stat(self):
        """Returns a Stats instance with a value of 10"""
        return Stats(10)

    def test_stat_default_value(self):
        stat = Stats()
        assert stat.value == 0

    def test_stat_with_initial_value(self):
        stat = Stats(10)
        assert stat.value == 10

    def test_add_one_flat_modifier(self, stat):
        stat.add_modifier(StatsModifier(2, StatModType.FLAT))
        assert stat.value == 12

    def test_add_mult_flat_modifier(self, stat):
        stat.add_modifier(StatsModifier(10, StatModType.FLAT))
        stat.add_modifier(StatsModifier(10, StatModType.FLAT))
        stat.add_modifier(StatsModifier(-5, StatModType.FLAT))
        assert stat.value == 25

    def test_add_one_percentadd_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))
        assert stat.value == 11

    def test_add_mult_percentadd_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_ADD))
        assert stat.value == 13

    def test_add_one_percentmult_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.1, StatModType.PERCENT_MULT))
        assert stat.value == 11

    def test_add_mult_percentmult_modifier(self, stat):
        stat.add_modifier(StatsModifier(0.2, StatModType.PERCENT_MULT))
        stat.add_modifier(StatsModifier(0.5, StatModType.PERCENT_MULT))
        assert stat.value == 18

    def test_add_mult_diferent_modifiers(self, stat):
        stat.add_modifier(StatsModifier(0.25, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.25, StatModType.PERCENT_ADD))
        stat.add_modifier(StatsModifier(0.5, StatModType.PERCENT_MULT))
        stat.add_modifier(StatsModifier(2, StatModType.FLAT))
        assert stat.value == 27
