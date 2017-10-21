from abc import ABCMeta, abstractmethod
class Vehicle(object):
    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, name, miles, make, model, year, sold_on):
        self.name = name
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year

    def set_number_of_wheels(self, wheels):
        self.wheels = wheels

    def number_of_wheels(self):
        if self.wheels is not None:
            return 4
        return self.wheels

    def price_of_vehicle(self):
        if self.year is not None:
            return 0.0  # Already year
        return (5000.0 * self.wheels) + (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        return 'Vehicle Type not defined'