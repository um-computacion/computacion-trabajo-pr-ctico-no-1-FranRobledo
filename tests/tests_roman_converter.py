import unittest
from src.roman_converter import decimal_to_roman
from src.roman_converter import roman

class TestRomanConverter(unittest.TestCase):
    def test_basic_numbers (self):
        self.assertEqual(decimal_to_roman(1), roman = "I")
        self.assertEqual(decimal_to_roman(5), roman = "V")
        self.assertEqual(decimal_to_roman(10), roman = "X")
        self.assertEqual(decimal_to_roman(50), roman = "L")
        self.assertEqual(decimal_to_roman(100), roman = "C")
        self.assertEqual(decimal_to_roman(500), roman = "D")
        self.assertEqual(decimal_to_roman(1000), roman = "M")
    def test_substraction_rules (self):
        self.assertEqual(decimal_to_roman(4), roman = "IV")
        self.assertEqual(decimal_to_roman(9), roman = "IX")
        self.assertEqual(decimal_to_roman(40), roman = "XL")
        self.assertEqual(decimal_to_roman(90), roman = "XC")
        self.assertEqual(decimal_to_roman(400), roman = "CD")
        self.assertEqual(decimal_to_roman(900), roman = "CM")
    def test_complex_number (self):
        self.assertEqual(decimal_to_roman(49), roman = "XLIX")
        self.assertEqual(decimal_to_roman(99), roman = "XCIX")
        self.assertEqual(decimal_to_roman(409), roman = "CDIX")
        self.assertEqual(decimal_to_roman(499), roman = "CDXCIX")
        self.assertEqual(decimal_to_roman(999), roman = "CMXCIX")
        self.assertEqual(decimal_to_roman(1499), roman = "MCDXCIX")
        self.assertEqual(decimal_to_roman(1999), roman = "MCMXCIX")
        self.assertEqual(decimal_to_roman(2499), roman = "MMCDXCIX")
        self.assertEqual(decimal_to_roman(2999), roman = "MMCMXCIX")
        self.assertEqual(decimal_to_roman(3499), roman = "MMMCDXCIX")
        self.assertEqual(decimal_to_roman(3999), roman = "MMMCMXCIX")


if __name__ == '__main__':
    unittest.main()