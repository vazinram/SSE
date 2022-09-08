x = int(input("please enter number one for ADD:"))
y = int(input("please enter number two for ADD:"))
z = int(input("please define Sum, MULTIPLY, dIVIDING, Subtract by 1, 2, 3 and 4"))
#Basic 2-number Calculator Functions
def add(x,y):
	return x+y

def multiply(x,y):
	return x*y

def subtract(x,y):
	return x-y

def divide(x,y):
	return x/y

def square(x,y):
    return x**y
    
if z==1:
    print(add(x,y))
elif z==2:
    print(multiply(x,y))
elif z == 3:
    print(subtract(x,y))
elif z==4:
    print(divide(x,y))
elif z==5:
    print(square(x,y)) 