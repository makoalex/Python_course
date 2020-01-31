# INHERITANCE  allows us to build a class that inherits functionality from another class
# called base or parent class . IN PYTHIN WE PASS THE BASE CLASS AS AN ARGUMENT TO THE CHILD CLASS
from math import ceil


class Us:
    cute = True

    def __init__(self, name):
        self.name = name

    def how_cute(self, cute_adjectiv):
        print('{} is the {}!!!'.format(self.name, cute_adjectiv))


class Ola(Us):
    pass


class Mako(Us):
    pass


O = Ola('Ola')
print(O.how_cute('cutest'))


# attempt II
class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    def fahrenheit(self):
        return self._temperature * 1.8 + 32

    def kelvin(self):
        return self._temperature + 273

    @property
    def temp(self):
        return self._temperature

    @temp.setter
    def temp(self, temp_value):
        if temp_value < -273:
            raise ValueError('not possible to go over -273')
        self._temperature = temp_value


man = Celsius(34)
print(man.temp)


# attempt III
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self._year = year

    def type(self):
        if 'GT'.lower() in self.brand:
            return 'The {} is a racing car.'.format(self.brand)
        return 'The {} is a pretty ok car'.format(self.brand)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        if new_year > 2000:
            self._year = new_year
            print('the model is ready for registration')
        else:
            raise ValueError(' The model is not registration approved')


class Car(Vehicle):
    def door_number(self, number):
        if number > 4:
            return 'This {} is a hatchback'.format(self.brand)
        else:
            return '{} model is a sedan'.format(self.brand)


a = Car('toyota gt ', 2001)
print(a.type())


# attempt IV
# bookstore- author, book number, languages, merchendise
# books- sections, book number, years, authors
class Library:
    new_book = 0
    all_books = []

    def __init__(self, book, author, book_number= 350):
        self.book = book
        self.author = author
        self.book_number = book_number
        Library.new_book += 1
        Library.all_books.append(self.book)

    def by_author(self):
        by_author = []
        by_author.append(self.author)
        return by_author


    def count(self):
        total_books = self.book_number + Library.new_book
        return 'There is a total of {} books in our library'.format(total_books)

class Section(Library):
    def __init__(self, book, author, book_number, language, genre ):
        super().__init__(book,author, book_number)
        self.genre = genre
        self.langauge = language


b = Library('maitrey', 'mircea elliade')
print(b.all_books)
print(b.by_author())
v = Library('gaudeamus', 'mircea eliad')
print(v.by_author())
print(v.all_books)
print(v.count())




class Train:

    def __init__(self, num_cars):
        self. num_cars = num_cars

    def __repr__(self):
        return 'There are {} of cars on this train'.format(self.num_cars)
    def __len__(self):
        return self.num_cars

t= Train(4)
print(t)



