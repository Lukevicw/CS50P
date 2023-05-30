from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("AaEeIiOoUu") == ""
    assert shorten("1234567890") == "1234567890"
    assert shorten("hello") == "hll"
    assert shorten("!@#$?,.;:'") == "!@#$?,.;:'"
    #assert shorten("QWERTYUIOPASDFGHJKLZXCVBNM") == "QWRTYPSDFGHJKLZXCVBNM"

if __name__ == "__main__":
    main()
