from quicksort import quicksort
from unittest import main, TestCase


class Test(TestCase):
    def test1(self):
        input = [1, 3, 4, 2, 5, 8, 6, 7, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = quicksort(input)
        self.assertEqual(result, expected)


main()
