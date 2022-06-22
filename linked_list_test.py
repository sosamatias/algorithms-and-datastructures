from unittest import main, TestCase
from linked_list import LinkedList, Node


class Test(TestCase):
    def setUp(self):
        ll = LinkedList()
        ll.push(1)
        ll.push(2)
        ll.push(3)
        ll.push(4)
        self.llist = ll

    def test_no_loop(self):
        self.assertFalse(self.llist.detectLoop())
        self.assertFalse(self.llist.detectLoopFlag())

    def test_loop(self):
        # generate a loop
        self.llist.head.next.next.next.next = self.llist.head
        self.assertTrue(self.llist.detectLoop())
        self.assertTrue(self.llist.detectLoopFlag())

    def test_reverse(self):
        input = Node('a', Node('b', Node('c')))
        expected = Node('c', Node('b', Node('a')))
        l = LinkedList(input)
        result = l.reverse()
        while result:
            self.assertEqual(expected.data, result.data)
            expected = expected.next
            result = result.next


main()
