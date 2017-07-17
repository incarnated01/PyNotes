#Ministry of Silly Codes July 2017
#The prologue
#Variables; Operations with variables, and I/O.

#A variable is a named place in memory that can store information.
#Modules are included with import statements
import math

x = 7
print(x)

#>>> x = 7
#>>> print(x)
#7
#>>> 

#Remember = is an assignment operator.  == means equality

#All variables have types.  Python will auto type based on what is assigned.
#Logical and mathematic functions can be performed on variables with the results varying based on data type.

intrest_rate = 0.03
principal = 1000
intrest_earned = intrest_rate*principal
total_amount = principal+intrest_earned

number_of_weeks = 26
number_of_days = number_of_weeks*7

city_name = "Los Angeles"
state_name = "California"
zip_code = "90001-5151"

address = city_name+state_name+zip_code

#Assignment, like Hebrew and Arabic, reads right to left

#Iteration is a very important operation

y=5
y+=1

print(y)

#>>> y=5
#>>> y+=1
#>>> print(y)
#6
#>>> 

#I/O is a primary need for any interactive system. (So much so the entire field of UX exists.)
#I/O is very complex because the user is unpredictable. (Hence the need for so much hardware devoted to it.)
#Remember that I/O also includes writing to storage and the cloud as well as get and post requests over the network.
#The philosophical question here is do scripts given to the browser count as I/O?

#print function is the most basic output command
print("One space for each","comma.\n", "Input next")

#>>> print("One space for each","comma.\n", "Input next")
#One space for each comma.
# Input next

#input in python is very clever
Question0 = input("What is your favorite color?")
print(Question0)

#>>> Question0 = input("What is your favorite color?")
#What is your favorite color?
#blue

#>>> print(Question0)
#blue

#input command results are always typed string.
a = input("Enter a value for a:")
b = input("Enter a value for b:")
print("The sum of a and b is ", a+b)

#>>> a = input("Enter a value for a:")
#Enter a value for a:
#1
#>>> b = input("Enter a value for b:")
#Enter a value for b:
#2
#>>> print("The sum of a and b is ", a+b)
#The sum of a and b is  12

#But conversion is fun and easy.
#int(x [,base])  #Converts x to an integer. base specifies the base if x is a string.
#long(x [,base] )  #Converts x to a long integer. base specifies the base if x is a string.
#float(x)  #Converts x to a floating-point number.
#complex(real [,imag])  #Creates a complex number.
# str(x)  #Converts object x to a string representation.
#repr(x)   #Converts object x to an expression string.
#eval(str)  #Evaluates a string and returns an object.
#tuple(s)  #Converts s to a tuple.
#list(s)  #Converts s to a list.
#set(s)  #Converts s to a set.
#dict(d)  #Creates a dictionary. d must be a sequence of (key,value) tuples.
#frozenset(s)  #Converts s to a frozen set.
#chr(x)  #Converts an integer to a character.
#unichr(x)  #Converts an integer to a Unicode character.
#ord(x)  #Converts a single character to its integer value.
#hex(x)  #Converts an integer to a hexadecimal string.
#oct(x)  #Converts an integer to an octal string.

a = int(input("Enter a value for a:"))
b = int(input("Enter a value for b:"))
print("The sum of a and b is ", a+b)

#>>> a = int(input("Enter a value for a:"))
#Enter a value for a:
#1

#>>> b = int(input("Enter a value for b:"))
#Enter a value for b:
#2

#>>> print("The sum of a and b is ", a+b)
#The sum of a and b is  3

a = eval(input("Enter a value for a:"))
b = eval(input("Enter a value for b:"))
print("The sum of a and b is ", a+b)

#A bit more code.

radius = float(input("Enter the radius:"))
area = math.pi*radius*radius
print("The area is", str(area))






