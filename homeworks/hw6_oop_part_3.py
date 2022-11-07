from abc import abstractmethod, ABC

# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
# Example:
#
# for i in FibonacciNumbers(10):
#     print(i)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55


class FibonacciNumbers:
    number = 0
    next_number = 1

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        n = self.number
        if self.value >= 0:
            self.value -= 1
            self.number, self.next_number = self.next_number, self.number + self.next_number
            return n
        else:
            raise StopIteration


for i in FibonacciNumbers(10):
    print(i)

# 2.* Implement generator for Fibonacci numbers


def fibonacci_generator(value):
    number = 0
    next_number = 1
    while value >= 0:
        value -= 1
        yield number
        number, next_number = next_number, number + next_number


for i in fibonacci_generator(10):
    print(i)


#
# 3. Write generator expression that returns square numbers of integers from 0 to 10

square_numbers = (number * number for number in range(0, 10))
for i in square_numbers:
    print(i)

#
# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.


class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):

    def screen(self):
        print("This is screen")

    def keyboard(self):
        print("This is keyboard")

    def touchpad(self):
        print("This is touchpad")

    def webcam(self):
        print("This is webcam")

    def ports(self):
        print("These are ports")

    def dynamics(self):
        print("These are dynamics")

#
# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.


class Car(ABC):

    def drive(self):
        print("I'm driving")

    def stop(self):
        print("I'm stopping")

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
