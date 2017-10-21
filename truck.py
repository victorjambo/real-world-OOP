from vehicle import Vehicle
class Truck(Vehicle):
    top_speed = 80

    def vehicle_type(self):
        return self.type

    def __can_carry_cargo(self):
    	return True

    def speed(self):
    	if self.__can_carry_cargo:
    		top_speed = 40
    	return 80