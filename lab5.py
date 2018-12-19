import random
from turtle import *
import turtle
#1
colormode(255)
class Square (Turtle):
	def __init__(self, size, speed):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		self.speed(speed)

	def random_color (self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(r,g,b)
		self.speed(10)
s = Square(10,10)
s.random_color()

#2
class Hexagon(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		for i in range (6):
			self.begin_poly()
			self.fd(100)
			self.right(60)
			self.end_poly()
		p = get_poly()
		register_shape("Hexagon", p)
turtle.mainloop()		

#3 is in all of them
