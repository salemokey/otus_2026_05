import pytest
from src.Square import Square


@pytest.mark.parametrize(("side_a", "area"), [(3, 9), (3.5, 12.25)])
def test_square_area(side_a, area):
    r = Square(side_a)
    assert r.area == area


@pytest.mark.parametrize(("side_a", "perimeter"), [(3, 12), (3.5, 14.0)])
def test_square_perimeter(side_a, perimeter):
    r = Square(side_a)
    assert r.perimeter == perimeter
