from unittest import main, TestCase
from fibonacci import fibonacci_iterative, fibonacci_recursive, fibonacci_recursive_memo


class Test(TestCase):
    def test_fibonacci(self):
        for fibo in [fibonacci_iterative, fibonacci_recursive, fibonacci_recursive_memo]:
            self.assertEqual(fibo(1), 0)
            self.assertEqual(fibo(2), 1)
            self.assertEqual(fibo(3), 1)
            self.assertEqual(fibo(4), 2)
            self.assertEqual(fibo(5), 3)
            self.assertEqual(fibo(6), 5)
            self.assertEqual(fibo(7), 8)
            self.assertEqual(fibo(8), 13)
            self.assertEqual(fibo(9), 21)


main()
