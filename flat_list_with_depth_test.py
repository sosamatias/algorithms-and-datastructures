from unittest import main, TestCase
from flat_list_with_depth import flat_recursive, flat_iterative


class Test(TestCase):
    def setUp(self):
        self.input = [5, [6, [7, 8], 4], 3]
        self.expected = [(1, 5), (2, 6), (3, 7), (3, 8), (2, 4), (1, 3)]

    def test_flat_recursive(self):
        result = []
        flat_recursive(self.input, result)
        self.assertEqual(result, self.expected)

    def test_flat_iterative(self):
        result = []
        flat_iterative(self.input, result)
        self.assertEqual(result, self.expected)


main()
