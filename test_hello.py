from hello import add, sub


def test_add():
    assert 55 == add(25, 30)
    assert 5 == add(2, 3)


def test_sub():
    assert 10 == sub(11, 1)
