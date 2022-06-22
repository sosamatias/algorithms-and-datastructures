from unittest import TestCase, main
from binary_search import Solution


class Test(TestCase):
    def test_empty(self):
        arr = []
        target = 3
        expected = -1
        result = Solution().binary_search(arr, target)
        self.assertEqual(result, expected)

    def test_even_arr(self):
        arr = [1, 2, 3, 4]
        target = 3
        expected = 2
        result = Solution().binary_search(arr, target)
        self.assertEqual(result, expected)

    def test_odd_arr(self):
        arr = [1, 2, 3, 4, 5]
        target = 3
        expected = 2
        result = Solution().binary_search(arr, target)
        self.assertEqual(result, expected)

    def test_target_last(self):
        arr = [1, 2, 3, 4, 5]
        target = 5
        expected = 4
        result = Solution().binary_search(arr, target)
        self.assertEqual(result, expected)

    def test_target_first(self):
        arr = [1, 2, 3, 4, 5]
        target = 1
        expected = 0
        result = Solution().binary_search(arr, target)
        self.assertEqual(result, expected)


main()
