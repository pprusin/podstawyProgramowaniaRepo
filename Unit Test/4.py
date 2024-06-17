import unittest

def is_palindrome(s):
    return  s

class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("madam"), "Simple palindrome test failed")
        
    def test_mixed_case_palindrome(self):
        self.assertTrue(is_palindrome("MadAm"), "Mixed case palindrome test failed")
        
    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"), "Palindrome with spaces test failed")
        
    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome("Able was I, ere I saw Elba!"), "Palindrome with punctuation test failed")
        
    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("Hello world"), "Non-palindrome test failed")
        
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""), "Empty string test failed")
        
    def test_single_character_string(self):
        self.assertTrue(is_palindrome("a"), "Single character palindrome test failed")
        
    def test_numeric_palindrome(self):
        self.assertTrue(is_palindrome("12321"), "Numeric palindrome test failed")

if __name__ == '__main__':
    unittest.main()
