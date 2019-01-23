from turtle import * 
import turtle
class Ball(Turtle):
 	
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		self.shapesize(self.r/10) 		
		self.color(color)
		self.showturtle()
		#x and y positions
	def move(self, screen_width, screen_height):
		current_x=self.xcor()
		new_x = self.dx+current_x
		current_y=self.ycor()
		new_y = self.dy+current_y
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y-self.r
		self.goto(new_x,new_y)
		#right edge
		if (right_side_ball>screen_width):
			self.dx=self.dx*(-1)
			#left edge
		if (left_side_ball<-screen_width):
			self.dx=self.dx*(-1)
			#up edge
		if (up_side_ball>screen_width):
			self.dy=self.dy*(-1)
			#down edge
		if (down_side_ball<-screen_width):
			self.dy=self.dy*(-1)
	def new_Ball(self, x, y, dx, dy, r, color):
		self.penup()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		self.shapesize(self.r/10)
		self.color(color)
	def delete(self):
		self.reset()



 					





 		