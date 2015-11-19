import datetime

# Class that can be used as a function

class Add:
    def __init__(self, default=0):
        self.default = default

    # used when an instance of the Add class is used as a function
    def __call__(self, extra=0):
        return self.default + extra

add2 = Add(2)
print(add2(5))
# >> 7


class Person:
    def __init__(self, name, birth_date=None):
        self.name = name
        self.birth_date = birth_date

    @property
    def days_alive(self):
        raturn (datetime.datetime.today() - self.birth_date).days

me = Person(name="Ken", birth_date=datetime.datetime(1981, 5, 23))
print(me.days_alive)
