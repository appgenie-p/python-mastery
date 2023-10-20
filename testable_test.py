import os

from testable import get_var


def test_testable():
    sut = get_var()
    test_env = os.getenv("PYTHONPATH")

    assert True
