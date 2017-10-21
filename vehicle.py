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
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        return 'Vehicle Type not defined'