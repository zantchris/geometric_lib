import unittest
import math
import square
import rectangle
import circle
import triangle

class TestGeometryFunctions(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square.area(7), 49)
        self.assertEqual(square.area(0), 0)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(7), 28)

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(6, 8), 48)
        self.assertEqual(rectangle.area(0, 8), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(6, 8), 28)

    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(4), math.pi * 16)
        self.assertEqual(circle.area(0), 0)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(4), 2 * math.pi * 4)

    def test_triangle_area(self):
        self.assertEqual(triangle.area(9, 0), 0)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 12, 13), 30)

if __name__ == '__main__':
    unittest.main()
