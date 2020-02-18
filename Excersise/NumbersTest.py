import unittest
from Excersise.Numbers import Numbers


class NumbersTest(unittest.TestCase):
    def setUp(self):
        self.numbers = Numbers()

    def testFizz(self):
        self.assertEqual("fizz",self.numbers.fizzBuzz(5))

    def testFizzForHigherNumber(self):
        self.assertEqual("fizz",self.numbers.fizzBuzz(100010))

    def testFizzBuzz(self):
        self.assertEqual(self.numbers.fizzBuzz(15),"fizzbuzz")

    def testBuzz(self):
        self.assertEqual(self.numbers.fizzBuzz(9),"buzz")

