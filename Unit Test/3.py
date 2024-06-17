import unittest

class TestListEquality(unittest.TestCase):
    def test_lists_are_equal(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 5]
        self.assertListEqual(list1, list2, "The lists should be equal")

    def test_lists_are_not_equal(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [1, 2, 3, 4, 6]
        self.assertNotEqual(list1, list2, "The lists should not be equal")

    def test_empty_lists(self):
        list1 = []
        list2 = []
        self.assertListEqual(list1, list2, "Empty lists should be equal")

    def test_lists_of_different_lengths(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3, 4]
        self.assertNotEqual(list1, list2, "Lists of different lengths should not be equal")

if __name__ == '__main__':
    unittest.main()
