import tkinter as tk
from tkinter import simpledialog
a = [5, 10, 15, 20, 25]
def num(list1):
	b = [list1[0], list1[-1]]
	return b
print(num(a))
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d=[]
for num in c:
	if num < 5:
		
		d.insert(1, num)
		
print(d)
h=[]
 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in b:
	
		h.insert(1,num)
print(h)
answer = int(simpledialog.askstring("Input", "Your message here!",
                                parent=tk.Tk()))
IsPrime = True
for i in range(2,answer):
	if answer%i==0:
		IsPrime = False
if IsPrime:
	print("the number is prime") 
else:
	print("not a prime")	


