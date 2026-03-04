import unittest
from src.calculators.bmi import calculate_bmi
from src.calculators.dilution import calculate_dilution

class TestCalculators(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(50, 1.60), 19.53, places=2)
        self.assertAlmostEqual(calculate_bmi(90, 1.80), 27.78, places=2)

    def test_calculate_dilution(self):
        self.assertAlmostEqual(calculate_dilution(10, 2, 5), 4.0)
        self.assertAlmostEqual(calculate_dilution(20, 1, 10), 2.0)
        self.assertAlmostEqual(calculate_dilution(5, 5, 1), 25.0)

if __name__ == '__main__':
    unittest.main()