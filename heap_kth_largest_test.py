from unittest import main, TestCase
from heap_kth_largest import Solution


class Test(TestCase):
    def test1(self):
        k = 3
        arr = [1, 3, 2, 1, 5]
        result = Solution().kth_largest(arr, k)
        expected = 2
        self.assertEqual(result, expected)

    def test2(self):
        k = 2
        arr = [1, 3, 2, 1, 5]
        result = Solution().kth_largest(arr, k)
        expected = 3
        self.assertEqual(result, expected)


main()
