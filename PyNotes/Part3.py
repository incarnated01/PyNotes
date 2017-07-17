#Ministry of Silly Codes July 2017
#Part3: War
#Program Development and Testing--Loops and Iteration

#Steps: 1. Input, 2. Logic, 3. Output   You should test each step.

#Step1
balance = float(input("Enter how much you want to save: "))
payment = float(input("Enter contribution per period: "))

if(payment<=0):
    payment = float(input("Please enter a positive amount more than 0"))
#Test with a print statement.

#Step2
remainingPayments = balance/payment

#Step3
print(remainingPayments, " payments remain.")

#Test with multiple values... i.e. Input 0 causes error, added code to line 11 IOT solve.

#Loops and Iterations

#While

while(value<=0):
    print("Enter a positive value!")


#Iterate
a = 0
while a<3:
    print(a)
    a+=1
#>>> while a<3:
#...     print(a)
#...     a+=1
#0
#1
#2

#Average age of the people in the room
numPeople = int(input("How many people? "))
i = 0
totalAge = 0.0
while (i < numPeople):
    age = float(input("Input age of person" +str(i+1)+ ": "))
    totalAge = totalAge + age
    i+=1
averageAge = totalAge/numPeople
print("The average age was", averageAge)

#Above code streamlined with a for loop called range here
numPeople = int(input("How many people? "))
i = 0
totalAge = 0.0
for i in range(numPeople): 
    age = float(input("Input age of person" +str(i+1)+ ": "))
    totalAge = totalAge + age
    print("The average age was", averageAge)

#Built in iteration tools. for i in range(a,b,c)
# a being the number to start with, b being the number to go to, c being the size of increment 
for i in range (1,7,2):
    print(i)
#1
#3
#5
#Multiplication table
for i in range(10):
    for j in range(10):
        print(i, '*', j, '=', i*j)

#Pair people
numPeople = input("How many people? ")
for i in range(1, numPeople+1):
    for j in range(i+1, numPeople+1):
        print(i, '&', j, "is one pair")