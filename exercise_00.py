#!/usr/bin/python3


class FixedPoint:
    """
    A class to represent a fixed-point number in canonical form.
    """
    _fractional_bits = 8  # Static constant for fractional bits

    def __init__(self):
        """
        Default constructor initializing the fixed-point number to 0.
        """
        self._value = 0  # Private attribute to store the fixed-point value
        print("Default constructor called")

    def get_raw_bits(self):
        """
        Get the raw value of the fixed-point number.
        """
        print("get_raw_bits called")
        return self._value

    def set_raw_bits(self, raw):
        """
        Set the raw value of the fixed-point number.

        :param raw: The raw value to set.
        """
        print("set_raw_bits called")
        self._value = raw

    def __repr__(self):
        """
        String representation of the FixedPoint object.
        """
        return f"FixedPoint(value={self._value})"

# Example usage
if __name__ == "__main__":
    a = FixedPoint()
    print(a)
    a.set_raw_bits(42)
    print(a.get_raw_bits())
    print(a)
