# Python Module 02: Mastering Class Design and Operator Overloading

## Overview

This module introduces fundamental concepts in Python class design, emphasizing structured programming and operator overloading. Through hands-on exercises, you will learn how to design robust classes, implement useful operations, and build reusable components.

## Learning Objectives

- Understand the importance of structured class design.
- Explore the concept of fixed-point numbers.
- Implement operator overloading for custom classes.
- Work with 2D points and algorithms to solve geometric problems.

## Exercises

### Exercise 00: My First Class in Canonical Form
- **Goal**: Create a Python class representing a fixed-point number.
- **Key Features**:
  - Default constructor to initialize a fixed-point number to `0`.
  - Methods to get and set raw values.
  - Proper encapsulation using private attributes.

### Exercise 01: Towards a More Useful Fixed-Point Class
- **Goal**: Enhance the fixed-point class by adding new constructors and conversion methods.
- **Key Features**:
  - Constructors to handle integer and floating-point inputs.
  - Methods to convert fixed-point numbers to integers and floats.
  - Overload `__str__` for user-friendly output.

### Exercise 02: Operator Overloading
- **Goal**: Extend the fixed-point class to support comparison and arithmetic operations.
- **Key Features**:
  - Overload comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`).
  - Overload arithmetic operators (`+`, `-`, `*`, `/`).
  - Static methods to return the minimum and maximum of two fixed-point numbers.

### Exercise 03: Point Inside Triangle (BSP)
- **Goal**: Implement a function to check if a point lies inside a triangle.
- **Key Features**:
  - Create a `Point` class with immutable coordinates.
  - Use geometric algorithms to determine inclusion.
  - Handle edge cases such as points on the triangle's edges or vertices.

## Requirements

- Python 3.7+
- Familiarity with object-oriented programming concepts.
- Basic understanding of geometric algorithms (for Exercise 03).

## Resources

- [Understanding Floating-Point Numbers](http://www.cprogramming.com/tutorial/floating_point/understanding_floating_point.html)
- [Python’s math module](https://docs.python.org/3/library/math.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Triangle Point Inclusion Algorithm](https://en.wikipedia.org/wiki/Point_in_polygon)

## Author

This module is designed to guide you through advanced Python class design and operator overloading. Happy coding!
