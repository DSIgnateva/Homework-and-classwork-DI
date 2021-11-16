from abc import ABC, abstractmethod
import math


# онлайн-задание

class CellularSubscribers:
    def __init__(self, surname, name, patronymic,
                 date_of_birth, gender, connection_date, balance, tariff):
        """
        :param surname: user's surname
        :param name: user's name
        :param patronymic: user's patronymic
        :param date_of_birth: user's date of birth
        :param gender: user's gender
        :param connection_date: users's connection_date
        :param balance: user's balance
        :param tariff: user's tariff
        :return
        """
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.connection_date = connection_date
        self.balance = balance
        self.tariff = tariff


class GeometricFigure(ABC):
    @abstractmethod
    def square(self):
        """
        calculates the square of a shape
        :return:
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        calculates the perimeter of a shape
        :return:
        """
        pass


class Circle(GeometricFigure):
    pass


class Guadrilateral(GeometricFigure, ABC):
    pass


class Rectangle(Guadrilateral):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2


class Trapezoid(Guadrilateral):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        if a > b:
            self.a, self.b = self.b, self.a
        self.c = c
        self.d = d

    def square(self):
        h = (self.c ** 2 - (self.b - self.a) ** 2) * (1 / 2)
        return ((self.a + self.b) / 2) * h

    def perimeter(self):
        return self.a + self.b + self.c + self.d


class Parallelogram(Guadrilateral):
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle  # угол указывается в радианах

    def square(self):
        return self.a * self.b * math.sin(self.angle)

    def perimeter(self):
        return (self.a + self.b) * 2


# домашняя работа


class Writers:
    def __init__(self, year_of_birth, year_of_death, name, surname, alias, country, list_of_works: list):
        """
        :param year_of_birth: year of birth of the writer
        :param year_of_death: year of death of the writer (specify None if the writer is alive)
        :param name: the name of the writer
        :param surname: surname of the writer
        :param alias: writer pseudonym
        :param country: country of the writer
        :param list_of_works: writer's work
        :return
        """

        self.year_of_birth = year_of_birth
        self.year_of_death = year_of_death
        self.name = name
        self.surname = surname
        self.alias = alias
        self.country = country
        self.list_of_works = list_of_works

    def add_work(self, work):
        self.list_of_works.append(work)


class Publisher:
    def __init__(self, name, year_of_creation):
        self.name = name
        self.year_of_creation = year_of_creation


class Work:
    def __init__(self, writers: list, publishers: list, year):
        """
        :param writers: list of objects of class writer
        :param publishers: list of objects of class publisher
        :param year: year of writing
        :return
        """

        self.writers = writers
        self.publishers = publishers
        self.year = year

    def add_writers(self, writer):
        self.writers.append(writer)


class Book(Work):
    def __init__(self, binding, cover):
        self.binding = binding
        self.cover = cover


class Journal(Work):
    def __init__(self, type_of_cover):
        """
        :param type_of_cover: type of journal cover
        :return
        """
        self.type_of_cover = type_of_cover


class Publication(Work):
    def __init__(self, place):
        """
        :param place: internet or newspaper
        :return
        """
        self.place = place
