#!/usr/bin/python3


class FixedPoint:
    """
    A class to represent a fixed-point number with operator overloading.
    """
    _fractional_bits = 8

    def __init__(self, value=0):
        if isinstance(value, int):
            self._value = value << self._fractional_bits
        elif isinstance(value, float):
            self._value = round(value * (1 << self._fractional_bits))
        else:
            self._value = 0

    def to_float(self):
        return self._value / (1 << self._fractional_bits)

    def __sub__(self, other):
        return FixedPoint(self.to_float() - other.to_float())

    def __mul__(self, other):
        return FixedPoint(self.to_float() * other.to_float())

class Point:
    """
    A class to represent a 2D point using FixedPoint numbers.
    """
    def __init__(self, x=0, y=0):
        self.x = FixedPoint(x)
        self.y = FixedPoint(y)

    def __repr__(self):
        return f"Point(x={self.x.to_float():.2f}, y={self.y.to_float():.2f})"


def cross_product(a, b):
    """
    Calculate the cross product of two points.
    """
    return (a.x * b.y).to_float() - (a.y * b.x).to_float()


def bsp(a, b, c, point):
    """
    Determine if a point is inside a triangle defined by points a, b, and c.

    :param a: First vertex of the triangle.
    :param b: Second vertex of the triangle.
    :param c: Third vertex of the triangle.
    :param point: The point to check.
    :return: True if the point is inside the triangle, False otherwise.
    """
    # Calculate vectors
    ab = Point(b.x.to_float() - a.x.to_float(), b.y.to_float() - a.y.to_float())
    ac = Point(c.x.to_float() - a.x.to_float(), c.y.to_float() - a.y.to_float())
    ap = Point(point.x.to_float() - a.x.to_float(), point.y.to_float() - a.y.to_float())
    # Compute cross products
    cross1 = cross_product(ab, ac)
    cross2 = cross_product(ab, ap)
    cross3 = cross_product(ap, ac)
    if cross1 == 0 or cross2 == 0 or cross3 == 0:
        return False  # On the edge or vertex
    # Check if the point is inside
    return (cross2 > 0 and cross3 > 0 and (cross2 + cross3) <= cross1) or (cross2 < 0 and cross3 < 0 and (cross2 + cross3) >= cross1)

# Example usage
if __name__ == "__main__":
    a = Point(0, 0)
    b = Point(4, 0)
    c = Point(2, 3)
    p_inside = Point(2, 1)
    p_outside = Point(5, 5)
    print("Triangle vertices:", a, b, c)
    print("Point inside:", p_inside, "->", bsp(a, b, c, p_inside))
    print("Point outside:", p_outside, "->", bsp(a, b, c, p_outside))
