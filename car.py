from vehicle import Vehicle
class Car(Vehicle):
	top_speed = 180
	
	def set_car_type(self, type):
		self.type = type
	
	def vehicle_type(self):
		return self.type