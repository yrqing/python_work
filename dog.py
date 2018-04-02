class Dog():
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def sit(self):
		# sit
		print(self.name + " sit")




class ElectricDog(Dog):

	def __init__(self):
		super().__init__("electric", 5)


myDog = ElectricDog()
myDog.sit()