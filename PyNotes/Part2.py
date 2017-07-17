#Ministry of Silly Codes July 2017
#Part2: The 3rd World

#Conditional statements rely on a boolean IOT determine if code is executed.
import unittest
isTrue = True
if isTrue:
    print("Condition is true")
else:
    print("Condition is false")

#Also nested:
isTheCase = False
alsoTheCase = False
if isTheCase:
    print("THe 1st case",)
    if alsoTheCase:
        print("Both cases",)
    else:
        print("Not the 2nd case!",)
else:
    print("neither case")

#Elif is a thing.

#Evaluate to Boolean. Use >, <, >=, <=, ==, and !=

a = 1
b = 2
c = 2

if a>2:
    print("A is greater")
else:
    print("A is less")

#Boolean operators: and, or, not.

#More Code

total = LDL+HDL+(TRI/5.0)
if (LDL<100) and (HDL >60) and (TRI<150) and (total<200):
    print("Cholesterol looks great")
elif (LDL>130) or (HDL<50) or (TRI >200) or (total>240):
    print("Warning: Cholesterol looks bad!")
else:
    print("Borderline")
