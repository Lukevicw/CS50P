from bank import value

"""def main():
    test_hello()
    test_what()
    test_upper()
    test_h()"""


def test_hello():
    assert value("hello") == 0

def test_what():
    assert value("what's up?") == 100

def test_upper():
    assert value("Hello") == 0

def test_h():
    assert value("hey") == 20

"""
if __name__ == "__main__":
    main()
"""