from turtle import *
import math
import random
import turtle

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10.0)
		self.color(color)
		self.radius = radius
		self.speed(speed)

ball1 = Ball(7, "pink", 1)
ball2 = Ball(5, "blue", 3)
ball3 = Ball(20, "green", 6)

def check_collision(ball1, ball2):
	x1, y1 = ball1.pos()
	x2, y2 = ball2.pos()
	r1 = ball1.radius
	r2 = ball2.radius
	d = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
	if r1+r2 >= d:
		print ("the balls are collide")
	else:
		print("the balls are not collide")

# ball2.penup()
# ball2.goto(100,100)
# ball2.pendown()

list_balls = [ball1, ball2, ball3]
def check_collision2 (list_balls):
	list2=list_balls
	for i in range(len(list_balls)):
		for j in range(len(list_balls)):
			if list_balls[i] != list2[j]:
				check_collision(list_balls[i],list2[j])
			else:
				print("not allowed")





check_collision2(list_balls)



turtle.mainloop()