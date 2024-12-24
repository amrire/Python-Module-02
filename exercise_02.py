#!/usr/bin/python3


class FixedPoint:
    """
    A class to represent a fixed-point number with operator overloading.
    """
    _fractional_bits = 8  # Static constant for fractional bits

    def __init__(self, value=0):
        if isinstance(value, int):
            self._value = value << self._fractional_bits
        elif isinstance(value, float):
            self._value = round(value * (1 << self._fractional_bits))
        else:
            self._value = 0

    def get_raw_bits(self):
        return self._value

    def set_raw_bits(self, raw):
        self._value = raw

    def to_float(self):
        return self._value / (1 << self._fractional_bits)

    def to_int(self):
        return self._value >> self._fractional_bits

    def __repr__(self):
        return f"FixedPoint(value={self.to_float():.6f})"

    # Comparison operators
    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return self._value != other._value

    def __lt__(self, other):
        return self._value < other._value

    def __le__(self, other):
        return self._value <= other._value

    def __gt__(self, other):
        return self._value > other._value

    def __ge__(self, other):
        return self._value >= other._value

    # Arithmetic operators
    def __add__(self, other):
        return FixedPoint(self.to_float() + other.to_float())

    def __sub__(self, other):
        return FixedPoint(self.to_float() - other.to_float())

    def __mul__(self, other):
        return FixedPoint(self.to_float() * other.to_float())

    def __truediv__(self, other):
        if other._value == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return FixedPoint(self.to_float() / other.to_float())

    # Increment and decrement
    def increment(self):
        self._value += 1
        return self

    def decrement(self):
        self._value -= 1
        return self

    # Static methods for min and max
    @staticmethod
    def min(fp1, fp2):
        return fp1 if fp1._value < fp2._value else fp2

    @staticmethod
    def max(fp1, fp2):
        return fp1 if fp1._value > fp2._value else fp2

# Example usage
if __name__ == "__main__":
    a = FixedPoint(10.5)
    b = FixedPoint(2.75)
    print("a:", a)
    print("b:", b)
    print("a + b:", a + b)
    print("a - b:", a - b)
    print("a * b:", a * b)
    print("a / b:", a / b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("min(a, b):", FixedPoint.min(a, b))
    print("max(a, b):", FixedPoint.max(a, b))
