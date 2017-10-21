from vehicle import Vehicle
class Motorcycle(Vehicle):
    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        return 'motorcycle type'
