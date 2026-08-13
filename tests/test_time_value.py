from src.finance.time_value import (
    future_value,
    present_value,
    real_return
)


def test_future_value():
    result = future_value(10000, 0.08, 5)
    assert round(result, 2) == 14693.28


def test_present_value():
    result = present_value(20000, 0.07, 5)
    assert round(result, 2) == 14259.72


def test_real_return():
    result = real_return(0.10, 0.04)
    assert round(result, 4) == 0.0577
