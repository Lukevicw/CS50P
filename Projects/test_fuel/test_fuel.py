from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    #test_zero()


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("one/two")
    with pytest.raises(ZeroDivisionError):
        convert("1/0") == ZeroDivisionError


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()
