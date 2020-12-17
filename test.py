import unittest
from calculator import calc


class TestProgression(unittest.TestCase):
    calculator = calc(2.56)

    def test_add__(self):
        self.assertEqual(self.calculator.add(3), 5.5600000000000005)
        self.assertEqual(self.calculator.add(2.44), 5)
        self.assertTrue(self.calculator.add(487), isinstance(self.calculator.add(487), float))

    def test_sub__(self):
        self.assertEqual(self.calculator.sub(2), 0.56)
        self.assertEqual(self.calculator.sub(1), 1.56)

    def test_mul__(self):
        self.assertEqual(self.calculator.mul(2), 5.12)
        self.assertEqual(self.calculator.mul(4), 10.24)

if __name__ == '__main__':
    unittest.main()
