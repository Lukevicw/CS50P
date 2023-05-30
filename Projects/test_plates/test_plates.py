from plates import is_valid

def main():
    test_ffs()
    test_0start()
    test_long()
    test_short()
    test_symbols()
    test_mid_digit()
    test_zero()
    test_2letters()
    test_pun()


def test_ffs():
    assert is_valid("wt") == True
    assert is_valid("WTFLOL") == True
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_0start():
    assert is_valid("0wtf") == False
    assert is_valid("WTF01") == False
    assert is_valid("WTF10") == True


def test_long():
    assert is_valid("thisislong") == False

def test_short():
    assert is_valid("h") == False

def test_symbols():
    assert is_valid("H E") == False
    assert is_valid("H!.E") == False
    assert is_valid("WT.1") == False

def test_mid_digit():
    assert is_valid("W22TF") == False
    assert is_valid("WTF222") == True

def test_zero():
    assert is_valid("A02A") == False
    assert is_valid("H02A") == False

def test_2letters():
    assert is_valid("XY2") == True
    assert is_valid("X1") == False
    assert is_valid("15") == False
    assert is_valid("7X") == False

def test_pun():
    assert is_valid("A.A") == False



if __name__ == "__main__":
    main()