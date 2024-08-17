from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    try:
        jar = Jar(-1)
    except ValueError:
        assert True
    else:
        assert False

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    try:
        jar.deposit(3)
    except ValueError:
        assert True
    else:
        assert False

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

    try:
        jar.withdraw(3)
    except ValueError:
        assert True
    else:
        assert False

def test_capacity():
    jar = Jar(15)
    assert jar.capacity == 15

def test_size():
    jar = Jar(5)
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
