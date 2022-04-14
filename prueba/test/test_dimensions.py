from dimension import dimensions


def test__class_dimensions():
    assert 20 == dimensions(4, 5)
    assert dimensions(3, 2) == 6
