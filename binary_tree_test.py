from unittest import main, TestCase
from binary_tree import Tree

"""
   testing
      22
   /      \
  15      25       
 /  \    /  \
10  20  23  40

in_order = [10, 15, 20, 22, 23, 25, 40]
pre_order = [22, 15, 10, 20, 25, 23, 40]
post_order = [10, 20, 15, 23, 40, 25, 22]
"""


class Test(TestCase):
    def setUp(self):
        t = Tree(22)
        self.values = [15, 25, 10, 20, 23, 40]
        for value in self.values:
            t.insert(value)
        self.tree = t

    def test_insert(self):
        self.assertEqual(self.tree.contains(22), True)
        for value in self.values:
            self.assertEqual(self.tree.contains(value), True)

        self.assertEqual(self.tree.contains(19), False)
        self.assertEqual(self.tree.contains(32), False)
        self.assertEqual(self.tree.contains(11), False)

    def test_in_order(self):
        result = []
        self.tree.in_order(result)
        in_order = [10, 15, 20, 22, 23, 25, 40]
        self.assertEqual(len(in_order), len(result))
        for i in range(len(in_order)):
            self.assertEqual(in_order[i], result[i])

    def test_pre_order(self):
        result = []
        self.tree.pre_order(result)
        pre_order = [22, 15, 10, 20, 25, 23, 40]
        self.assertEqual(len(pre_order), len(result))
        for i in range(len(pre_order)):
            self.assertEqual(pre_order[i], result[i])

    def test_post_order(self):
        result = []
        self.tree.post_order(result)
        post_order = [10, 20, 15, 23, 40, 25, 22]
        self.assertEqual(len(post_order), len(result))
        for i in range(len(post_order)):
            self.assertEqual(post_order[i], result[i])

    def test_depth(self):
        root = Tree(10)
        root.left = Tree(8)
        root.right = Tree(15)
        root.left.left = Tree(4)
        root.left.left.right = Tree(5)
        root.left.left.right.right = Tree(6)
        root.right.left = Tree(14)
        root.right.right = Tree(16)
        expected = 5
        output = root.depth()
        self.assertEqual(expected, output)

    def test_reverse(self):
        tree = Tree(5)
        tree.left = Tree(2)
        tree.right = Tree(7)
        tree.right.left = Tree(6)
        tree.right.right = Tree(8)

        tree.reverse()
        self.assertEqual(tree.right.data, 2)
        self.assertEqual(tree.left.data, 7)
        self.assertEqual(tree.left.right.data, 6)
        self.assertEqual(tree.left.left.data, 8)


main()
