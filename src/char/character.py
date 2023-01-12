import json
import os

from src.char.stats import Stats
from .. import config


class StatsMapping:
    STR = "str"
    VIT = "vit"
    AGI = "agi"
    INT = "int"
    WILL = "will"
    LCK = "lck"


class Profile:
    profile_path = os.path.join(config.DATA_PATH, "stats_profiles.json")
    with open(profile_path) as file:
        _profiles = json.load(file)

    @staticmethod
    def get_profile(class_name: str) -> dict:
        if class_name in Profile._profiles:
            return Profile._profiles[class_name]
        else:
            return ValueError


class BaseStats:
    def __init__(self) -> None:
        # Data Manager Read from json or sql
        self._is_dirty = False
        self._stats_map = {}

    def init_stats_from_profile(self, class_name: str):
        class_profile = Profile.get_profile(class_name)
        for attr in class_profile:
            attr_name, attr_value = class_profile[attr]
            self.__setattr__(str("_" + attr), Stats(attr_name, value=attr_value))

    def apply_mod(self, attr, mod):
        self.__getattr__(attr).add_modifier(mod)

    @property
    def str(self):
        return self._str.value

    @str.setter
    def str(self, value):
        self._str.base_value = value
        self._is_dirty = True

    @property
    def vit(self):
        return self._vit.value

    @vit.setter
    def vit(self, value):
        self._vit.base_value = value
        self._is_dirty = True

    @property
    def agi(self):
        return self._agi.value

    @agi.setter
    def agi(self, value):
        self._agi.base_value = value
        self._is_dirty = True

    @property
    def int(self):
        return self._int.value

    @int.setter
    def int(self, value):
        self._int.base_value = value
        self._is_dirty = True

    @property
    def will(self):
        return self._will.value

    @will.setter
    def will(self, value):
        self._will.base_value = value
        self._is_dirty = True

    @property
    def lck(self):
        return self._lck.value

    @lck.setter
    def lck(self, value):
        self._lck.base_value = value
        self._is_dirty = True

    @property
    def is_dirty(self):
        return self._is_dirty


class DerivedStats:
    def __init__(self, base_stats: BaseStats = None) -> None:
        stats = {}

    def init_from_base_stats(self, base_stats: BaseStats):
        pass


class Character:
    def __init__(self, name: str = None, level: int = 1, stats_dict: dict = None):
        self._name = name

    def __repr__(self) -> str:
        return f"[Character] {self.name}\n"

    def init_stats_from_dict(self, stats_dict):
        pass

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength
