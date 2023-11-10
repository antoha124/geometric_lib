import math
import unittest

import circle, rectangle, square, triangle


class CircleAreaTestCase(unittest.TestCase):
    def test_circle_zero_argument_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_circle_small_argument_area(self):
        res = circle.area(5)
        self.assertEqual(res, 5 * 5 * math.pi)

    def test_circle_big_argument_area(self):
        res = circle.area(400)
        self.assertEqual(res, 400 * 400 * math.pi)

    def test_circle_negative_argument_area(self):
        res = circle.area(-5)
        self.assertEqual(res, 0)


class RectangleAreaTestCase(unittest.TestCase):
    def test_rectangle_zero_argument_area(self):
        res = rectangle.area(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_small_argument_area(self):
        res = rectangle.area(5, 7)
        self.assertEqual(res, 5 * 7)

    def test_rectangle_big_argument_area(self):
        res = rectangle.area(400, 240)
        self.assertEqual(res, 400 * 240)

    def test_rectangle_negative_argument_area(self):
        res = rectangle.area(-5, 240)
        self.assertEqual(res, 0)


class SquareAreaTestCase(unittest.TestCase):
    def test_square_zero_argument_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_small_argument_area(self):
        res = square.area(5)
        self.assertEqual(res, 5 * 5)

    def test_square_big_argument_area(self):
        res = square.area(400)
        self.assertEqual(res, 400 * 400)

    def test_square_negative_argument_area(self):
        res = square.area(-5)
        self.assertEqual(res, 0)


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
        res = triangle.area(-5, -7)
        self.assertEqual(res, 0)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_circle_zero_argument_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_small_argument_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2 * 5 * math.pi)

    def test_circle_big_argument_perimeter(self):
        res = circle.perimeter(400)
        self.assertEqual(res, 2 * 400 * math.pi)

    def test_circle_negative_argument_perimeter(self):
        res = circle.perimeter(-5)
        self.assertEqual(res, 0)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_rectangle_zero_argument_perimeter(self):
        res = rectangle.perimeter(5, 0)
        self.assertEqual(res, 0)

    def test_rectangle_small_argument_perimeter(self):
        res = rectangle.perimeter(5, 7)
        self.assertEqual(res, 2 * 5 + 2 * 7)

    def test_rectangle_big_argument_perimeter(self):
        res = rectangle.perimeter(400, 240)
        self.assertEqual(res, 2 * 400 + 2 * 240)

    def test_rectangle_negative_argument_perimeter(self):
        res = rectangle.perimeter(-5, -7)
        self.assertEqual(res, 0)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_square_zero_argument_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_small_argument_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 4 * 5)

    def test_square_big_argument_perimeter(self):
        res = square.perimeter(400)
        self.assertEqual(res, 4 * 400)

    def test_square_negative_argument_perimeter(self):
        res = square.perimeter(-5)
        self.assertEqual(res, 0)


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
        res = triangle.perimeter(-5, -7, -9)
        self.assertEqual(res, 0)
