import turtle
from turtle import *
import random

# title.hideturtle()
# sbutt.hideturtle()
# slbutt.hideturtle()
# ebutt.hideturtle()
# gbutt.hideturtle()
# duck.hideturtle()


turtle.bgpic("kitchen.gif")
turtle.register_shape("kitchen.gif")
# turtle.shape("kitchen.gif")

#duck turtle
duck = turtle.clone()
duck.hideturtle()
duck.penup()
duck.goto(200,-200)
duck.showturtle()
turtle.register_shape("image.gif")
duck.shape("image.gif")

#pizza turtle
pizza= turtle.clone()
pizza.penup()
turtle.register_shape("pizza1.gif")
pizza.shape("pizza1.gif")

def dragging(x, y):
    pizza.ondrag(None)
    pizza.setheading(pizza.towards(x, y))
    pizza.goto(x, y)
    pizza.ondrag(dragging)
    collisions()
pizza.speed=('fastest')
pizza.ondrag(dragging)


def collisions():
  pizza.radius=20
  duck.radius=100
  
  d=math.sqrt(math.pow(duck.xcor()-pizza.xcor(),2)+ math.pow(duck.ycor()-pizza.ycor(),2))
  if (d<=duck.radius + pizza.radius):
    print("shalalalalala")
    pizza.hideturtle()
    pizza.goto(-500,0)
    pizza.showturtle()
hbutt = turtle.clone()
turtle.register_shape("home.gif")
hbutt.shape("home.gif")
hbutt.speed(0)
hbutt.pu()
hbutt.goto(-650,300)
# hbutt.onclick(goto_home)   '


turtle.mainloop()