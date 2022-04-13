from dimension import dimensions


def test_dimensions():
    d = dimensions(4, 5)
    assert d.computer_dimension() == 20

    d = dimensions(3, 2)
    assert d.computer_dimension() == 6
