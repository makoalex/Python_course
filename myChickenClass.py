class Chicken:
    total_eggs = 0

    def __init__(self, name, species, eggs=0):
        self.name = name
        self.species = species
        self.eggs = eggs

    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs = self.eggs + 1
        return " {} of the {} species has laid a total of {} eggs.".format(self.name, self.species, self.eggs)


print(Chicken.total_eggs)
lil_chick = Chicken('Fluffer', 'Silkie', 1)
print(Chicken.total_eggs)
print(lil_chick.lay_egg())
chicky = Chicken('chilly', 'Araucana', 4)
print(chicky.lay_egg())
print(Chicken.total_eggs)
print(id(chicky.total_eggs))
print(id(lil_chick.total_eggs))


# user class
class User:
    active_users = 0
    @classmethod
    def users_site(cls):
        return 'we have a total of {} on the site'.format(User.active_users)
    @classmethod
    def from_string(cls, data):
        first, last, age = data.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    def __repr__(self):
        return '{} is {}'.format(self.first, self.age)

    def login(self):
        User.active_users +=1
        return '{} has logged in'.format(self.first)

    def log_out(self):
        User.active_users -= 1
        return '{} {}has log out'.format(self.first, self.last)

    def full__name(self):
        return '{} {} is the full name'.format(self.first, self.last)

    def happy_bday(self):
        self.age += 1
        return 'Happy birthday {}'.format(self.first)

    def senior_discount(self):
        if self.age >= 60:
            return 'we have a senior package'
        return 'you have {} until you can enjoy retirement'.format(60-self.age)


user1 = User('Ola', 'Løvholm', 61)
user2=User.from_string('Mako, Taco, 35')
print(user2)
print(user1)

