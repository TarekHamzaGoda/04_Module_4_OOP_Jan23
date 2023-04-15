import unittest
import Unit4_Regex


class PostCodeTester(unittest.TestCase):

    def test_Unit4_Regex(self):
        self.assertEqual(Unit4_Regex.validate_uk_postcode("M1 1AA"), True)
        self.assertEqual(Unit4_Regex.validate_uk_postcode("M60 1NW"), True)
        self.assertEqual(Unit4_Regex.validate_uk_postcode("CR2 6XH"), True)
        self.assertEqual(Unit4_Regex.validate_uk_postcode("23123123s"), True)


if __name__ == '__main__':
    unittest.main()

