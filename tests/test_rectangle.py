import pytest
from src.Rectangle import Rectangle


@pytest.mark.parametrize(("side_a", "side_b", "area"), [(3, 5, 15), (3.5, 5.5, 19.25)])
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"), [(3, 5, 16), (3.5, 5.5, 18)]
)
def test_rectagle_perimeter(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter
