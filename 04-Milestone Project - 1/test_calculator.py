import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).with_name("calculator.py")
spec = importlib.util.spec_from_file_location("calculator", MODULE_PATH)
calculator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculator)


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(calculator.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(8, 0)


if __name__ == "__main__":
    unittest.main()
