import unittest
from unittest.mock import patch
import leapYear
from io import StringIO

class Test_LeapYear(unittest.TestCase):
    # Test first condition that if a number is evenly divisible by 4
    # THen it is a leap year
    def test_isLeapYear4(self):
        with patch('sys.stdout', new = StringIO()) as printedMsg:
            yearInput = 2012
            leapYear.LeapYear(2012)
            result = (printedMsg.getvalue()).replace('\n','')
            self.assertEqual(result, "2012 is a leap year.")

    def test_notLeapYear_4and100(self):
        with patch('sys.stdout', new = StringIO()) as printedMsg:
            yearInput = 2100
            leapYear.LeapYear(2100)
            result = (printedMsg.getvalue()).replace('\n','')
            self.assertEqual(result, "2100 is not a leap year.")

if __name__ == '__main__':
    unittest.main()
