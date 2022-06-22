from unittest import main, TestCase
from collections import deque
from mergesort import mergesort, _merge


class Test(TestCase):
    def test_mergesort_1(self):
        input = [3, 2, 1, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(mergesort(input), expected)

    def test_mergesort_2(self):
        input = [3, 2, 1, 4]
        expected = [1, 2, 3, 4]
        self.assertEqual(mergesort(input), expected)

    def test_mergesort_3(self):
        input = [3]
        expected = [3]
        self.assertEqual(mergesort(input), expected)

    def test_merge(self):
        a = deque([1, 3, 5, 7])
        b = deque([2, 4, 6])
        expected = [1, 2, 3, 4, 5, 6, 7]
        result = _merge(a, b)
        self.assertEqual(result, expected)


main()
