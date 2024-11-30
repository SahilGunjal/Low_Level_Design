from abc import abstractmethod, ABC

"""
Liskov Substitution Principle: It states that Objects of a superclass should be replaceable with objects of its
subclasses without affecting the correctness of the program.
"""


class Vehicle(ABC):
    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def noOfWheels(self):
        pass


class Car(Vehicle):
    def startEngine(self):
        print("Car has started")

    def noOfWheels(self):
        print("Car has 4 wheels")


class Bicycle(Vehicle):
    def startEngine(self):
        # This doesn't make any sense
        pass

    def noOfWheels(self):
        print("Bicycle has 2 wheels")

# So, here in this approach we cannot really implement method startEngine as it doesn't make
# any sense so it's violating the LSP

# Solution is
# 1. change method to start instead of start engine and then in Bicycle enter "Started Pedaling"
# 2. Create another abstract classes called hasEngine and notHasEngine (extending Vehicle) and then put those
# startEngine method in that class only for hasEngine... and put another method in notHasEngine
# and then Car will extend hasEngine and Bicycle will extend the notHasEngine

# For simplicity just implement first
# All same just change startEngine method to start() and change the description in Bicycle
# class as "Started Pedaling"