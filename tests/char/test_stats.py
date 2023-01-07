if __name__ == "__main__":
    _str = Stats(10)
    print(_str.value)
    _str.add_modifier(StatsModifier(2, StatModType.FLAT))
    _str.add_modifier(StatsModifier(2, StatModType.PERCENT_ADD))
    _str.add_modifier(StatsModifier(3, StatModType.PERCENT_ADD))
    _str.add_modifier(StatsModifier(2, StatModType.PERCENT_MULT))
    print(_str.value)
