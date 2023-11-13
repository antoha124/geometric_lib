import math
import unittest

import triangle


class TriangleAreaTestCase(unittest.TestCase):
    def test_triangle_zero_argument_area(self):
        res = triangle.area(5, 0)
        self.assertEqual(res, 0)

    def test_triangle_small_argument_area(self):
        res = triangle.area(5, 7)
        self.assertEqual(res, (5 * 7) / 2)

    def test_triangle_big_argument_area(self):
        res = triangle.area(400, 240)
        self.assertEqual(res, (400 * 240) / 2)

    def test_triangle_negative_argument_area(self):
        self.assertEqual(type(triangle.area(-5, -7)), Exception)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_triangle_zero_argument_perimeter(self):
        res = triangle.perimeter(5, 7, 0)
        self.assertEqual(res, 0)

    def test_triangle_small_argument_area(self):
        res = triangle.perimeter(5, 7, 9)
        self.assertEqual(res, 5 + 7 + 9)

    def test_triangle_big_argument_area(self):
        res = triangle.perimeter(400, 240, 170)
        self.assertEqual(res, 400 + 240 + 170)

    def test_triangle_negative_argument_area(self):
        self.assertEqual(type(triangle.perimeter(-5, -7, -9)), Exception)
