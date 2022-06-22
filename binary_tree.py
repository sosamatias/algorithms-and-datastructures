class Tree:
    def __init__(self, data):
        self.data = data
        self.left: Tree = None
        self.right: Tree = None

    def insert(self, data):
        if data > self.data:
            if not self.right:
                self.right = Tree(data)
            else:
                self.right.insert(data)
        else:
            if not self.left:
                self.left = Tree(data)
            else:
                self.left.insert(data)

    def contains(self, data) -> bool:
        if data == self.data:
            return True
        if data > self.data:
            if self.right:
                return self.right.contains(data)
            return False
        else:
            if self.left:
                return self.left.contains(data)
            return False

    def in_order(self, result):  # left, root, right
        if self.left:
            self.left.in_order(result)

        result.append(self.data)

        if self.right:
            self.right.in_order(result)

    def pre_order(self, result):  # root, left, right
        result.append(self.data)

        if self.left:
            self.left.pre_order(result)

        if self.right:
            self.right.pre_order(result)

    def post_order(self, result):  # left, right, root
        if self.left:
            self.left.post_order(result)

        if self.right:
            self.right.post_order(result)

        result.append(self.data)

    def depth(self):
        return self._depth(self, 0)

    def _depth(self, node, d):
        if node is None:
            return d

        l = self._depth(node.left, d+1)
        r = self._depth(node.right, d+1)
        return max(l, r)

    def reverse(self):
        return self._reverse(self)

    def _reverse(self, tree):
        if not tree:
            return
        temp = tree.right
        tree.right = tree.left
        tree.left = temp
        self._reverse(tree.left)
        self._reverse(tree.right)
