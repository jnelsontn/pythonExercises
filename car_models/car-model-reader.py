class Car:

	def __init__(self):
		self.carmakes = list()
		self.carmodels = list()

	def read_car_make(self):
	 	with open('car-makes.txt', 'r') as car_makes:
	 		for x in car_makes:
	 			self.carmakes.append(x[:-1])
	 		return self.carmakes

	def read_car_model(self):
	 	with open('car-models.txt', 'r') as car_models:
	 		for y in car_models:
	 		 	self.carmodels.append(y[:-1])
	 		return self.carmodels

	def generate_dictionary(self):
		car_makes = self.read_car_make()
		car_models = self.read_car_model()
		car_dictionary = dict()

		for make in car_makes:
			for model in car_models:
				if make[0] == model[0]:
					car_dictionary[make] = model[2:]
		print(car_dictionary)

CarClass = Car()
CarClass.generate_dictionary()


