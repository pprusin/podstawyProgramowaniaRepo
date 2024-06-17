import unittest

def parse_and_validate(input_data):
    if not isinstance(input_data, dict):
        return False, "Invalid input type"
    
    if 'name' not in input_data or not isinstance(input_data['name'], str) or not input_data['name']:
        return False, "Invalid or missing 'name'"
    
    if 'age' not in input_data or not isinstance(input_data['age'], int) or input_data['age'] <= 0:
        return False, "Invalid or missing 'age'"
    
    return True, "Valid input"

class TestParseAndValidate(unittest.TestCase):
    def test_valid_input(self):
        input_data = {'name': 'John Doe', 'age': 30}
        valid, message = parse_and_validate(input_data)
        self.assertTrue(valid)
        self.assertEqual(message, "Valid input")
    
    def test_invalid_type(self):
        input_data = "Not a dictionary"
        valid, message = parse_and_validate(input_data)
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid input type")

    def test_missing_name(self):
        input_data = {'age': 30}
        valid, message = parse_and_validate(input_data)
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid or missing 'name'")
    
    def test_invalid_name(self):
        input_data = {'name': '', 'age': 30}
        valid, message = parse_and_validate(input_data)
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid or missing 'name'")
    
    def test_missing_age(self):
        input_data = {'name': 'John Doe'}
        valid, message = parse_and_validate(input_data)
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid or missing 'age'")
    
    def test_invalid_age(self):
        input_data = {'name': 'John Doe', 'age': -5}
        valid, message = parse_and_validate(input_data)
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid or missing 'age'")

    def test_invalid_age_type(self):
        input_data = {'name': 'John Doe', 'age': 'thirty'}
        valid, message = parse_and_validate(input_data)
        self.assertFalse(valid)
        self.assertEqual(message, "Invalid or missing 'age'")

if __name__ == '__main__':
    unittest.main()
