from palindrome import longest_palindrome

import unittest

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s0='girafarig'
        self.s1='abccba'
    def test_palindrome(self) -> None:
        self.assertEqual(longest_palindrome(self.s0), len(self.s0))
        self.assertEqual(longest_palindrome(self.s1), len(self.s1))

if __name__=='__main__':
    unittest.main()