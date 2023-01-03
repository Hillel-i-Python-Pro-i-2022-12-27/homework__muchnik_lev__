# Создайте свой произвольный класс и в нём помимо обычных методов и
# атрибутов создайте несколько статических методов и методов класса.
# Продемонстрируйте их работу.
from  datetime import date

class Chel:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18




Chelik1 = Chel('Sarah', 25)
Chelik2 = Chel.from_birth_year('Roark', 1994)

print(Chelik1.name, Chelik1.age)

print(Chelik2.name, Chelik2.age)


