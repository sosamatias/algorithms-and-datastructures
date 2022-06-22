from unittest import main, TestCase
from queue import Queue


class Test(TestCase):

    def test1(self):
        s = Queue()
        self.assertEqual(s.dequeue(), None)
        s.enqueue(1)
        s.enqueue(2)
        s.enqueue(3)
        self.assertEqual(s.dequeue(), 1)
        self.assertEqual(s.dequeue(), 2)
        self.assertEqual(s.dequeue(), 3)
        self.assertEqual(s.dequeue(), None)


main()
