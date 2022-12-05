import pytest
import os
from utils import record


class Tests:
    def test_name_type_error(self):
        with pytest.raises(TypeError) as t:
            record.record(name=["test"])

        expected_val = "Name of the file should be a string."
        actual_val = str(t.value)

        assert expected_val == actual_val

    def test_name_length_error(self):
        with pytest.raises(OverflowError) as o:
            record.record(name="a"*256)

        expected_val = "File name should be shorter than 255 characters."
        actual_val = str(o.value)

        assert expected_val == actual_val

    def test_negative_duration_error(self):
        with pytest.raises(ValueError) as v:
            record.record(duration=-1)

        expected_val = "Duration should be integer larger than zero."
        actual_val = str(v.value)

        assert expected_val == actual_val

    def test_too_long_duration_error(self):
        with pytest.raises(NotImplementedError) as ni:
            record.record(duration=61)

        expected_val = "Duration larger than 60 seconds is not supported."
        actual_val = str(ni.value)

        assert expected_val == actual_val
