import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculator.calculate(100000, 12, 12, 1)[0]['amount'], '112000')
        self.assertEqual(calculator.calculate(100000, 12, 12, 12)[11]['amount'], '112682.50')
        self.assertEqual(calculator.calculate(100000, 12, 12, 4)[1]['income'], '6090.00')
        self.assertEqual(calculator.calculate(100000, 12, 12, 2)[0]['number'], '6')


class TestApp(unittest.TestCase):
    def test_index(self):
        ...


    def test_calculate(self):
        ...