from working import convert
import pytest



def main():
    test_convert()




def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

    with pytest.raises(ValueError):
        convert("10:30 AM 7:30 PM") == ValueError

    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM") == ValueError

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM") == ValueError

    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM") == ValueError

    with pytest.raises(ValueError):
        convert("9AM to 5PM") == ValueError

    with pytest.raises(ValueError):
        convert("09:00 to 17:00") == ValueError

    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM") == ValueError