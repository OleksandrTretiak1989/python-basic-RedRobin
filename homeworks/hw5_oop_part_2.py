# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """
#
class Laptop:
    def __init__(self):
        bat_10000 = Battery('Capacity of the battery is 10000 mAh')
        bat_15000 = Battery('Capacity of the battery is 15000 mAh')
        bat_20000 = Battery('Capacity of the battery is 20000 mAh')
        self.laptop = [bat_10000.capacity, bat_15000.capacity, bat_20000.capacity]


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


laptop = Laptop()
print(laptop.laptop)

# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """


class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring

class GuitarString:
    def __init__(self, brand):
        self.brand = brand

strings_fender =  GuitarString('Fender strings')
guitar_fender = Guitar(strings_fender)

# 3
# class Calc:
#     """
#     Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
#     """

# Я вирішив зробити два варіанти рішення цієї задачі. Через об'єкт і через класс метод

class Calc:
    def __init__(self, attr_1, attr_2, attr_3):
        self.attr_1 = attr_1
        self.attr_2 = attr_2
        self.attr_3 = attr_3

    def add_nums(self):
        return self.attr_1 + self.attr_2 + self.attr_3
s = Calc(1, 2, 3)
print(s.add_nums())

class Calc1:
    attr_11 = 1
    attr_21 = 2
    attr_31 = 3

    @classmethod
    def add_nums1(cls):
        return cls.attr_11 + cls.attr_21 + cls.attr_31

print(Calc1.add_nums1())


#
# 4*.
# class Pasta:
#     """
#     Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
#     Він повинен мати 2 методи:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """
#
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

pasta_1 = Pasta(["tomato", "cucumber"])
print(f"{pasta_1.__class__.__name__} with {pasta_1.ingredients}")

pasta_2 = Pasta.bolognaise()
print(f"{pasta_2.__class__.__name__} with {pasta_2.ingredients}")


# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """
#
class Concert:
    max_visitor_num = 0

    def __init__(self):
         self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitor_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitor_num

Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(f"Visitors count: {concert.visitors_count}")



# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """
#
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


record = AddressBookDataClass(1, "Ivan Ivanov", "+380631234567", "10, Nezalezhnosti, St", "email@gmail.com",
                              "21.04.1989", 33)

print(record)
print(record.phone_number)

# 7. Create the same class (6) but using NamedTuple

import collections
AddressBookDataClass2 = collections.namedtuple("AddressBookDataClass2", ['key', 'name', 'phone_number', 'address',
                                                                         'email', 'birthday', 'age'])

record2 = AddressBookDataClass2(1, "Ivan Ivanov", "+380631234567", "10, Nezalezhnosti, St", "email@gmail.com",
                                "21.04.1989", 33)

print(record2)
print(record2.phone_number)
print(record2[2])

# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
#     """
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"AddressBook(key='{self.key}', name='{self.name}', phone_number='{self.phone_number}', " \
               f"address='{self.address}', email='{self.email}', birthday='{self.birthday}', age='{self.age}')"


record3 = AddressBook(1, "Ivan Ivanov", "+380631234567", "10, Nezalezhnosti, St", "email@gmail.com",
                      "21.04.1989", 33)

print(record3)

# 9.
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"

# Перший варіант простим присвоєнням, а другий (закоментований) через сеттер
class Person:

    name = "John"
    age = 36
    country = "USA"

    # def setage(self, change_age):
    #     self.age = change_age


person_object = Person()
print(person_object.age)
# person_object.setage(33)
person_object.age = 33
print(person_object.age)

#
# 10.
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

class Student:

    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

student_object = Student(1, "John")

setattr(student_object, 'email', 'email@gmail.com')
student_email = getattr(student_object, 'email')
print(student_email)

#Друге (альтернативне рішення):
class Student_1:

    id_1 = 0
    name_1 = ""

student_object_1 = Student_1
student_object_1.email_1 = 'email@gmail.com'
student_email_1 = getattr(student_object_1, 'email_1')
print(student_email_1)
