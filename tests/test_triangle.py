from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"), [(3, 4, 5, 6)])
def test_triangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == area


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimeter"), [(3, 4, 5, 12)])
def test_triangle_perimeter(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter
