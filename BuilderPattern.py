"""
Builder pattern in python

I have used builder pattern to create models for APIs. In builder pattern we are building the object step by step and
it is not just created with constructor.

Constructor can be used to set the non-optional fields and rest can be built step by step using methods
"""


class Car:

	def __init__(self, brand):
		self.brand = brand
		self.fuel = None
		self.color = None
		self.gearBox = None

	def __str__(self):
		return "brand : " + str(self.brand) + " | fuel : " + str(self.fuel) + " | color : " + str(self.color) + " | gearBox : " + str(self.gearBox)

	def setFuel(self, fuel):
		self.fuel = fuel
		return self

	def setColor(self, color):
		self.color = color
		return self

	def setGearBox(self, gearBox):
		self.gearBox = gearBox
		return self


c1 = Car("BMW")
c1.setFuel("Petrol").setColor("black")
print(c1)
