import unittest
from car import *
from truck import *
from motorcycle import *


class CarClassTest(unittest.TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        honda = Car('Honda', 4.5, 'legacy', 'SG-3G',2012, 2017)
        self.assertIsInstance(honda, Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        honda = Car('Honda', 4.5, 'legacy', 'SG-3G',2012, 2017)
        self.assertTrue((type(honda) is Car), msg='The object should be a type of `Car`')

if __name__ == "__main__":
    unittest.main(exit = False)
