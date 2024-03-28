import unittest

class TestShuffleSort(unittest.TestCase):
    
    def test_shuffle(self):
        original_list = [1, 2, 3, 4, 5]
        shuffled_list = custom_shuffle(original_list)
        self.assertNotEqual(original_list, shuffled_list)
        self.assertEqual(sorted(original_list), sorted(shuffled_list))

    def test_remove_duplicates(self):
        lst_with_duplicates = [1, 2, 2, 3, 3, 4, 5, 5]
        unique_lst = remove_duplicates(lst_with_duplicates)
        self.assertEqual(unique_lst, [1, 2, 3, 4, 5])

    def test_sort_list(self):
        unsorted_list = [5, 3, 1, 4, 2]
        sorted_list = sort_list(unsorted_list)
        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
