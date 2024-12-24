#!/usr/bin/python3
import math


class FixedPoint:
    """
    A class to represent a fixed-point number with extended functionality.
    """
    _fractional_bits = 8  # Static constant for fractional bits

    def __init__(self, value=0):
        """
        Constructor that accepts an integer, a float, or initializes to 0.

        :param value: Integer or float to initialize the fixed-point value.
        """
        if isinstance(value, int):
            self._value = value << self._fractional_bits
            print("Integer constructor called")
        elif isinstance(value, float):
            self._value = round(value * (1 << self._fractional_bits))
            print("Float constructor called")
        else:
            self._value = 0
            print("Default constructor called")

    def get_raw_bits(self):
        """
        Get the raw value of the fixed-point number.
        """
        return self._value

    def set_raw_bits(self, raw):
        """
        Set the raw value of the fixed-point number.

        :param raw: The raw value to set.
        """
        self._value = raw

    def to_float(self):
        """
        Convert the fixed-point value to a floating-point number.
        """
        return self._value / (1 << self._fractional_bits)

    def to_int(self):
        """
        Convert the fixed-point value to an integer.
        """
        return self._value >> self._fractional_bits

    def __repr__(self):
        """
        String representation of the FixedPoint object.
        """
        return f"FixedPoint(value={self.to_float():.6f})"

    def __str__(self):
        """
        User-friendly string representation of the FixedPoint object.
        """
        return str(self.to_float())


# Example usage
if __name__ == "__main__":
    a = FixedPoint()
    b = FixedPoint(10)
    c = FixedPoint(42.42)
    print("a:", a)
    print("b:", b)
    print("c:", c)
    a.set_raw_bits(1234)
    print("Raw bits of a:", a.get_raw_bits())
    print("a as float:", a.to_float())
    print("a as integer:", a.to_int())