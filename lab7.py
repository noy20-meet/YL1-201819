#import Tkinter as tk
#import tkSimpleDialog

#Then when ever you want to ask the user for input use this code:
#greeting = tkSimpleDialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
#if greeting in ("Arrr!"):
#	print("Go away, pirate.")
#else:
#	print("Greetings, hater of pirates!")
# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

#import Tkinter as tk
#import tkSimpleDialog

#year = tkSimpleDialog.askinteger("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw())

#if year <= 1900:
 #   print ("Woah, that's the past!")
#elif year > 1900 and year < 2020:
 #   print ("That's totally the present!")
#else:
 #   print ("Far out, that's the future!!")

#
# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

#class Person:
 # def __init__(self, first_name, last_name):
#	self.first = first_name
#	self.last = last_name
 # def speak(self):
  #	print("My name is " + self.first + " " + self.last)

#me = Person("Brandon", "Walsh")
#you = Person("Ethan", "Reed")

#me.speak()
#you.speak()

import Tkinter as tk
import tkSimpleDialog
# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+		A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

# exam_one = tkSimpleDialog.askinteger("Input", "Input exam grade one: ", parent=tk.Tk().withdraw())

# exam_two = tkSimpleDialog.askinteger("Input"," exam grade two: ", parent=tk.Tk().withdraw())

# exam_three = tkSimpleDialog.askinteger("Input"," exam grade three: ", parent=tk.Tk().withdraw())

# grades = [exam_one, exam_two, exam_three]
# sum = 0
# for i in grades:
#   sum = sum + i

# avg = sum / len(grades)

# if avg >= 90:
#     letter_grade = "A"
# elif avg >= 80 and avg < 90:
#     letter_grade = "B"
# elif avg > 69 and avg < 80:
# 	letter_grade = "C"
# elif avg <= 69 and avg >= 65:
#     letter_grade = "D"
# else:
#     letter_grade = "F"

# for grade in grades:
#     print("Exam: " + str(grade))

#     print("Average: " + str(avg))

#     print("Grade: " + letter_grade)

# if letter_grade is "F":
#     print "Student is failing."
# else:
#     print "Student is passing."
# class Person:
#    def __init__(self,name,age, color = "Red", favorite_food = "Chocolate"):
#        self.name = name
#        self.favorite_food = favorite_food
#        self.age = age
#        self.color = color



#    def define_color(self, color="Red"):
#        self.color = color

#    def print_info(self):
#        print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
#        print("My favorite food is " + self.favorite_food + " and my favorite color is " + self.color)


# a = Person("Britney", 16, "Pizza")
# a.define_color("Black")
# a.print_info()

# b = Person("Jake", 15)
# b.print_info()
# b.define_color()
# class Bear:
#     def __init__(self, name):
#     	self.name = name
#         print("A new bear created. Its name is: " + self.name)
    
#     def say_hi(self):
#         print("hi im a bear! My name is " + self.name)
# my_bear = Bear("Danny")
# (my_bear.say_hi())


# balloons = 5
# name = "Ron"
# color = "Yellow"
# print("This is a tale about " + str(balloons) + " balloons. The first kid is " + name + " who got a  " + color + " balloon ")

# class Cake:
#     def __init__(self, flavor):
#         self.flavor = flavor

#     def eat(self):
#         print("Yummy!!! Eating a" + self.flavor + "cake :)")

# cake = Cake("chocolate")
# cake.eat()
# # what I want to be printed: Yummy!!! Eating a chocolate cake :)

# class Cat:
# 	def __init__(self, name, age=0):
# 		self.name = name
# 		self.age = age
# 	def birthday(self):
# 		currentBirthday = 1
# 		self.age += 1
# 		while currentBirthday < self.age:
# 			print(self.name + " having its " + str(currentBirthday) + " birthday!")
# 			currentBirthday += 1

# my_cat = Cat("Salem", 8)
# my_cat.birthday()
# # what I want: my cat to celebrate its 8th birthday (and all the 
# # birthdays that come before that)
