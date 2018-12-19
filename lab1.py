import turtle



print ("Noy")
name = "Noy"
print(name*3)
###################
number1 = 3
print(number1)
number2 = number1*0.5
print(number2)
################
list1 = [1, 2, 3]
vr=0
for num in list1:
	vr+=num
	print(vr)
######################
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()
##################


turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
turtle.circle(100)















turtle.mainloop()





