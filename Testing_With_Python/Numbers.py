class Numbers:

    def fizzBuzz(self, number):
        if number % 5 == 0 and number % 3 == 0:
            return "fizzbuzz"
        elif number % 5 == 0:
            return "fizz"
        elif number % 3 == 0:
            return "buzz"
        return "blah"


