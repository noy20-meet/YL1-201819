import turtle
from turtle import *
import time
import random
import math
from ball import Ball
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
running = True
turtle.setup (width=2000, height=1500, startx=0, starty=0)
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2
#part1-make balls
my_ball=Ball(0,0,10,10,20,'red')
number_of_balls=19
minimum_ball_radius =2
maximum_ball_radius=100
minimum_ball_dx=-5
maximum_ball_dx=5
minimum_ball_dy=-5
maximum_ball_dy=5
#score
scores=turtle.Turtle()
scores.hideturtle()
scores.penup()
scores.color("Black")


scores.goto(540, 400)
scores.pendown()
score=0



#try again butten
global BALLS

tryagain= turtle.Turtle()



def GenerateBalls(IsFirst):
	global BALLS
	if IsFirst:
		BALLS = []
		for i in range(number_of_balls):
			new_ball_x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius )
			new_ball_y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
			new_ball_dx = random.randint(minimum_ball_dx, maximum_ball_dx)
			new_ball_dy = random.randint(minimum_ball_dy, maximum_ball_dy)
			new_ball_r = random.randint(minimum_ball_radius, 80)
			new_ball_color = (random.random(), random.random(), random.random())
			new_ball = Ball(new_ball_x,new_ball_y,new_ball_dx,new_ball_dy,new_ball_r,new_ball_color)
			BALLS.append(new_ball)
			print("created")
	else:
		for ball in BALLS:
			new_ball_x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius )
			new_ball_y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
			new_ball_dx = random.randint(minimum_ball_dx, maximum_ball_dx)
			new_ball_dy = random.randint(minimum_ball_dy, maximum_ball_dy)
			new_ball_r = random.randint(minimum_ball_radius, 80)
			new_ball_color = (random.random(), random.random(), random.random())
			ball.new_Ball(new_ball_x,new_ball_y,new_ball_dx,new_ball_dy,new_ball_r,new_ball_color)
			print("created")
		print(BALLS)
def move_all_balls():
	for ball in BALLS:
		 ball.move(screen_width, screen_height)
#part3-collision
def collide(ball_a, ball_b):
	if (ball_a==ball_b):
		return False
	distance=((ball_a.xcor()-ball_b.xcor())**2+(ball_a.ycor()-ball_b.ycor())**2)**.5	
	if (distance<=ball_a.r+ball_b.r):
		return True
	else:
		return False

def tryagain1(x,y):
	global running,score
	score = 0
	GenerateBalls(False)
	running=True
	my_ball.new_Ball(0,0,10,10,20,'red')
	tryagain.hideturtle()
	scores.clear()
	turtle.clear()
	rungame()
#part 4-Check collisions for all balls
def check_all_balls_collision():
	global running, score
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
		#This code will put our ball (my_ball) to be in a new list called all_balls
	for ball_a in all_balls:
		for ball_b in all_balls:
			if (collide(ball_a,ball_b)):
				r1=ball_a.r
				r2=ball_b.r
				new_ball_x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius )
				new_ball_y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
				new_ball_dx = random.randint(minimum_ball_dx, maximum_ball_dx)
				new_ball_dy = random.randint(minimum_ball_dy, maximum_ball_dy)
				new_ball_r = random.randint(minimum_ball_radius, maximum_ball_radius)
				new_ball_color = (random.random(), random.random(), random.random())
				if(r1>r2):
					ball_b.new_Ball(new_ball_x,new_ball_y,new_ball_dx,new_ball_dy,new_ball_r,new_ball_color)
					ball_a.r=ball_a.r+6
					ball_a.shapesize(ball_a.r/10)
					if (my_ball==ball_a):
						print("hello")
						score=score+10
						scores.clear()
						scores.write("score = 000"+str(score) , align= "center" , font= ("Comic Sans MS" , 20 , "normal"))
						if(score>300):
							turtle.write("***YOU WON***", align="center", font=("Comic Sans MS", 80, "normal"))
							turtle.Screen().register_shape("butten.gif")
							tryagain.showturtle()
							tryagain.penup()
							tryagain.goto(0,-200)
							tryagain.pendown()
							tryagain.shape("butten.gif")
							tryagain.onclick(tryagain1)	
							turtle.listen()
							
							

					if(my_ball==ball_b):
						running=False
						turtle.write("***GAME OVER***", align="center", font=("Comic Sans MS", 80, "normal"))
						turtle.Screen().register_shape("butten.gif")
						tryagain.showturtle()
						tryagain.penup()
						tryagain.goto(0,-200)
						tryagain.pendown()
						tryagain.shape("butten.gif")
						tryagain.onclick(tryagain1)	
						turtle.listen()
						# turtle.done()


						
						# turtle.exitonclick()
					
					
						

						

						#turtle.exitonclick()


				else:
					ball_a.new_Ball(new_ball_x,new_ball_y,new_ball_dx,new_ball_dy,new_ball_r,new_ball_color)
					ball_b.r=ball_b.r+4
					ball_b.shapesize(ball_b.r/10)
					if(my_ball==ball_a):
						running=False
						turtle.write("***GAME OVER***", align="center", font=("Comic Sans MS", 80, "normal"))
						turtle.Screen().register_shape("butten.gif")
						tryagain.showturtle()
						tryagain.penup()
						tryagain.goto(0,-200)
						tryagain.pendown()
						tryagain.shape("butten.gif")
						tryagain.onclick(tryagain1)	
						turtle.listen()
						# turtle.done()

						# turtle.exitonclick()

						#tryagain.goto(0,-150)
						#print('here1')
						#turtle.register_shape("tryagain.gif")
						#tryagain.shape("tryagain.gif")
						#print('here2')
						#if i gush the byssun running=true



				#for ball in all_balls:
					#if(my_ball<ball):
					#	running=True
					#else:
					#	running=False		
	
#Part 5: Movearound	
def movearound():
	x=turtle.getcanvas().winfo_pointerx()-screen_width
	y=screen_height-turtle.getcanvas().winfo_pointery()
	my_ball.goto(x,y)

#Part 6: The While Loop



def rungame():
	global running
	while running :
		screen_width=turtle.getcanvas().winfo_width()/2
		screen_height=turtle.getcanvas().winfo_height()/2

		movearound()
		move_all_balls()
		check_all_balls_collision()
		
		
		time.sleep(.1)
		turtle.update() 
GenerateBalls(True)
rungame()


turtle.mainloop()




