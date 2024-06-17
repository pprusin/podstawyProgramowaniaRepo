def is_sorted_ascending(lst):
    """Check if a list is sorted in ascending order."""
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

import unittest

def is_sorted_ascending(lst):
    """Check if a list is sorted in ascending order."""
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

class TestIsSortedAscendingFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(is_sorted_ascending([]), "An empty list should be considered sorted")

    def test_single_element_list(self):
        self.assertTrue(is_sorted_ascending([1]), "A single element list should be considered sorted")

    def test_sorted_list(self):
        self.assertTrue(is_sorted_ascending([1, 2, 3, 4, 5]), "A sorted list should be considered sorted")

    def test_unsorted_list(self):
        self.assertFalse(is_sorted_ascending([5, 3, 1, 4, 2]), "An unsorted list should not be considered sorted")

    def test_sorted_with_duplicates(self):
        self.assertTrue(is_sorted_ascending([1, 2, 2, 3, 4]), "A sorted list with duplicates should be considered sorted")

    def test_unsorted_with_duplicates(self):
        self.assertFalse(is_sorted_ascending([1, 2, 2, 3, 2]), "An unsorted list with duplicates should not be considered sorted")

    def test_sorted_negative_numbers(self):
        self.assertTrue(is_sorted_ascending([-3, -2, -1, 0, 1]), "A sorted list with negative numbers should be considered sorted")

    def test_unsorted_negative_numbers(self):
        self.assertFalse(is_sorted_ascending([-1, -2, -3, 0, 1]), "An unsorted list with negative numbers should not be considered sorted")

    def test_sorted_large_numbers(self):
        self.assertTrue(is_sorted_ascending([1000, 1001, 1002, 1003]), "A sorted list with large numbers should be considered sorted")

    def test_unsorted_large_numbers(self):
        self.assertFalse(is_sorted_ascending([1003, 1002, 1001, 1000]), "An unsorted list with large numbers should not be considered sorted")

if __name__ == '__main__':
    unittest.main()
