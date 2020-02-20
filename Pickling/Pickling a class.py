import pickle


class Car:
    def __init__(self, model, colour, year, worth):
        self.model = model
        self.colour = colour
        self.year = year
        self.worth = worth

    def __repr__(self):
        return " This {} is from {} and it's {} in colour ".format(self.model, self.year, self.colour)

    def value(self, summ=1000):
        depreciation = self.worth - summ
        return depreciation


# toyota = Car('Auris', 'red', 2008, 10000)
"""now we will pickle the class into a file, and serialze the date, converting it into a byte stream and we can pull it back out
 and turn it into whatever it was before"""

"""with open('machine.pickle', 'wb') as file:
    we're writing binary so we have to add the b next to w
    result = pickle.dump(toyota, file)
    print(result)"""

"""to unpickle, or pull the coade back out"""
with open('machine.pickle', 'rb')as file:
    res = pickle.load(file)
    print(res)
    print(res.value())