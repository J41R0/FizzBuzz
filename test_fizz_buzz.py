import unittest
from fizz_buzz import fizz_buzz_game


class FizzBuzzTest(unittest.TestCase):
    def test_input(self):
        # testing integer input only
        res = fizz_buzz_game("test")
        self.assertEqual("Invalid data type", res)
        res = fizz_buzz_game(1.234)
        self.assertEqual("Invalid data type", res)

    def test_numbers(self):
        # testing regular numbers
        res = fizz_buzz_game(1)
        self.assertEqual(1, res)
        res = fizz_buzz_game(7)
        self.assertEqual(7, res)
        res = fizz_buzz_game(2222)
        self.assertEqual(2222, res)

    def test_fizz(self):
        # testing numbers divisible by 3
        res = fizz_buzz_game(3)
        self.assertEqual('Fizz', res)
        res = fizz_buzz_game(9)
        self.assertEqual('Fizz', res)
        res = fizz_buzz_game(27351)
        self.assertEqual('Fizz', res)

    def test_buzz(self):
        # testing numbers divisible by 5
        res = fizz_buzz_game(5)
        self.assertEqual('Buzz', res)
        res = fizz_buzz_game(20)
        self.assertEqual('Buzz', res)
        res = fizz_buzz_game(1000)
        self.assertEqual('Buzz', res)

    def test_fizz_buzz(self):
        # testing numbers divisible by 3 and 5
        res = fizz_buzz_game(15)
        self.assertEqual('FizzBuzz', res)
        res = fizz_buzz_game(90)
        self.assertEqual('FizzBuzz', res)
        res = fizz_buzz_game(7320)
        self.assertEqual('FizzBuzz', res)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
