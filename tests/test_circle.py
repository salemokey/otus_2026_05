import pytest
from src.Circle import Circle


@pytest.mark.parametrize(("rad", "area"), [(3, 28.27)])
def test_circle_area(rad, area):
    c = Circle(rad)
    assert c.area == area


@pytest.mark.parametrize(("rad", "perimeter"), [(3, 18.85)])
def test_circle_perimeter(rad, perimeter):
    c = Circle(rad)
    assert c.perimeter == perimeter
