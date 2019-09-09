import lib2.app


def test_two():
    assert lib2.app.add_args([1, 2]) == 3


def test_three():
    assert lib2.app.add_args([1, 2, 3]) == 6
