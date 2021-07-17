  
import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.script_clean_dataset import fix_missing_ffill


class TestCases(unittest.TestCase):
    def fix_missing_ffill(self):
        """
        Test that it fix missing value for  a given list
        """
        data = [1, 'NaN', 3,4]
        result = fix_missing_ffill(data)
        self.assertEqual(result, 3)

    

if __name__ == '__main__':
    unittest.main()
