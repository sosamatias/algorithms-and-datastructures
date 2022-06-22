from unittest import main, TestCase
from depth_first_search import Node, dfs_iterative, dfs_recursive


class TestSolution(TestCase):
    def setUp(self):
        self.head = Node(4)
        node2 = Node(2)
        self.head.left = node2
        node6 = Node(6)
        self.head.right = node6
        node2.left = Node(1)
        node2.right = Node(3)
        node6.left = Node(5)
        node6.right = Node(7)
        """
             4
           /   \
          2     6
         / \   / \
        1   3 5   7 
        """

    def test_dfs_recursive(self):
        result = []
        dfs_recursive(self.head, result)
        self.assertEqual(result, [4, 2, 1, 3, 6, 5, 7])

    def test_dfs_iterative(self):
        result = []
        dfs_iterative(self.head, result)
        self.assertEqual(result, [4, 2, 1, 3, 6, 5, 7])


main()
