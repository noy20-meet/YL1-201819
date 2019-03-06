import turtle, math
turtle.bgpic("kitchen.gif")
turtle.register_shape("image.gif")
turtle.shape("image.gif")
turtle.goto(0,0)

eat = False
running = True 
movable = True
pizza = turtle.Turtle()
pizza.pu()
turtle.Screen().register_shape("pizza1.gif")
pizza.shape("pizza1.gif")
pizza.goto(0,200)

screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

# def movearound():

		
	

# def collide(pizza):

def dragging(x, y):
    # pizza.ondrag(None)
    pizza.goto(x, y)
    # pizza.ondrag(dragging)
    # collisions()
pizza.speed=('fastest')
pizza.ondrag(dragging)






	#distance= math.sqrt((0-pizza.xcor())**2+(-pizza.ycor())**2)
	#if distance<=10:
	#	return True
	#else:
	#	return False


def spacebar():
	global eat, movable
	movable = True
	print("reached")
	if sleep==False:
		turtle.bgpic("kitchen.gif")
		eat = True
	else:
		turtle.bgpic("kitchen.gif")
		sleep = False

turtle.listen()





turtle.mainloop()