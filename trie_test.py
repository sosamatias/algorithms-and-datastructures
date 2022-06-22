from trie import Trie
from unittest import main, TestCase


class Test(TestCase):
    def test1(self):
        words = [
            'dog', 'dark', 'cat', 'door', 'doge'
        ]

        t = Trie()
        for w in words:
            t.add_word(w)

        result = t.search('do')
        self.assertEqual(result, ['dog', 'doge', 'door'])


main()
