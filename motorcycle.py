from vehicle import Vehicle
class Motorcycle(Vehicle):
	top_speed = 120
	
	def set_car_type(self, type):
		self.type = type
	
	def vehicle_type(self):
		return self.type

	def set_number_of_pass(self):
		self.passenger = 2

	def number_of_pass(self):
		return self.passenger