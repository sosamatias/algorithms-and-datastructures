from unittest import main, TestCase
from combinations import combinations


class Test(TestCase):
    def test1(self):
        input = [2, 3]
        expected = [[2, 3], [2], [3], []]
        result = combinations(input)
        self.assertEqual(expected, result)

    def test2(self):
        input = [1, 2, 3]
        expected = [[1, 2, 3], [1, 2],
                    [1, 3], [1], [2, 3], [2], [3], []]
        result = combinations(input)
        self.assertEqual(expected, result)


main()
