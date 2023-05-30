from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jardep = Jar()
    jardep.deposit(5)
    assert jardep.size == 5
    jardep.deposit(5)
    assert jardep.size == 10


def test_withdraw():
    jarwith = Jar()
    jarwith.deposit(10)
    jarwith.withdraw(5)
    assert jarwith.size == 5
    jarwith.withdraw(2)
    assert jarwith.size == 3
    ...