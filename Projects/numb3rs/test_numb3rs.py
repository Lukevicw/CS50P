from numb3rs import validate

def main():
    test_validate()


def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("cat") == False
    assert validate("1") == False
    assert validate("555.111.111.111") == False
    assert validate("111.555.111.111") == False
    assert validate("111.111.555.111") == False
    assert validate("111.111.111.555") == False

if __name__ == "__main__":
    main()