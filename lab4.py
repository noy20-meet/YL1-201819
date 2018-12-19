class Rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def Area(self):
		return self.width * self.height
	def Perimeter(self):
		return (self.width + self.height) * 2
	def Print(self):
		print "This rectangle's width is " + str(self.width) + " and the height is " + str(self.height)
rec1= Rectangle(5, 3)
rec1.Print()

class Person(object):
	def __init__(self, age, city, gender, food):
		self.age = age
		self.city = city
		self.gender = gender
		self.food = food
	def Eat(self):
		self.food = "full"
ron = Person(15, "zippori", "girl", "vegi")
Katrina = Person(15, "nazath" , "girl" , "pizza")
ron.Eat()
print(ron.food)		

			


