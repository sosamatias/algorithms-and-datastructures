from unittest import main, TestCase
from stack import Stack


class Test(TestCase):
    def test1(self):
        s = Stack()
        self.assertEqual(s.pop(), None)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), None)


main()
