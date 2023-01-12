import pytest

from src.char.character import Profile


class TestProfile(object):
    @pytest.fixture
    def profile(self):
        """Returns a Stats instance with a value of 10"""

        yield Profile()

        Profile._profiles.clear()

    def test_profile_with_exiting_class(self, profile):
        Profile._profiles = {"test_class": {"str": 10, "int": 5}}
        expected = {"str": 10, "int": 5}

        actual = profile.get_profile(class_name="test_class")

        message = f"Wrong dict, expected: {expected}, actual: {actual}"
        assert actual == expected, message

    def test_profile_with_missing_class(self, profile):
        expected = ValueError
        actual = profile.get_profile(class_name="test_class")

        message = f"Wrong dict, expected: {expected}, actual: {actual}"
        assert actual == expected, message
