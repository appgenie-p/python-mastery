import pytest

from e85_multitask import count_down, count_up, main


def test_count_down():
    # Test count_down with n=5
    gen = count_down(5)
    assert list(gen) == [5, 4, 3, 2, 1]

    # Test count_down with n=0
    gen = count_down(0)
    with pytest.raises(StopIteration):
        next(gen)


def test_count_up():
    # Test count_up with n=5
    gen = count_up(5)
    assert list(gen) == [0, 1, 2, 3, 4]

    # Test count_up with n=0
    gen = count_up(0)
    with pytest.raises(StopIteration):
        next(gen)


def test_main():
    gen_round = main()
    assert gen_round == [5, 0, 4, 1, 3, 2, 2, 3, 1, 4]
