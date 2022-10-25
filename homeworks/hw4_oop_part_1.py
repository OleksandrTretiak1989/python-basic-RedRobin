# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        print("Increasing speed")

    def break_speed(self):
        print("Breaking speed")

    def mileage_info(self):
        print("Mileage info")


# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity
class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self, capacity):
        print(f"Seating capacity is {capacity}")


# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
print(issubclass(Bus, Vehicle))

# 4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
school_bus = Bus(120, 22000)
print(isinstance(school_bus, (Bus, Vehicle)))


# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject
class School:

    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self):
        print("School address is 10, Nezalezhnosti, St")

    def main_subject(self):
        print("Main subject is Ukrainian language")


# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage):
        super().__init__(get_school_id, number_of_students)
        super().__init__(max_speed, mileage)

    def bus_school_color(self):
        print("School bus color is yellow")


s_bus = SchoolBus(7415, 600, 120, 22000)
print(s_bus.school_address(), s_bus.main_subject())
print(s_bus.seating_capacity(40))
print(s_bus.mileage_info())


# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
# створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.
class Bear:
    def __init__(self, food):
        self.food = food
    def eat(self):
        print(f'I am {__class__.__name__} and I eat {self.food}')

class Wolf:
    def __init__(self, food):
        self.food = food
    def eat(self):
        print(f'I am {__class__.__name__} and I eat {self.food}')

fat_bear = Bear('honey')
lazy_wolf = Wolf('meat')
animals = (fat_bear, lazy_wolf)
for animals in animals:
    animals.eat()

# Магічні методи:
# Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише коли population > 1500,
# інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи
class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super(City, cls).__new__(cls)
        else:
            print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population

print('Try to create object "kharkiv" with population 900')
kharkiv = City('Kharkiv', 900)

print('Try to create object "kyiv" with population 2500')
kyiv = City('Kyiv', 2500)

print('Using attributes object "kyiv"')
print(kyiv.name, kyiv.population)
