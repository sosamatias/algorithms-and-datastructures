from permutations import permutations2, permutations1
from unittest import main, TestCase


class Test(TestCase):
    def test_permutations1(self):
        assert permutations1([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [
            2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

    def test_permutations2(self):
        input1 = [2, 3]
        expected1 = [[2, 3], [3, 2]]
        result1 = permutations2(input1)
        self.assertEqual(result1, expected1)

        input2 = [1, 2, 3]
        expected2 = [[1, 2, 3], [2, 1, 3], [
            2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
        result2 = permutations2(input2)
        self.assertEqual(result2, expected2)


main()
